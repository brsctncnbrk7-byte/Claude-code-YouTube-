# HANDOFF — sonraki oturum için

**Dal:** `claude/new-session-dop2fl` (remote'ta `main` yok). Son commit: bkz. `git log -1`.

## Sıradaki iş (öncelik sırasıyla)
1. Release doğrulamaları: `ep-003` ve yeniden yayımlanan `ep-001`/`ep-002` varlıklarını indir, manifest sha256 karşılaştır → `reports/quota/`; sonra `reports/READY_FOR_VPS.md`'yi kesinleştir.
2. ep-005 (Minard) build sonucu: `reports/pilot/ep-005-build.log`; kare/ses incelemesi → gate → release isteği. ep-006 (Literary Digest) aynı yol.
3. ep-004 (Wald) ve ep-007–013 senaryoları → 30 günlük kuyruk tamponu (her biri kaynaklı; `content/queue.yaml`).
4. Üretim sürümleri (ADR-013): 7. gün verisinden sonra ep-001/002/003 için ek veri sahneleri.
5. Kullanıcı yüklemeye başlayınca `content/publish-queue.yaml` → `first_public_publish_utc` doldurulur; gün 3/7/14/21/30 raporları.

## Oturum başlangıcı
`cat docs/STATUS.md docs/HANDOFF.md content/queue.yaml; bash scripts/env_check.sh; git status; git log -5`
Modeller yoksa: `uv run python scripts/fetch_models.py`. Testler: `uv run pytest -q`.

## Notlar
- Claude ortamında `playwright install` çalıştırma (Chromium 1194 hazır; Python playwright==1.56.0).
- espeak-ng apt ile kurulu olmalı (`apt-get install -y espeak-ng`); ytf env değişkenlerini kendisi ayarlar.
- `/usr/bin/time` için `apt-get install -y time`.
- Render önbelleği `build/<ep>/<fmt>/ck`; scenes.js değişince tüm sahneler yeniden render edilir (kod hash'i).
- Ses QC bayrakları: `reports/<ep>/<fmt>/qc.json → audio_eval.asr.flagged`; kabul edilenler `gate.notes`'a yazılır.
