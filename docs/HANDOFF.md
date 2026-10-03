# HANDOFF — sonraki oturum için

**Dal:** `claude/new-session-dop2fl` (remote'ta `main` yok; ilk push bu daldan)

## Sıradaki iş (öncelik sırasıyla)
1. `src/ytf` MVP: tts → subtitles → render (Playwright) → assemble → qc → package; `tests/`; `scripts/fetch_models.py`.
2. Pilot #1 `ep-001` (Nightingale gül diyagramı) uçtan uca; `reports/pilot/ep-001.md` teknik + içerik ayrı.
3. Pilot #2 `ep-002` (Challenger O-ring verisi) + `--format short`; `reports/pilot/render-benchmark.md`, `reproducibility.md`.
4. `.github/workflows/release.yml` küçük test çıktısıyla zincir doğrulaması (workflow → release → indirme → sha256).
5. İlk hafta paketleri (yalnızca pilotlar başarılıysa), kanal kiti, operasyon rehberleri, READY_FOR_VPS raporu.

## Oturum başlangıcı
`cat docs/STATUS.md docs/HANDOFF.md content/queue.yaml; bash scripts/env_check.sh; git status; git log -5`

## Notlar
- Modeller `models/` altında (gitignored). Yoksa `uv run python scripts/fetch_models.py`.
- Claude ortamında `playwright install` çalıştırma; `PLAYWRIGHT_BROWSERS_PATH` hazır (Chromium 1194, Python playwright==1.56.0).
- espeak-ng apt ile kurulu olmalı; `PHONEMIZER_ESPEAK_LIBRARY=/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1` ve `ESPEAK_DATA_PATH=/usr/lib/x86_64-linux-gnu/espeak-ng-data` (ytf bunları otomatik ayarlar).
