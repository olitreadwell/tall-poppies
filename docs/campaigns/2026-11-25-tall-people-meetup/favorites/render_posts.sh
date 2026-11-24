#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
repo="$(cd "$root/../../.." && pwd)"
for f in "$root"/favorites/posts/*/*.html; do
  if [[ "$f" == *"03-story"* ]]; then
    size="1080,1920"
  else
    size="1080,1350"
  fi
  "$repo/node_modules/.bin/playwright" screenshot \
    --browser chromium --channel chrome \
    --viewport-size "$size" --wait-for-timeout 900 \
    "file://$f" "${f%.html}.png" >/dev/null
  echo "$(basename "$f")"
done
