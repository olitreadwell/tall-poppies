#!/usr/bin/env bash
# Render every board and carousel page to PNG at 1080x1350.
set -euo pipefail
shopt -s nullglob
root="$(cd "$(dirname "$0")/.." && pwd)"
repo="$(cd "$root/../../.." && pwd)"
for dir in "$root"/systems/*/; do
  for f in "$dir"*.html; do
    "${repo}/node_modules/.bin/playwright" screenshot \
      --browser chromium --channel chrome \
      --viewport-size "1080,1350" --wait-for-timeout 700 \
      "file://${f}" "${f%.html}.png"
  done
done
