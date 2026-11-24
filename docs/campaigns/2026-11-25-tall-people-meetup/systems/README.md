# Moodboard systems

Twenty design eras, one layout. Every era uses the Memphis board structure the
user picked: a solid header band, a full-width photo, a fact band, then the
palette. Three pages per era, sixty boards in total.

## What is in each folder

| File | What it is |
| --- | --- |
| `board-1.png` | Identity. Number, era, year, name, full-width photo, descriptor, keywords, four swatches with hex. |
| `board-2.png` | Images and type. The same photo cropped four ways, the swatches again, the font triple. |
| `board-3.png` | Applied. Facebook event frame, Instagram frame, venue strip. |
| `*.html` | Editable source. Text stays live, so a later edit is a text edit, not a redraw. |

Every board is 1080 x 1350. There are no carousels and no MP4 files in this
set. The moodboard is the deliverable.

## Regenerate

```
python3 systems/generate.py
bash systems/render.sh
```

`render.sh` writes one PNG next to each HTML file. It needs the repo's
Playwright install and Chrome.

## How colour is decided

`generate.py` tests every text and panel pair. For each panel it tries the era
ink, white, then black. If none clears 4.5:1, it keeps the highest-contrast ink
and moves only the panel colour a few percent towards white or black until the
pair passes. The adjusted hex is written into the swatch, so the board and the
palette agree.

That is a colour change, not a rejection. Every board ships, and every board
meets WCAG 2.2 AA for normal text.

`systems/contrast-check.py` checks the four pairs each board uses. The older
`moodboards/check-contrast.py` covers the one-page sheet only.

`systems/contact_sheet.py` builds `contact-sheet.png`, twenty rows of three
boards, with the era name and year on each row.

## Fonts

Six OFL families, loaded from the Google CDN:

- Archivo Black
- Anton
- Bebas Neue
- Inter
- Space Grotesk
- Space Mono

Install them locally before opening anything in Penpot, or text will reflow.

## Photos

Public domain or CC0 only, recorded in `photos/sources.json`. Each board uses
one photo, cropped four ways for the second page. All twenty eras have their
own image. No stock smiling groups, no AI faces.

## Adding an era

Copy a block in `E`, change the palette, fonts, photo, words and the two lists.
Run the two commands. The contrast guard repairs the palette before anything
renders.

## Editable SVG proof

[swiss/board-1.svg](swiss/board-1.svg) is a live-text SVG version of the Swiss
identity board. Open it in Figma, Illustrator, Affinity Designer or a browser.
The photo and the three OFL fonts are embedded, so the text stays editable
without Penpot. The other boards are still HTML plus PNG.
