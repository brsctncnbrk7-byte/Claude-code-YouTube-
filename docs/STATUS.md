# STATUS — güncel durum

**Son güncelleme:** 2026-10-03 (oturum 1)
**Faz:** 1→2 (araştırma/kararlar yazıldı; üretim hattı MVP başlıyor)
**READY_FOR_VPS:** HAYIR

## Tamamlanan somut çıktılar
- Repo iskeleti: CLAUDE.md, README, LICENSE (MIT), .gitignore, .env.example, scripts/env_check.sh, scripts/secret_scan.sh
- docs/MASTER_PLAN.md (hedef, eşik matematiği, fazlar, yeniden üretilebilirlik tanımı)
- docs/DECISIONS.md ADR-001…011 (ağ, public repo, runner, teslim yolu, dil+TTS, render yolu, ses QC, altyazı, niş, format)
- docs/research: ortam yetenekleri (ölçümlü), araç/lisans tablosu (ayrı satırlar; Piper TR sesleri REJECTED), niş karşılaştırması (7 aday), ChatGPT yardım talebi
- docs/policies: etiket şeması, YPP uygunluk, inauthentic content + üretim kapısı kuralları, sentetik içerik beyanı, production-gate
- docs/operations: github-quota + teslim/tetikleme kararı, licensing-notes
- assets/fonts: Inter variable (OFL 1.1) + lisans metni
- Ölçümler: Kokoro RTF ≈ 0.26; Whisper base.en WER ≤ 0.016; Playwright 16 fps PNG yakalama

## Açık doğrulamalar (unverified / secondary)
| Konu | Durum | Nerede |
|---|---|---|
| YPP 72851 / 12843009 tam metin | chatgpt-verified (ortamdan okunamadı) | policies/ypp-eligibility.md |
| 1311392 inauthentic content tam metin | unverified | HELP_REQUEST #3 |
| 14328491 sentetik beyan tam metin | unverified | HELP_REQUEST #4 |
| Kokoro HF LICENSE/VOICES.md | GitHub kanıtı var; HF dosyası okunamadı | HELP_REQUEST #6 |
| GitHub Actions sınırları | secondary | operations/github-quota.md |
| World Bank / GCP veri atıf şartları | unverified | HELP_REQUEST #9 |

## Açık engeller
- Ağ politikası (kullanıcı kararı: devam). İnsan dinleme testi yapılamaz → ses QC üç katmanlı (ADR-008); raporlar bunu açıkça yazar.

## Commit/push durumu
Bu dosya güncellendiği oturumun sonunda `git log`/`git push` çıktısı HANDOFF'a işlenir.
