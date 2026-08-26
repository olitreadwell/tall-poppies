# Tall Poppies Pōneke – GitHub Project Integration Spec

*How the Tall Poppies brand fits into this repo's template structure.*

## File placement map

| Content | Destination | Purpose |
| --- | --- | --- |
| Brand voice, tone, grammar | `docs/brand/README.md` | Core brand voice |
| Colours, typography, imagery | `docs/brand/design-system.md` | Design system |
| Meetup identity concepts | `docs/brand/mascots.md` | 10 mascot prompts |
| Venue framework | `docs/reviews/review-system.md` | The Meetup Method |
| Blank venue check template | `docs/reviews/template.md` | Fill-in template |
| Finished venue checks | `docs/reviews/venue-reviews/` | One file per venue |
| Content calendar & pillars | `docs/content/calendar.md` | Monthly cadence, Broadcast, pillars |
| Humour packs | `docs/content/humor.md` | Kiwi + tall-people jokes |
| Competitor audit | `docs/research/competitor-audit.md` | Pōneke social meetup landscape |
| Brand assets | `assets/images/`, `assets/fonts/`, `assets/templates/canva/` | Logo, mascot art, venue shots, fonts |

`docs/operations/agent-manual.md` (how an LLM should operate the brand) is
referenced by the original brand doc set but hasn't been drafted yet —
add it here once it exists.

## GitHub-specific pieces

- `.github/ISSUE_TEMPLATE/venue_review_request.yml` — crew members suggest
  a meetup venue
- `.github/ISSUE_TEMPLATE/content_idea.yml` — suggest a post/poll/joke
- `.github/PULL_REQUEST_TEMPLATE.md` — Tall Poppies content PR checklist
  (code PRs still use `docs/contributing/templates/PR_DESCRIPTION.md`)

## Brand consistency check (before pushing content)

- [ ] Copy uses the Tall Poppies voice (matey, unfiltered, sentence case)
- [ ] Links resolve to the right doc paths
- [ ] Colours match the design-system palette
- [ ] No corporate fluff
