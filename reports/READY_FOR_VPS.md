# READY_FOR_VPS / GITHUB PREPARATION COMPLETE — 2026-10-03

Sekiz bitiş ölçütü (docs/MASTER_PROMPT.md §10) kanıtlarıyla aşağıdadır. VPS geçişi **başlatılmadı**; repo GitHub'da kalır ve geçiş yalnızca kullanıcı talebiyle başlar (CLAUDE.md §5, docs/operations/vps-setup.md "denenmedi" etiketlidir).

| # | Ölçüt | Durum | Kanıt |
|---|---|---|---|
| 1 | Güncel kaynaklı araştırma, seçilmiş niş/dil, marka, 30 günlük plan | ✅ | docs/research/niche-comparison.md (7 aday, puan matrisi); ADR-006 (İngilizce + Kokoro), ADR-010 (Data detective stories), ADR-011; docs/MASTER_PLAN.md (eşik matematiği, 3 senaryo, takvim); channel/brand.md + channel/assets |
| 2 | Seçilen ücretsiz araçların ticari kullanım ve teknik uygunluğu | ✅ (etiketli) | docs/research/tools-and-licenses.md: kod/ağırlık/ses/fonemizer/font/veri ayrı satırlar, kanıt dosyaları; Piper TR sesleri REJECTED; Kokoro ağırlıkları Apache-2.0 (yazarın GitHub README'si; HF LICENSE dosyası bu ortamdan okunamadı → HELP_REQUEST #6) |
| 3 | Gerçek pilot uçtan uca + ikinci farklı konuda aynı hat + Shorts yolu gerçek çıktıyla | ✅ | reports/pilot/ep-001.md (Nightingale, 4.8 dk), ep-002.md (Challenger, 3.0 dk), her ikisi uzun+Short `QC_PASS`; kod değişikliği olmadan ikinci konu |
| 4 | İlk hafta yayın paketleri tam, placeholder yok | ✅ | GitHub Releases `ep-001`, `ep-002`, `ep-003`: her biri 21 varlık (MP4, Short MP4, SRT/VTT, 3 thumbnail, metadata.yaml, sources/licenses, qc-report, manifest.json, UPLOAD_CHECKLIST); content/publish-queue.yaml |
| 5 | Gerçek CPU/RAM/disk, render süresi, dosya boyutu, GitHub kota ölçümü → VPS gereksinimi | ✅ | reports/pilot/render-benchmark.md; reports/quota/actions-ep-00{1,2}.md (runner süreleri 13–19 dk/koşu); docs/operations/vps-setup.md (ölçümlerden türetilmiş, VPS'te test edilmedi) |
| 6 | Temiz klondan tek komutla pilot yeniden üretimi; hata/devam mekanizması | ✅ | reports/pilot/reproducibility.md: Koşu 3 REPRODUCIBLE=true, MP4 sha256 birebir; GitHub runner çıktıları da yerel derlemelerle bit-düzeyinde aynı; checkpoint/retry: src/ytf/jobs.py, tests/test_jobs.py, docs/operations/recovery.md |
| 7 | Büyük çıktılar erişilebilir, ücretsiz, kalıcı teslim; repo içinde manifest + checksum | ✅ | Releases (kalıcı, ücretsiz); her paket `manifest.json` sha256; indirme + checksum doğrulamaları: reports/quota/actions-ep-001.md, actions-ep-002.md (ep-003: 22:21 UTC, sha256 eşleşti) |
| 8 | Kanal açma/yükleme paketleri, hesap sahibi zorunlulukları, analytics sınırları, ücretsiz çalışma sınırları, VPS geçiş rehberi | ✅ | channel/SETUP_CHECKLIST.md (HESAP SAHİBİ adımları işaretli), dist/*/UPLOAD_CHECKLIST.md, docs/operations/{publishing,measurement,github-quota,session-continuity,recovery,vps-setup}.md |

## Açıkça kalan sınırlar (hazırlığı engellemez, raporlanır)
- Resmî YouTube/Google politika sayfaları bu ortamdan okunamadı: YPP eşikleri `chatgpt-verified`, diğer politikalar `unverified`/`secondary` (docs/policies/README.md). Ağ izni açılırsa yeniden doğrulama ilk iştir.
- Ses kalitesi insan dinlemesiyle değil fonem + ASR round-trip + spektrogram ile değerlendirildi; her QC raporu bunu beyan eder.
- Bölüm süreleri 2.6–4.8 dk (ADR-013); 6–9 dk hedefi 7. gün verisinden sonra ek veri sahneleriyle.
- 30 günde YPP kabulü istatistiksel olarak düşük olasılıklı bir hedeftir (MASTER_PLAN §2); kabul süresi YouTube'un kontrolündedir.
- VPS rehberi test edilmemiştir; geçiş kullanıcı talebiyle başlar.

## Kullanıcıdan beklenen tek şey
Kanal açma (channel/SETUP_CHECKLIST.md) ve yükleme (docs/operations/publishing.md §B). Yayın tarihi `content/publish-queue.yaml → first_public_publish_utc` alanına yazıldığında 30 gün sayacı başlar.
