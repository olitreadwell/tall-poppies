#!/usr/bin/env python3
"""Search archive.org for image items with a usable public-domain or CC licence.

Only explicit rights statements pass. Items with no licence field are skipped,
because archive.org hosts plenty of material that is still in copyright.
"""

import argparse
import json
import pathlib
import subprocess
import urllib.parse

UA = "TallPoppiesCampaignBot/1.0 (contact: oli@example.com)"
SEARCH = "https://archive.org/advancedsearch.php"
META = "https://archive.org/metadata/"
DOWNLOAD = "https://archive.org/download/"

ALLOWED = (
    "creativecommons.org/publicdomain/zero/1.0",
    "creativecommons.org/publicdomain/mark/1.0",
    "creativecommons.org/licenses/by/4.0",
    "creativecommons.org/licenses/publicdomain",
    "no known copyright restrictions",
)
IMAGE_FORMATS = {"JPEG", "PNG", "TIFF", "JPEG 2000"}


def curl(url, binary=False, timeout=45):
    result = subprocess.run(
        ["curl", "-sSL", "-m", str(timeout), "-A", UA, url],
        capture_output=True,
    )
    return result.stdout if binary else result.stdout.decode("utf-8", "replace")


def search(query, rows):
    params = {
        "q": query,
        "fl[]": ["identifier", "title", "licenseurl", "rights", "collection", "mediatype"],
        "rows": rows,
        "page": 1,
        "output": "json",
    }
    raw = curl(SEARCH + "?" + urllib.parse.urlencode(params, doseq=True))
    return json.loads(raw).get("response", {}).get("docs", [])


def rights(doc):
    return (doc.get("licenseurl") or doc.get("rights") or "").strip()


def usable(doc):
    value = rights(doc).lower()
    return any(token in value for token in ALLOWED)


def best_image(identifier):
    data = json.loads(curl(META + identifier))
    candidates = []
    for item in data.get("files", []):
        name = item.get("name", "")
        if item.get("format") not in IMAGE_FORMATS:
            continue
        if "_thumb" in name.lower() or name.startswith("__ia_thumb"):
            continue
        try:
            size = int(item.get("size", 0))
        except ValueError:
            size = 0
        if 0 < size <= 50_000_000:
            candidates.append((size, name))
    return max(candidates, default=(0, ""))[1]


def download(url, path):
    result = subprocess.run(
        ["curl", "-sSL", "-m", "120", "-A", UA, "-o", str(path), url],
        capture_output=True,
    )
    if result.returncode != 0 or path.stat().st_size < 20_000:
        raise SystemExit(f"Download failed: {url}")
    return path.stat().st_size


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="archive.org advanced search query")
    parser.add_argument("--out", default="archive-downloads")
    parser.add_argument("--rows", type=int, default=20)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--max", type=int, default=3)
    args = parser.parse_args()

    docs = [doc for doc in search(args.query, args.rows) if usable(doc)]
    if not docs:
        raise SystemExit("No items with an explicit public-domain or CC licence.")

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    sources_path = out / "sources.json"
    sources = json.loads(sources_path.read_text()) if sources_path.exists() else {}

    for doc in docs[: args.max]:
        identifier = doc["identifier"]
        name = best_image(identifier)
        print(f"{identifier} | {doc.get('title', '')[:70]}")
        print(f"  {rights(doc)}")
        if not name:
            print("  no still image file")
            continue
        print(f"  https://archive.org/details/{identifier} | {name}")
        if args.download:
            suffix = pathlib.Path(name).suffix.lower()
            path = out / f"{identifier}{suffix}"
            size = download(DOWNLOAD + f"{identifier}/{urllib.parse.quote(name)}", path)
            print(f"  saved {path} ({size} bytes)")
            sources[path.name] = {
                "identifier": identifier,
                "title": doc.get("title", ""),
                "rights": rights(doc),
                "file": name,
                "url": f"https://archive.org/details/{identifier}",
            }

    if args.download:
        sources_path.write_text(json.dumps(sources, indent=2) + "\n")
        print(f"Wrote {sources_path}")


if __name__ == "__main__":
    main()
