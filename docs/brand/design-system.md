# Design system

## Colour palette

| Colour | Hex | Usage |
| --- | --- | --- |
| Pōneke Amber | `#E87A2A` | Primary accent, CTAs, highlights |
| Tall Timber | `#2C1810` | Dark backgrounds, text |
| Cream Pour | `#F5E6C8` | Light backgrounds |
| Fern Green | `#5A7A4A` | Nature/walk highlights |
| Southerly Blue | `#4A6B8A` | Contrast, evening photography |
| Cloud Cream | `#FAF6F0` | Whitespace |

## Typography

| Element | Font |
| --- | --- |
| Headings | Abril Fatface / Playfair Display |
| Body | Inter / Open Sans |
| Meta (prices, times) | DM Mono |

## Imagery vibe

- Bright, candid group shots — tall people laughing at the back table
- High ceilings, good light, people who can see each other
- Candid, unpolished — never staged
- Edit: natural temp, slight warmth, keep it real

## Applying this in the app

This repo's Tailwind theme and Radix primitives (`src/components/ui`) are
the implementation surface for this palette and type scale — wire these
tokens into `tailwind.config` / the CSS custom properties rather than
hardcoding hex values in components. Brand assets (logo, meetup art, fonts)
live under `assets/`.
