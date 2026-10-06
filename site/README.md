# Public sales dashboard snapshot

`index.html` is the static, public GitHub Pages artifact. It intentionally contains only fields required to render the lead dashboard; local review notes and the private business profile are not included.

Refresh the snapshot from the local lead agent by regenerating `mobile-app-sales-agent/dashboard.html`, copying it here as `site/index.html`, then committing the approved update. GitHub Actions publishes `site/` when changes reach `main` after Pages is configured to use GitHub Actions.
