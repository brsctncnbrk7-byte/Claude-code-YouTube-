# Release requests

Tag pushes from the Claude Code environment are refused by its git proxy (only the working branch may be pushed), and `workflow_dispatch`
needs the workflow on the default branch (`main` does not exist yet). So a release is requested by **committing a small file here**:

```
echo "episode: ep-001" > release-requests/ep-001.request      # optional second line: "format: both"
git add release-requests/ep-001.request && git commit -m "release: ep-001" && git push
```
`.github/workflows/release.yml` runs on that push, builds the episode on a free standard runner, uploads a 90-day artifact and creates
the GitHub Release `ep-001` (tag created by `gh release create` with GITHUB_TOKEN inside the same run — no extra token, no second workflow).
Re-requesting the same episode re-uploads assets with `--clobber`. A push that only changes the workflow file runs the 3-second smoke test
and publishes release `smoke-<run_id>` so the full chain (workflow → release → download → sha256) can be verified cheaply.
