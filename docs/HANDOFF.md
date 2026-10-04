# HANDOFF — sonraki oturum için

**Dal:** `claude/new-session-dop2fl` (remote'ta `main` yok). Son commit: bkz. `git log -1`.

## Sıradaki iş (öncelik sırasıyla)
0. **Kullanıcı incelemesi bekleniyor (2026-10-04):** ep-001 ve ep-002 örnekleri telefondan izlenmek üzere doğrudan asset linkleriyle iletildi (release varlıkları indirildi, HTTP 200, sha256 = manifest; kayıt: `reports/releases/sample-links-2026-10-04.md`). İçerik kabulü ve ilk yayın tarihi **kullanıcı adına kaydedilmez**. Kullanıcı `docs/research/chatgpt-answers-2026-10-04.md` dosyasını iletince: her yanıtı `docs/STATUS.md` "Açık doğrulamalar" tablosuna ve ilgili `docs/policies/*` / `docs/research/tools-and-licenses.md` kaydına madde madde işle; yalnızca birebir alıntı + tarih gelen maddeler `chatgpt-verified` olur, diğerleri `unverified` kalır. VPS'e geçiş yok.
1. READY_FOR_VPS kabul incelemesi: reports/ACCEPTANCE_REVIEW.md; VPS geçişi **yalnızca kullanıcı talebiyle** — docs/operations/vps-setup.md'den başla, mevcut projelere dokunma.
2. (Tamamlandı) ep-005 ve ep-006 yayımlandı. Sıradaki: ep-004 Wald için gerçek SRG memorandum tablosu (HELP_REQUEST) ya da ep-007 Simpson (UCBAdmissions verisi) senaryosu.
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
