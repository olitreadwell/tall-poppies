# Skill review

I used `judge-repo` on the two skill sources this kit depends on. `brandkit` is a local skill inside `olitreadwell/ai-harness`. `de-ai-text` is a skill inside `olitreadwell/oss-contrib-pipeline`.

| Repo | Stars | Forks | Contributors | Last push | License | Open issues or PRs |
| --- | --- | --- | --- | --- | --- | --- |
| ai-harness | 0 | 0 | 1 | 17 Nov 2026 | None found | 0 |
| oss-contrib-pipeline | 0 | 0 | 1 | 19 Nov 2026 | None found | 3 |

## Health verdict

Both repos are active, single maintainer personal repos. They are not community projects with a bus factor. `ai-harness` has 118 commits and one merged pull request. `oss-contrib-pipeline` has 787 commits. Neither repo has tags or a release to pin against. Neither repo has a licence.

## Safety verdict

`brandkit` is prompt text and reference material. It has no executable code, install script, or outbound network call. I used it for the design brief and layout direction, not for generated imagery.

`de-ai-text` has a Python checker. `ai-tells.py` reads local text and does not use the network. `sync-tells.py` fetches Wikipedia only when you run it. I ran `ai-tells.py` in gate mode, not the sync script.

## Overall

Pass for local use in this campaign. Caution if you plan to redistribute the skill text or vendor it into another product, because there is no licence.

The main design risk is not the skill. It is the source material. `brandkit` pushes premium brand-board thinking. This campaign deliberately strips that back to a pub notice with one accent and live type. Do not add the usual brand-board gloss later.
