#!/usr/bin/env bash
# Render every core post to PNG at 1080x1350.
set -euo pipefail
root="$(cd "$(dirname "$0")" && pwd)"
repo="$(cd "$root/../../../.." && pwd)"
for f in "$root"/*.html; do
  "${repo}/node_modules/.bin/playwright" screenshot \
    --browser chromium --channel chrome \
    --viewport-size "1080,1350" --wait-for-timeout 1200 \
    "file://${f}" "${f%.html}.png"
done
