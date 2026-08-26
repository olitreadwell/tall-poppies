# Adding a venue check (for an agent or a human)

The mechanical steps for turning a venue into a published venue check.

## 1. Check it doesn't already exist

```bash
find docs/reviews/venue-reviews/ -iname "*<venue-slug>*"
```

## 2. Start from the template

```bash
cp docs/reviews/template.md docs/reviews/venue-reviews/<venue-slug>.md
```

## 3. Fill it out

Follow [the Meetup Method framework](review-system.md) — all 8 signals,
the "Who's this for?" verdict, and the "Who would hate this?" call-out.
Don't publish a venue check missing any of those; it's what keeps this
unfiltered instead of another generic write-up.

## 4. Open a PR

```bash
git checkout -b docs/venue-check/<venue-slug>
git add docs/reviews/venue-reviews/<venue-slug>.md
git commit -m "Add venue check: <Venue Name>"
git push -u origin docs/venue-check/<venue-slug>
```

Use the default PR template — it already has the content checklist
(brand-voice consistency, current venue details, etc.).

## What this doesn't cover

Publishing to Instagram, the Broadcast Channel, or any other social
platform is a separate, manual step — nothing in this repo posts on your
behalf. `docs/content/calendar.md` describes the intended cadence and
content pillars, but there's no automation here that runs on a schedule;
treat it as a planning doc, not a live system.
