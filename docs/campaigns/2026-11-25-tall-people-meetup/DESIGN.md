# DESIGN.md

Design system for Tall People Meetup Wellington. This file is written to be read by a design agent, and by a person opening Penpot for the first time.

Read this before making any asset. If something here conflicts with `brand-brief.md`, this file wins for visual decisions and `copy.md` wins for words.

## What this is

A monthly social for tall people in Wellington. First meetup Wednesday 25 November 2026, 5pm to 8pm, Rosie's Red-Hot Cantina, 4 Queens Wharf. Free. All welcome.

Every asset should read as a real night out, the way a venue poster does. Not a startup, not a wellness brand, not a campaign.

## Principles

1. **Facts over attitude.** Date, time, venue, all welcome. If an element carries no fact, remove it.
2. **One accent per surface.** A second colour is a supporting tone at low area, not a second brand.
3. **Hard edges.** No rounded cards, no soft shadows, no glass.
4. **Type does the work.** A poster is allowed to be only type.
5. **Leave room.** Empty space is a design decision, not a gap to fill.
6. **Make it look made.** Visible rules, misregistration, uneven baselines where the era calls for it. Polish reads as a template.

## Colour

Tokens live in `tokens/tokens.json`, in W3C Design Tokens format, grouped by era. Import that file into Penpot and every theme arrives as a set.

The default system is the Swiss theme:

| Token | Value | Role |
| --- | --- | --- |
| `era.swiss.bg` | `#FFFFFF` | Ground |
| `era.swiss.ink` | `#111111` | Text |
| `era.swiss.accent` | `#E30613` | One rule or one word |
| `era.swiss.support` | `#6B6B6B` | Secondary text only, never large |

Twenty themes ship in the same file. Swap the era group to change the whole look. Do not mix two era groups in one asset.

Banned: beige and cream grounds, purple-to-blue gradients behind white text, pastel tints of a saturated colour used as a background.

## Typography

| Role | Family | Fallback | Use |
| --- | --- | --- | --- |
| Display | Archivo Black | Arial Bold | Headlines, dates |
| Text | Inter | Helvetica Neue | Body, captions |
| Mono | IBM Plex Mono | Courier New | Time, address, small labels |

All three are open licence and free to embed. Archivo Black and Inter are on Google Fonts. IBM Plex Mono is OFL.

Rules:

- Display sizes: 28, 40, 64, 96. Nothing between.
- Text sizes: 9, 11, 13, 16. Nothing below 9 at 360px wide.
- Mono is always uppercase with 0.12em to 0.24em tracking.
- Never centre body text. Centre only a short label inside a block.
- No letter-spaced lowercase headings. No outlined text. No text shadows except a 3px hard offset in the surf theme.

## Moodboard system

The visual shortlist is `systems/`. All twenty eras use the same photo-led Memphis structure: solid header, full-width photograph, fact band, palette. Only the palette, fonts and descriptor change.

Use `systems/<era>/board-1.png` for the identity, `board-2.png` for crops and type, and `board-3.png` for the Facebook, Instagram and venue surfaces. The HTML in the same folder is the editable source.

Colour is repaired rather than rejected. When a panel cannot carry its era ink at 4.5:1, the panel moves a few percent towards white or black and the swatch records the new hex.

## Layout

| Format | Size | Margin | Note |
| --- | --- | --- | --- |
| Instagram feed | 1080 x 1350 | 72 | Date is the hero |
| Story and Reel cover | 1080 x 1920 | 72 | Keep text inside the middle 70 percent |
| Facebook event | 1920 x 1080 | 120 | Safe area is the centre 1500 x 900 |
| Facebook page cover | 1640 x 624 | 80 | Mobile crops to the centre 640 |
| Profile | 640 x 640 | 48 | Displays as a circle |

Grid: 12 columns, 24px gutter at 1080 width. Align left unless the era is centred (nouveau, deco, polish).

## Components

**Date block.** Day number at display size, month in mono underneath. The day number is the largest element on any launch asset.

**Detail block.** Three lines, mono, uppercase: day and time, venue, address. Never break the venue across lines.

**Welcome line.** "All welcome" in mono or small caps, always present, always legible. This is the one line that never moves and never shrinks below 9px.

**Height rule.** A vertical or horizontal rule that runs off the edge of the canvas. It comes from pencil marks on a doorframe. One per asset, accent colour.

**Accent block.** One solid shape. A rectangle, a circle or a diagonal band. Never two shapes of the same weight.

## Imagery

Two acceptable modes.

1. **Illustration.** Flat vector, limited palette, no gradients. The giraffe cover is the reference. Do not place type over the animals' heads.
2. **Photography.** Documentary, available light, no eye contact with the camera, no stock smiling. Public domain or CC0 only. Record the source.

Never: 3D renders, glass panels, floating UI cards, isometric scenes, generic line-art people, AI-generated faces.

## Copy

- Short sentences. Specific facts.
- Contractions in social copy. No contractions in documents.
- One dry joke per asset, at most.
- Never "finally", "you deserve", "community-driven", "safe space", "celebrate".
- Never ask "Are you tall?" Describe the meetup instead.
- Always say "all welcome". It is the promise, not a disclaimer.

## Accessibility

Target WCAG 2.2 AA and verify, do not assume.

- Normal text 4.5:1 minimum. Large text (24px, or 18.66px bold) 3:1.
- The era tokens are checked. Run `moodboards/check-contrast.py` after any change.
- No text on a photo without a solid panel behind it.
- Nothing conveyed by colour alone.
- Minimum 9px text at 360px wide, which is 27px at 1080.
- No motion in static assets, so 2.2 and 2.3 do not apply.

## Do not

- Centre the headline and put a small line under it.
- Use three equal boxes with icons.
- Put a rounded card in the middle of a coloured background.
- Use emoji as bullets.
- Stretch an illustration to fill a story frame.
- Reuse one layout without changing the photo, type and palette together.

## Asset checklist

Before an asset ships:

- [ ] Date, time, venue and "all welcome" all present
- [ ] One accent, one era theme, no stray colour
- [ ] Contrast checked
- [ ] Text live, not outlined
- [ ] Reads at 360px wide on a phone
- [ ] Nothing important in the top or bottom 15 percent on stories
