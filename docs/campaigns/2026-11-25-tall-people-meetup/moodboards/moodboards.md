# Twenty eras

Open `index.html` at full size. `contact-sheet.png` is the same thing as one image.

Same facts on every tile: Wednesday 25 November, 5pm to 8pm, Rosie's Red-Hot Cantina, 4 Queens Wharf, all welcome. Everything else changes.

Version two. The first sheet was twenty layouts in one cream palette. This one has twenty palettes and twenty composition systems, and no beige anywhere.

## The twenty

| No. | Era | Ground | What carries it |
| --- | --- | --- | --- |
| 01 | Victorian playbill, 1850 | white | wood type, double rules, dense columns |
| 02 | Art Nouveau, 1900 | deep green | gold arch, blush hairline, centred |
| 03 | Constructivist, 1920 | black | red diagonal, Impact, one idea |
| 04 | Bauhaus, 1925 | yellow | red circle, blue triangle, lowercase |
| 05 | Art Deco, 1927 | black | gold fan rays, wide tracking, emerald seal |
| 06 | Swiss Style, 1955 | white | Helvetica, strict grid, one red bar |
| 07 | Mid-century travel, 1958 | cobalt | flat hills, sunflower sun, coral shore |
| 08 | Pop Art, 1963 | white | Ben-Day dots, speech bubble, magenta |
| 09 | Polish film poster, 1965 | burgundy | mustard form, muted serif, one shape |
| 10 | Psychedelic, 1967 | deep purple | pink and yellow blobs, tilted type |
| 11 | Funk, 1973 | near-black | orange band, gold rules, heavy slab |
| 12 | Punk zine, 1979 | black | ransom letters, red stripe, no grid |
| 13 | Memphis, 1984 | pink | teal block, yellow dot, zigzag |
| 14 | Corporate brochure, 1986 | navy | teal rules, icon rows, data table |
| 15 | Surf rad, 1991 | hot pink | cyan sky, striped sun, Impact |
| 16 | Rave flyer, 1992 | black | cyan and magenta, repetition, mono |
| 17 | Grunge, 1993 | black | rust highlight, xerox grit, off baselines |
| 18 | Y2K chrome, 1999 | pale blue | metal gradient, bubbles, pill shapes |
| 19 | Frutiger Aero, 2007 | sky gradient | gloss panel, bubbles, aqua |
| 20 | Cyberpunk, 2020 | black | amber CRT, teal, scanlines, barcode |

## Colour

No beige. The lightest grounds are pure white or a cool pale blue, and everything else is a saturated field.

| Role | Values |
| --- | --- |
| Neutrals | `#FFFFFF`, `#000000`, `#0F0F0F`, `#DCE6F2` |
| Reds | `#C8102E`, `#E30613`, `#E01B24`, `#FF1F1F`, `#5C1A1B` |
| Warm | `#FFD400`, `#FFC93C`, `#E0A33E`, `#FF7A1A`, `#FF6B4A`, `#C05621` |
| Cool | `#0B4FA8`, `#0B2A5B`, `#1E3FA8`, `#2BB3C0`, `#00D4FF`, `#00F0FF`, `#5CC8F2` |
| Bright | `#FF2D87`, `#FF2E93`, `#C4005F`, `#FF00C8`, `#FF4FA3`, `#FFD6E8` |
| Green | `#0E3B2E`, `#124C3B`, `#38D66B`, `#1FA37A`, `#00897B` |

## Accessibility

Every text and background pair is measured. The script is `check-contrast.py` and it holds the bar at 4.5:1 for all text, which is stricter than WCAG 2.2 AA asks for headlines.

```
python3 check-contrast.py
49 pairs checked. Lowest: 17 Grunge rust at 4.59:1.
All pairs meet WCAG 2.2 AA for normal text (4.5:1).
```

That covers 1.4.3 Contrast. The other AA points this sheet respects:

- No text sits on an image or a gradient without a solid panel behind it.
- Nothing is conveyed by colour alone. Every poster states the date, time and venue in words.
- Type sizes stay at 8px or above at 360px wide, which is roughly 24px at the 1080px export.
- No motion, so 2.2 Pause and 2.3 Seizure do not apply.

Run it again after any colour change.

## Where these came from

About thirty posters, pulled from public design archives and looked at before anything was drawn.

- https://www.are.na/poster-design
- https://www.are.na/risograph
- https://www.are.na/gig-posters
- https://www.are.na/concert-posters
- https://www.are.na/type-only
- https://www.are.na/wayfinding
- https://www.are.na/editorial-design
- https://www.are.na/swiss-design
- https://fontsinuse.com/tags/25/swiss-style

Icons in 14, 16 and 20 come from Lucide, which is ISC licensed, so commercial use needs no attribution. https://lucide.dev

The useful finding was how much of the work is decided by ink limits. Screenprint gives two colours and an overprint. Newsprint gives black and one red. Riso gives two spot inks with visible misregistration. Fix the ink and the rest follows, which is why these read as periods rather than as styles.

## Picking one

Five days out, pick one era for the whole kit. Mixing eras reads as a folder of templates.

- **15 Surf rad** is the loudest and travels furthest on Instagram.
- **06 Swiss** is the safest, and the easiest to keep tidy across 17 assets.
- **12 Punk** gets shared most often, because it looks made rather than bought.
- **20 Cyberpunk** is the one for Reels covers if you want a second surface. Keep it off the feed.

If you want one recommendation: 15 for launch and stories, 06 for the venue card, page cover and profile.

## What to avoid

- Centred headline with a small line underneath, on every asset.
- Three equal feature boxes with icons.
- Purple gradient behind white sans serif.
- Rounded cards with soft shadows.
- A stock photo of people laughing at a table.
- Emoji as bullets.
- The same layout in twenty colours.

## Editing these

`index.html` is the master. Each tile is plain HTML and CSS, so a colour, font or size change is one line. `v1-type-only.html` keeps the rejected first attempt.

Regenerate the contact sheet with:

```
./node_modules/.bin/playwright screenshot --browser chromium --channel chrome \
  --full-page --viewport-size "1640,1200" \
  "file:///<path>/moodboards/index.html" contact-sheet.png
```
