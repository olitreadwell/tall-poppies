#!/usr/bin/env python3
"""Compose the twenty moodboards into one labelled contact sheet."""

import contextlib
import importlib.util
import io
import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "contact-sheet.png"
THUMB_W = 400
THUMB_H = 500
GAP = 14
MARGIN = 30
LABEL_H = 34


def load_eras():
    spec = importlib.util.spec_from_file_location("generate", ROOT / "generate.py")
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module.E


def main():
    eras = load_eras()
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    bold_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    label_font = ImageFont.truetype(bold_path, 21)
    note_font = ImageFont.truetype(font_path, 17)

    row_h = LABEL_H + THUMB_H + GAP
    width = MARGIN * 2 + THUMB_W * 3 + GAP * 2
    height = MARGIN * 2 + row_h * len(eras) + 34
    sheet = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(sheet)

    for row, era in enumerate(eras):
        y = MARGIN + row * row_h
        label = f'{era["n"]:02d}  {era["name"]}  /  {era["year"]}'
        draw.text((MARGIN, y), label, fill="#111111", font=label_font)
        for col in range(3):
            src = ROOT / era["slug"] / f"board-{col + 1}.png"
            if not src.exists():
                raise SystemExit(f"Missing {src}. Run render.sh first.")
            image = Image.open(src).convert("RGB")
            image.thumbnail((THUMB_W, THUMB_H), Image.LANCZOS)
            x = MARGIN + col * (THUMB_W + GAP)
            sheet.paste(image, (x, y + LABEL_H))

    note = "Tall People Meetup Wellington  /  25 Nov 2026, 5pm to 8pm  /  Rosie's Red-Hot Cantina  /  all welcome"
    draw.text((MARGIN, height - MARGIN - 18), note, fill="#444444", font=note_font)
    sheet.save(OUT, optimize=True)
    print(OUT, sheet.size)


if __name__ == "__main__":
    main()
