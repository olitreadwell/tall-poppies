# Using Penpot

Penpot is the right home for this kit. It is open source, runs in a browser, and imports SVG without turning your text into paths, which is the whole point.

I cannot drive the Penpot interface from here. What I can do is hand you files that land in it cleanly, which is the part that usually takes an hour.

## What is ready to import

| File | What it does in Penpot |
| --- | --- |
| `tokens/tokens.json` | W3C design tokens. Twenty era themes plus spacing, radius and stroke. |
| `assets/svg/*.svg` | Seventeen finished layouts with live text. Import as boards, then edit. |
| `moodboards/index.html` | Reference for the twenty directions. Not for import. |
| `DESIGN.md` | The rulebook. Paste it into any agent working inside the file. |

## Import the tokens

1. Open a new Penpot file.
2. Left panel, `Tokens`, then `Import`.
3. Choose `tokens/tokens.json`.
4. Every era appears as a group, for example `era/swiss/bg` with the value `#FFFFFF`.

The file follows the W3C Design Tokens format that Penpot expects: a `$type`, a `$value`, and one value per token. If your version of Penpot rejects it, the likely cause is an older build before token import shipped. Update first.

To apply a theme, point each layer at the era group you want. Swapping `era/swiss` for `era/punk` repaints the file without touching layout.

## Import the layouts

1. `File`, `Import`, `SVG`.
2. Pick one file from `assets/svg/`.
3. Penpot asks whether to import as a single board. Say yes.

What to expect:

- Text arrives as editable text. Fonts fall back to the closest available if Archivo Black or IBM Plex Mono are not installed. Install both first, they are free.
- Groups come in as groups. A `text` element may arrive as a group of one.
- Anything that was rotated in the SVG arrives rotated. Check the angle after import.
- The 1920 x 1080 Facebook cover is the one most likely to need its safe area nudged, because Penpot pads the board on import.

## Working in the file

Set up once, then everything else is fast.

1. Create four pages: `Feed`, `Stories`, `Facebook`, `Scratch`.
2. Put the 1080 x 1350 feed boards on `Feed`, the 1920 x 1080 and 1640 x 624 boards on `Facebook`.
3. Create a component for the detail block. Three text layers, mono, uppercase. Every asset instances it, so changing the venue once changes it everywhere.
4. Create a second component for the welcome line. Lock the text size at 9px minimum.
5. Add a shared colour library from the tokens, so a theme swap is one click.

## Editing text without breaking layout

- Turn off `Auto width` on headline text and set a fixed width. Otherwise a longer word reflows the whole board.
- Keep line height as a multiple, not a pixel value. 0.92 for display, 1.5 for body.
- For the date block, set the day number to a fixed box and align the baseline to the month below it.
- If a font substitution makes a headline overflow, reduce tracking before you reduce size.

## Export

Penpot exports PNG at 1x, 2x or 3x. Use 1x for anything that matches the target pixel size, because 2x doubles the file and Facebook recompresses anyway.

For Instagram, export at the exact board size. Do not let the exporter scale.

## What I still cannot do

- I cannot open your Penpot account, so I cannot save into your team file.
- I cannot click through the interface to fix a broken import.
- I cannot see how a font renders on your machine.

If an import fails, send me the error text and I will adjust the SVG. The SVGs are plain text, so a fix is usually one attribute.
