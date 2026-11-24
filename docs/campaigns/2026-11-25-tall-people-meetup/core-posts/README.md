# Six core Instagram directions

Six themes, six layouts, six ways of applying colour. Every post is
1080x1350. The HTML is the source. The PNG is the export.

[Contact sheet](contact-sheet.png) shows all six.

## 01 Surf rad: bring your mates

[HTML](01-surf-mates.html) | [PNG](01-surf-mates.png)

- Layout: vertical split. Art panel on the left, type column on the right.
- Assets: wave-line pattern, a CSS striped sun, one small surfer photo.
- Colour: flat hot pink, cyan and lemon. No gradients.
- Caption: Bring your mates. Tall is not a membership card. Everyone is
  welcome. Wed 25 Nov, 5pm to 8pm, Rosie's Red-Hot Cantina, 4 Queens Wharf.
  All welcome. `#TallPeopleMeetupWellington #Wellington #Pōneke`

## 02 Bauhaus: find the venue

[HTML](02-bauhaus-venue.html) | [PNG](02-bauhaus-venue.png)

- Layout: left type stack, right full-height art crop.
- Assets: public-domain Bauhaus grid poster from `archive-downloads/`. No
  photo.
- Colour: flat primary yellow, red and blue. One blue venue block. The art
  supplies the rest of the colour.
- Caption: Rosie's Red-Hot Cantina, 4 Queens Wharf. Wed 25 Nov, 5pm to 8pm.
  Look for the group that takes up some room. All welcome.

## 03 Memphis: first meetup

[HTML](03-memphis-first.html) | [PNG](03-memphis-first.png)

- Layout: stacked headline, outlined circle, tilted details panel.
- Assets: inline squiggle, dot grid, triangle and outlined shapes. No photo.
- Colour: pastel pink ground with flat teal, lemon and purple blocks.
- Caption: First meetup. A drink and a chat with people who fit. No agenda.
  Just turn up. Wed 25 Nov, 5pm to 8pm, Rosie's, 4 Queens Wharf. All welcome.

## 04 Cyber Y2K: tomorrow

[HTML](04-y2k-tomorrow.html) | [PNG](04-y2k-tomorrow.png)

- Layout: browser window with a terminal panel, a countdown tile and a small
  image window.
- Assets: chrome ramp, chrome star and one duotone city photo.
- Colour: near-black ground, chrome gradients, mint terminal text. The photo
  is duotoned mint.
- Caption: Tomorrow. 5pm. Rosie's. All welcome. Wed 25 Nov, 5pm to 8pm,
  Rosie's Red-Hot Cantina, 4 Queens Wharf.

## 05 Psychedelic: launch

[HTML](05-psychedelic-launch.html) | [PNG](05-psychedelic-launch.png)

- Layout: full-bleed art, headline in the dark top zone, details in a hard
  panel at the bottom.
- Assets: the abstract painting at `photos/10-psychedelic.jpg`. No photo of
  people.
- Colour: the painting is saturated, then pushed under a deep purple
  gradient. Pink outline, green squiggle, pink date disc.
- Caption: You will not be the tallest person in the room. Tall People Meetup
  Wellington launch. Wed 25 Nov, 5pm to 8pm, Rosie's Red-Hot Cantina, 4 Queens
  Wharf. All welcome.

## 06 Rave: today

[HTML](06-rave-today.html) | [PNG](06-rave-today.png)

- Layout: oversized day-of type, marquee bands, details panel with barcode.
- Assets: public-domain rave flyer from `archive-downloads/` used as a dark
  texture, plus an inline neon heart.
- Colour: near-black ground, fluorescent cyan and magenta, offset shadow on
  the headline.
- Caption: Today. 5pm. Rosie's. All welcome. No ticket. Just turn up. Wed 25
  Nov, 5pm to 8pm, 4 Queens Wharf.

## Sources

Archive art is recorded in `../archive-downloads/sources.json`. The two
Bauhaus posters and the rave flyer are public domain mark. Files were resized
to a maximum of 1800 pixels for use here.

## Render

```bash
bash core-posts/render.sh
```
