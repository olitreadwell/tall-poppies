#!/usr/bin/env python3
"""Check every text and panel pair used on the three-page boards."""

import contextlib
import importlib.util
import io
import pathlib

ROOT = pathlib.Path(__file__).parent


def load():
    spec = importlib.util.spec_from_file_location("generate", ROOT / "generate.py")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def main():
    g = load()
    worst = (99.0, "")
    failures = []
    for era in g.E:
        theme = g.theme(era)
        pairs = [
            ("body", theme["INK"], theme["BG"]),
            ("tag", theme["TAG"], theme["BG"]),
            ("accent panel", theme["ONACC"], theme["ACC"]),
            ("support panel", theme["ONBG2"], theme["BG2"]),
        ]
        for name, fg, bg in pairs:
            ratio = g.cr(fg, bg)
            if ratio < worst[0]:
                worst = (ratio, f'{era["slug"]} {name} {fg} on {bg}')
            if ratio < 4.5:
                failures.append(f'{era["slug"]} {name} {fg} on {bg} = {ratio:.2f}')
    for line in failures:
        print("FAIL", line)
    print(f"{len(g.E) * 4} pairs checked. Lowest: {worst[1]} at {worst[0]:.2f}:1.")
    if not failures:
        print("All pairs meet WCAG 2.2 AA for normal text (4.5:1).")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
