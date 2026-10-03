# STATUS — güncel durum

**Son güncelleme:** 2026-10-03 (oturum 1, sonlara doğru)
**Faz:** 4→6 (ilk hafta paketleri tamam; son release doğrulamaları sürüyor)
**READY_FOR_VPS:** HAYIR (ölçüt tablosu aşağıda)

## Tamamlanan somut çıktılar
- Repo iskeleti, CLAUDE.md, MIT lisans, sır taraması, ortam raporu betiği
- docs: MASTER_PLAN, DECISIONS (ADR-001…011 + 004a), politika kayıtları (etiketli), araştırma (ortam, araç/lisans, niş), operasyon (yayın, ölçüm, kurtarma, süreklilik, GitHub kota, VPS taslağı)
- `src/ytf` üretim hattı: Kokoro TTS → zaman çizelgesi → SRT/VTT → HTML/SVG sahneler (Playwright) → FFmpeg → loudnorm+limiter → QC (teknik + 3 katmanlı ses) → paket (manifest sha256) — 10 test geçiyor
- **Pilot #1 ep-001 (Nightingale): QC_PASS uzun (4.8 dk) + Short** — `dist/ep-001/`
- **Pilot #2 ep-002 (Challenger): QC_PASS uzun (3.0 dk) + Short** — `dist/ep-002/`; aynı hat, farklı veri/sahne türleri, kod değişikliği gerekmedi
- **ep-003 (Snow): QC_PASS uzun (2.6 dk) + Short** — `dist/ep-003/`; yeni `dots` sahnesi; tarihsiz satır filtresi
- **Yeniden üretilebilirlik: PASS** — temiz klonda bit-düzeyinde aynı MP4 (ADR-012 tohumlu TTS + sabitlenmiş espeak; `reports/pilot/reproducibility.md`)
- **GitHub Releases:** `ep-001`, `ep-002` yayımlandı ve sha256 doğrulandı; sabitlenmiş hatla yeniden yayım ve `ep-003` koşuları sürüyor
- İkinci hafta tamponu: ep-005 (Minard, `flow` sahnesi) ve ep-006 (Literary Digest) senaryo+veri hazır (`scripted`)
- Kanal kiti: marka, logo/banner/profil/watermark PNG, kurulum listesi, playlist yapısı
- Actions: smoke zinciri doğrulandı (workflow → release `smoke-37149042055` → indirme → sha256 OK); ep-001 gerçek release koşusu başlatıldı (run 37151370173)
- Raporlar: `reports/pilot/ep-001.md`, `ep-002.md`, `render-benchmark.md`

## READY_FOR_VPS ölçütleri (docs/MASTER_PROMPT.md §10)
| # | Ölçüt | Durum |
|---|---|---|
| 1 | Araştırma, niş/dil, marka, 30 gün planı | ✅ (politikalar `chatgpt-verified`/`secondary` etiketli) |
| 2 | Ücretsiz araçların lisans/teknik uygunluğu | ✅ ayrı satırlar; Piper TR REJECTED; Kokoro HF LICENSE dosyası okunamadı (GitHub kanıtı var) |
| 3 | İki pilot + Shorts yolu gerçek çıktıyla | ✅ ep-001, ep-002 uzun+Short QC_PASS |
| 4 | İlk hafta paketleri (placeholder yok) | ✅ ep-001/002/003 uzun + 3 Short paketli (ep-003 release doğrulaması bekleniyor) |
| 5 | Gerçek CPU/RAM/disk/render/kota ölçümü | ✅ render-benchmark.md; Actions ep-001 koşusu ölçülüyor |
| 6 | Temiz klondan tek komutla yeniden üretim + hata/devam | ✅ Koşu 3: REPRODUCIBLE true, MP4 sha256 birebir |
| 7 | Büyük çıktılar erişilebilir/kalıcı teslim + manifest | ✅ Releases `ep-001`, `ep-002` (21 varlık, sha256 eşleşti) |
| 8 | Kanal/yükleme paketleri, hesap sahibi zorunlulukları, analytics sınırı, VPS rehberi | ✅ (VPS rehberi "denenmedi" etiketli) |

## Açık doğrulamalar (unverified / secondary)
| Konu | Durum | Nerede |
|---|---|---|
| YPP 72851 / 12843009 tam metin | chatgpt-verified | policies/ypp-eligibility.md |
| 1311392, 14328491, 6162278 tam metin | unverified | HELP_REQUEST #3–5 |
| Kokoro HF LICENSE/VOICES.md | GitHub kanıtı var; HF dosyası okunamadı | HELP_REQUEST #6 |
| GitHub Actions/Release sınırları | secondary | operations/github-quota.md |
| World Bank/GCP/UCI veri şartları | unverified (bu bölümlerde kullanılmıyor; UCI yalnızca ep-002'nin ikincil kaynağı) | HELP_REQUEST #9 |

## Açık engeller
- **İnsan dinleme testi yapılamıyor**: ses QC fonem + ASR + spektrogram ile; tonlama/doğallık ölçülemiyor (raporlarda beyan). Çözüm yolu: yok (ortam); kullanıcıya devredilmez.
- Resmî Google/YouTube sayfaları bu ortamdan okunamıyor (kullanıcı kararı: devam).
- Tag push proxy tarafından reddediliyor → release-request dosyası (ADR-004a).
- Bölüm süreleri 2.6–4.8 dk: lansman formatı 3–6 dk olarak kararlaştırıldı (ADR-013); 6–9 dk hedefi 7. gün verisinden sonra.
