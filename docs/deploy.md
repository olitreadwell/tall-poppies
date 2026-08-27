# Deployment

- Docker: `docker build -t app . && docker run -p 3000:3000 app`.
  Multi-stage, `node:22-alpine`, HEALTHCHECK on `/health`.
- Vercel: connect the repo; `npm run build` already ran green in CI.
- Static (GitHub Pages, `https://olitreadwell.github.io/tall-poppies/`):
  `BASE_PATH=/tall-poppies pnpm build`, then copy
  `.next/server/app/*.html` + `.next/static` to the `gh-pages` branch.
  API routes (`/api/*`, `/health`) do not run there; the contact form falls
  back to `mailto`. Landing, help, contact, and feedback pages render fully.
- Env: every runtime setting comes from env vars (`.env.example` documents
  them). Never commit real keys.
