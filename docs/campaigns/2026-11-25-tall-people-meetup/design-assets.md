# Design asset shelf

Every repo below was checked against the GitHub API on 20 November 2026. Stars rounded. Licences read from the repo metadata.

Use this instead of drawing everything by hand. All of it is free for commercial work, apart from the two rows marked otherwise.

## Icons

| Repo | Licence | Stars | Use it for |
| --- | --- | --- | --- |
| google/material-design-icons | Apache-2.0 | 54k | The full Google set. Best coverage of everyday objects. |
| simple-icons/simple-icons | CC0-1.0 | 26k | Brand marks. Public domain, no attribution. |
| lucide-icons/lucide | ISC | 26k | Clean 1.5px line icons. Already used in three boards. |
| feathericons/feather | MIT | 26k | The original minimal line set. Same feel as Lucide, fewer icons. |
| tabler/tabler-icons | MIT | 23k | 5,000 icons. Best range of UI and transport symbols. |
| microsoft/fluentui-system-icons | MIT | 11k | Filled and regular pairs. Good for a corporate or signage board. |
| microsoft/fluentui-emoji | MIT | 10k | Emoji as flat vector. Commercial safe, unlike most emoji sets. |
| Remix-Design/RemixIcon | Apache-2.0 | 8k | Neutral, slightly rounded. Good at small sizes. |
| twbs/icons | MIT | 8k | Bootstrap Icons. Small, consistent, well drawn. |
| iconoir-icons/iconoir | MIT | 5k | Lighter weight than Tabler. Good for editorial. |
| phosphor-icons/core | MIT | 404 | Six weights of the same set, so you can mix without clashing. |

## Type

| Repo | Licence | Stars | Use it for |
| --- | --- | --- | --- |
| google/fonts | OFL or Apache per family | 21k | Every Google font as source. Start here. |
| rsms/inter | OFL-1.1 | 20k | The default UI sans. Good for Swiss and corporate boards. |
| JetBrains/JetBrainsMono | OFL-1.1 | 13k | Terminal and code faces for the cyberpunk and rave boards. |
| IBM/plex | OFL-1.1 | 12k | One superfamily across sans, serif and mono. |
| adobe-fonts/source-sans | OFL-1.1 | 4k | Quiet, neutral, very legible at small sizes. |

## Colour and systems

| Repo | Licence | Stars | Use it for |
| --- | --- | --- | --- |
| radix-ui/colors | MIT | 2k | Twelve-step scales with contrast already tested. |
| primer/primitives | MIT | 422 | GitHub's colour primitives. Good neutral ramps. |
| carbon-design-system/carbon | Apache-2.0 | 10k | IBM's full component and token system. |
| Shopify/polaris | MIT | 6k | Commerce UI. Archived, still readable. |

## Illustration

| Repo | Licence | Stars | Use it for |
| --- | --- | --- | --- |
| realvjy/illlustrations | MIT | 57 | Hand-drawn vector illustrations. Archived but downloadable. |

Most big illustration libraries are not on GitHub. unDraw and Blush have no public repo. For a community meetup I would stay away from generic illustration anyway, because that is exactly where the AI look lives.

## Avoid

- `bansal/pattern.css` has no licence file, so the default is all rights reserved. Skip it.
- Anything with no `LICENSE` at the repo root. A README promise is not a licence.
- CC BY-SA and CC BY-NC sets for anything you print or boost. Share-alike and non-commercial both bite.

## Photos

Public domain and CC0 images come from Wikimedia Commons. The API returns a licence field per file, so nothing needs guessing.

Search a term, filter to files whose licence is PD or CC0, download the thumbnail. Fourteen photos in `photos/` came through that route and are worth using. The rest came back as maps, book covers and scans, so they were dropped. Source and licence for each survivor are in `photos/sources.json`.

Openverse is the other index worth knowing, at https://api.openverse.org. It is slower and rate limited but covers Flickr and museum collections.
