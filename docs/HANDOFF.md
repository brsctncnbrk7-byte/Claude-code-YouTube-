# HANDOFF — CLOSED / DISCONTINUED BY USER (2026-10-04)

**Kullanıcı kararı:** Proje, mevcut çıktılar yeterli bulunmadığı için sonlandırıldı. Bu dosya artık "sıradaki iş" listesi değildir; yeni oturumlar iş başlatmaz.

## Kapanış durumu
- Dal: `claude/new-session-dop2fl` (remote'ta `main` yok). Kapanış commit'i: bkz. `git log -1`.
- READY_FOR_VPS güncel durum değildir; `reports/READY_FOR_VPS.md` ve `reports/ACCEPTANCE_REVIEW.md` tarihli arşiv kayıtlarıdır.
- Hiçbir video yayımlanmadı; `content/publish-queue.yaml` → `first_public_publish_utc: null`; 30 günlük sayaç başlatılmadı.
- GitHub Releases (`ep-001`, `ep-002`, `ep-003`, `ep-005`, `ep-006`), raporlar ve repo içeriği silinmedi, korunur.
- Otomasyon kapatıldı: `.github/workflows/release.yml` artık push ile tetiklenmez; hesapta Routine/zamanlayıcı yok; VPS cron hiç kurulmadı.
- Açık doğrulamalar (`unverified` kayıtlar, HELP_REQUEST maddeleri) kapatılmış gibi gösterilmedi; açık kaldılar.

## Yeni bir oturum açılırsa
Yalnızca kullanıcının açık yazılı talimatıyla iş yapılır. Aksi hâlde: yeni render, revizyon, yayın, VPS kurulumu, workflow çalıştırma **yok**.

## Arşiv notları (teknik, yeniden açılırsa)
- Claude ortamında `playwright install` çalıştırma (Chromium 1194 hazır; Python playwright==1.56.0).
- espeak-ng apt ile kurulu olmalı; ytf env değişkenlerini kendisi ayarlar. `/usr/bin/time` için `apt-get install -y time`.
- Modeller: `uv run python scripts/fetch_models.py`; testler: `uv run pytest -q`.
- Ses QC bayrakları: `reports/<ep>/<fmt>/qc.json → audio_eval.asr.flagged`.
