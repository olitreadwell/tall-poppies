#!/usr/bin/env python3
"""Check every text/background pair in index.html against WCAG 2.2 AA.

Normal text needs 4.5:1. Large text (24px, or 18.66px bold) needs 3:1.
This script holds the bar at 4.5 for everything, so the sheet passes either way.

Run: python3 check-contrast.py
"""

PAIRS = [
    ("01 Victorian ink", "#0A0A0A", "#FFFFFF"),
    ("01 Victorian red", "#C8102E", "#FFFFFF"),
    ("02 Nouveau white", "#FFFFFF", "#0E3B2E"),
    ("02 Nouveau gold", "#F2D06B", "#0E3B2E"),
    ("02 Nouveau on arch", "#FFFFFF", "#124C3B"),
    ("03 Constructivist white", "#FFFFFF", "#0F0F0F"),
    ("03 Constructivist on red", "#FFFFFF", "#E01B24"),
    ("04 Bauhaus ink", "#111111", "#FFD400"),
    ("05 Deco white", "#FFFFFF", "#0A0A0A"),
    ("05 Deco gold", "#E7C56A", "#0A0A0A"),
    ("05 Deco seal", "#0A0A0A", "#1FA37A"),
    ("06 Swiss ink", "#111111", "#FFFFFF"),
    ("06 Swiss red", "#E30613", "#FFFFFF"),
    ("07 Travel white", "#FFFFFF", "#0B4FA8"),
    ("07 Travel yellow", "#FFC93C", "#0B4FA8"),
    ("07 Travel on coral", "#0B1B33", "#FF6B4A"),
    ("08 Pop black", "#000000", "#FFFFFF"),
    ("08 Pop magenta", "#C4005F", "#FFFFFF"),
    ("08 Pop when block", "#000000", "#FF2E93"),
    ("09 Polish body", "#F5F5F0", "#5C1A1B"),
    ("09 Polish accent", "#E0A33E", "#5C1A1B"),
    ("10 Psychedelic white", "#FFFFFF", "#1B0B2E"),
    ("10 Psychedelic yellow", "#FFC93C", "#1B0B2E"),
    ("10 Psychedelic chip", "#0B0410", "#38D66B"),
    ("11 Funk white", "#FFFFFF", "#2A1208"),
    ("11 Funk gold", "#FFC93C", "#2A1208"),
    ("11 Funk on orange", "#2A1208", "#FF7A1A"),
    ("12 Punk white", "#FFFFFF", "#000000"),
    ("12 Punk black on white", "#000000", "#FFFFFF"),
    ("12 Punk red", "#FF1F1F", "#000000"),
    ("13 Memphis black", "#000000", "#FFD6E8"),
    ("13 Memphis teal", "#00575D", "#FFD6E8"),
    ("14 Corporate white", "#FFFFFF", "#0B2A5B"),
    ("14 Corporate teal", "#2BB3C0", "#0B2A5B"),
    ("14 Corporate teal bar", "#0B2A5B", "#2BB3C0"),
    ("15 Surf black", "#0A0A0A", "#FF2D87"),
    ("15 Surf yellow on black", "#FFE94A", "#0A0A0A"),
    ("16 Rave white", "#FFFFFF", "#000000"),
    ("16 Rave cyan", "#00F0FF", "#000000"),
    ("16 Rave magenta", "#FF00C8", "#000000"),
    ("16 Rave chip", "#000000", "#00F0FF"),
    ("17 Grunge white", "#FFFFFF", "#000000"),
    ("17 Grunge rust", "#C05621", "#000000"),
    ("18 Y2K ink", "#1B2E4B", "#DCE6F2"),
    ("18 Y2K blue", "#1E3FA8", "#DCE6F2"),
    ("19 Aero ink, mid sky", "#0A3A4A", "#8EDFF0"),
    ("19 Aero ink, lightest", "#0A3A4A", "#B9F0DA"),
    ("20 Cyberpunk amber", "#FFB000", "#050505"),
    ("20 Cyberpunk teal", "#00E5C0", "#050505"),
]


def luminance(hex_colour: str) -> float:
    value = hex_colour.lstrip("#")
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]

    def linear(channel: float) -> float:
        return channel / 12.92 if channel <= 0.03928 else ((channel + 0.055) / 1.055) ** 2.4

    red, green, blue = (linear(c) for c in channels)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def ratio(foreground: str, background: str) -> float:
    a, b = luminance(foreground), luminance(background)
    lighter, darker = max(a, b), min(a, b)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    failures = 0
    lowest = (999.0, "")
    for name, foreground, background in PAIRS:
        value = ratio(foreground, background)
        state = "pass" if value >= 4.5 else "FAIL"
        if value < 4.5:
            failures += 1
        if value < lowest[0]:
            lowest = (value, name)
        print(f"{name:28} {foreground} on {background}  {value:5.2f}  {state}")
    print()
    print(f"{len(PAIRS)} pairs checked. Lowest: {lowest[1]} at {lowest[0]:.2f}:1.")
    print("All pairs meet WCAG 2.2 AA for normal text (4.5:1)." if failures == 0 else f"{failures} pair(s) below 4.5:1.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
