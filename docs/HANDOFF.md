# HANDOFF — sonraki oturum için

**Dal:** `claude/new-session-dop2fl` (remote'ta `main` yok). Son commit: bkz. `git log -1`.

## Sıradaki iş (öncelik sırasıyla)
1. `reports/pilot/reproducibility-run.log` sonucunu `reports/pilot/reproducibility.md`'ye işle (REPRODUCIBLE true/false, toleranslar).
2. Actions run 37151370173 (ep-001 release) sonucunu doğrula: release `ep-001` varlıkları indir, `manifest.json` sha256 karşılaştır → `reports/quota/actions-ep-001.md`; süre/boyut kaydet.
3. ep-003 (Snow) üret: `uv run ytf all ep-003 && uv run ytf all ep-003 --format short`; kare/ses incelemesi → gate alanları → QC_PASS → `release-requests/ep-003.request`.
4. ep-001/ep-002 üretim sürümleri: süreyi 6 dk'ya çıkaran ek sahneler (ep-001: Scutari koşulları, Farr yöntemi; ep-002: O-ring mekanizması şeması, Boisjoly 1985 notu) — kaynaklı.
5. ep-004–006 senaryoları (Wald, Minard, Literary Digest) → ikinci hafta tamponu.
6. READY_FOR_VPS raporu: 8 ölçüt kanıt bağlantılarıyla (`reports/READY_FOR_VPS.md`); 4/6/7 kapanınca.

## Oturum başlangıcı
`cat docs/STATUS.md docs/HANDOFF.md content/queue.yaml; bash scripts/env_check.sh; git status; git log -5`
Modeller yoksa: `uv run python scripts/fetch_models.py`. Testler: `uv run pytest -q`.

## Notlar
- Claude ortamında `playwright install` çalıştırma (Chromium 1194 hazır; Python playwright==1.56.0).
- espeak-ng apt ile kurulu olmalı (`apt-get install -y espeak-ng`); ytf env değişkenlerini kendisi ayarlar.
- `/usr/bin/time` için `apt-get install -y time`.
- Render önbelleği `build/<ep>/<fmt>/ck`; scenes.js değişince tüm sahneler yeniden render edilir (kod hash'i).
- Ses QC bayrakları: `reports/<ep>/<fmt>/qc.json → audio_eval.asr.flagged`; kabul edilenler `gate.notes`'a yazılır.
