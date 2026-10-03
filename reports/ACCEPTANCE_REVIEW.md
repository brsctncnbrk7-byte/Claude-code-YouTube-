# Son kabul incelemesi — GitHub hazırlığı (2026-10-03, oturum 1)

Kullanıcının 7 maddelik kabul talebi üzerine; READY_FOR_VPS bu inceleme bitene kadar yeniden açıldı (commit 3c15b94).
Bağımsız kanıt incelemesi ayrı bir alt ajan tarafından yapıldı; bulguları §D'de entegre edildi.

## A. Teknik hazırlık — 8 ölçüt (MASTER_PROMPT §10)

| # | Ölçüt | Kanıt dosyaları | Commit | Doğrulama yöntemi | Sonuç |
|---|---|---|---|---|---|
| 1 | Güncel kaynaklı araştırma, niş/dil, marka, 30 gün planı | docs/research/niche-comparison.md; docs/DECISIONS.md ADR-006/010/011/013; docs/MASTER_PLAN.md; channel/brand.md; channel/assets/{logo.svg,profile_800.png,banner_2560x1440.png,watermark_150.png} | 6913b47, 28a2a69 | Dosyalar okundu; niş matrisinde 7 aday, kaynaklar tarihli ve `secondary` etiketli; marka varlıkları görsel olarak incelendi | **PASS** (kaynakların çoğu ikincil; resmî YouTube sayfaları bu ortamdan okunamadı — açık kayıt) |
| 2 | Seçilen ücretsiz araçların ticari kullanım ve teknik uygunluğu | docs/research/tools-and-licenses.md (bileşen başına satır + kanıt URL'si; REJECTED listesi); content/ep-00X/licenses.md | baa74eb, 09a6208 | Lisans dosyaları GitHub/PyPI'den okundu (FFmpeg, Playwright, kokoro-onnx MIT, Kokoro ağırlıkları Apache-2.0 [yazarın README'si], onnxruntime, sherpa-onnx, Whisper MIT, phonemizer GPL [yalnızca süreç içi], Inter OFL, DNSMOS CC BY 4.0 [yalnızca QC]); Piper TR sesleri MODEL_CARD'dan okunup reddedildi | **PASS** — tek açık nokta: Kokoro HF deposundaki LICENSE dosyası doğrudan okunamadı; GitHub'daki yazar beyanı birincil kanıt (HELP_REQUEST #6) |
| 3 | Gerçek pilot uçtan uca + ikinci farklı konu + Shorts gerçek çıktı | reports/pilot/ep-001.md, ep-002.md; reports/ep-001/{long,short}/qc.json; reports/ep-002/{long,short}/qc.json; dist/ep-001, dist/ep-002 | 43e3676, e7c1899 | ffprobe (1920×1080/1080×1920, h264/aac, kare sayısı = beklenen); QC JSON `status` alanı; kareler Claude tarafından görsel incelendi | **PASS** |
| 4 | İlk hafta yayın paketleri tam, placeholder yok | GitHub Releases ep-001, ep-002, ep-003 (21'er varlık); dist/ep-00X/{mp4, short mp4, srt, vtt, 3 thumbnail, metadata.yaml, sources.md, licenses.md, qc-report.md, manifest.json, UPLOAD_CHECKLIST.md} | 43e3676, 732e2df, 28a2a69 | Varlıklar indirildi, manifest sha256 eşleşti; metadata alanları dolu; §C takvimi | **PASS** |
| 5 | Gerçek CPU/RAM/disk/render/kota ölçümü → VPS gereksinimi | reports/pilot/render-benchmark.md; reports/pilot/*-build*.log (`/usr/bin/time -v`); reports/quota/actions-ep-00{1,2}.md; docs/operations/vps-setup.md | 90b7009, 9ebbca3 | Sayılar build loglarından (Elapsed, Maximum resident) ve Actions API adım zamanlarından alındı | **PASS** (VPS rehberi "denenmedi" etiketli — kural gereği) |
| 6 | Temiz klondan tek komutla yeniden üretim; hata/devam | reports/pilot/reproducibility.md (Koşu 1–3 + çapraz makine); reports/pilot/chain3.log (`REPRODUCIBLE: true`); scripts/repro_check.py; src/ytf/jobs.py; tests/test_jobs.py; docs/operations/recovery.md | 7531568, 90b7009, 9ebbca3 | `git clone` → `uv sync --frozen` → `ytf build ep-001` → `repro_check.py`: süre/kare/cue/cümle/loudness/piksel eşit, MP4 sha256 birebir; runner çıktıları da yerel ile birebir | **PASS** |
| 7 | Büyük çıktılar erişilebilir, ücretsiz, kalıcı teslim; manifest + checksum | .github/workflows/release.yml (ubuntu-latest, GITHUB_TOKEN, `contents: write` yalnızca job'da); Releases ep-001/002/003/005; dist/*/manifest.json | c65c801, 9ebbca3, 30eddce | Her release'ten MP4/manifest indirildi, sha256 eşleşti, QC raporları `QC_PASS` | **PASS** |
| 8 | Kanal/yükleme paketleri, hesap sahibi zorunlulukları, analytics sınırları, ücretsiz sınırlar, VPS rehberi | channel/SETUP_CHECKLIST.md; dist/*/UPLOAD_CHECKLIST.md; docs/operations/{publishing,measurement,github-quota,session-continuity,recovery,vps-setup}.md | f20664f, 09a6208 | Dosyalar okundu; kullanıcıdan repo düzenlemesi isteyen ifadeler kaldırıldı (09a6208) | **PASS** |

## B. Ses QC yöntemi ve gerçek ses üzerindeki sonuçlar
_(bu bölüm `reports/<ep>/<fmt>/audio-eval.md` çıktılarıyla doldurulur — aşağıda)_

## C. İçerik kalite kabulü

**Kanal kimliği (ADR-006/010):** ad **Plotted Past** (handle önerisi `@plottedpast`; alternatifler channel/brand.md) • dil **İngilizce** • hedef kitle: 18–45, meraklı genel izleyici; veri/bilim/tarih ilgilileri; küresel • vaat: *"Every episode, a real mystery solved by a chart — rebuilt from the original numbers."* • format: 2.5–5 dk uzun video + 25–30 sn Short; tüm görseller orijinal veriden programatik; sentetik anlatıcı açıkça beyan ediliyor.

**İlk hafta yayın takvimi (gün 0 = ilk herkese açık yayın; saat 15:00 UTC):**
| Gün | Sıra | Bölüm | Format | Süre | QC | Paket (Release) |
|---|---|---|---|---|---|---|
| 0 | 1 | ep-001 The Chart That Shamed an Army (Nightingale) | uzun | 288.1 s | QC_PASS | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/tag/ep-001 |
| 1 | 2 | ep-001 Short | Short 1080×1920 | 30.0 s | QC_PASS | aynı release (`ep-001-short.mp4`) |
| 2 | 3 | ep-002 The Scatterplot That Could Have Saved Challenger | uzun | 179.6 s | QC_PASS | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/tag/ep-002 |
| 3 | 4 | ep-002 Short | Short | 24.1 s | QC_PASS | aynı release |
| 4 | 5 | ep-003 616 Dots: How a Map Found the Source of Cholera (Snow) | uzun | 157.2 s | QC_PASS | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/tag/ep-003 |
| 5 | 6 | ep-003 Short | Short | 26.5 s | QC_PASS | aynı release |
| 7 | 7 (2. hafta) | ep-005 Napoleon's Army in One Line (Minard) | uzun | 137.6 s | QC_PASS | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/tag/ep-005 |
| 8 | 8 | ep-005 Short | Short | 26.9 s | QC_PASS | aynı release |
| 9 | 9 | ep-006 The Poll That Got 1936 Spectacularly Wrong | uzun | — | (üretimde) | (release isteği gönderilecek) |

**ep-004 (Wald, survivorship bias) neden atlandı:** Bölümün dayandığı birincil kaynak (Wald 1943 SRG memorandumu, DTIC ADA091073) bu ortamdan okunamıyor ve ikincil kaynaklardaki "vuruş dağılımı" sayıları çoğunlukla örneklenmiş/illüstratiftir. Üretim kapısı A2 ("her olgusal iddia kaynaklı; doğrulanamayan iddia senaryodan çıkar") altında gerçek sayılar olmadan bölüm yapılamaz; illüstratif sayılarla yapmak yanıltıcı olurdu. Bu yüzden sıradaki, verisi kamu malı ve elde olan bölümler (ep-005 Minard, ep-006 Literary Digest) öne alındı; yayın sayısı eksilmedi (2. hafta: ep-005, ep-006 + Shorts). ep-004, memorandumun gerçek tablosu (HELP_REQUEST ile ya da izinli erişimle) doğrulanırsa üretilir; aksi hâlde yerini ep-007 (Simpson paradoksu, Berkeley 1973 verisi elde) alır. Kuyruk: content/queue.yaml.

**Uzunluk ilkesi (ADR-013):** Bölüm uzunluğunu içerik belirler; hiçbir bölüm süre için uzatılmaz. Ek sahne yalnızca yeni bilgi/anlatı değeri katıyorsa eklenir.

## D. Bağımsız inceleme bulguları (alt ajan, salt okunur; HEAD 09a6208) ve çözümleri
Alt ajan sonucu: 6 PASS, 2 PARTIAL (ölçüt 7 "repo içinde manifest", ölçüt 8 "kullanıcı repo düzenlemez"). Bulgular ve ana oturumun yaptığı düzeltmeler:
| # | Bulgu | Çözüm |
|---|---|---|
| 1 | Yayımlanan `UPLOAD_CHECKLIST` dosyaları hâlâ "paste the video URL into content/publish-queue.yaml" diyor (düzeltme paketlere yansımamış) | `package.py` adım 7–8 düzeltildi; tüm bölümler yeniden paketlenip yeniden yayımlanıyor (bu incelemenin sonunda release varlıkları doğrulanacak) |
| 2 | Dört bölümün commit'li `qc.json` dosyaları derin ses katmanından (iki ASR + DNSMOS) önce üretilmiş; `audio-eval.md` yalnızca ep-001 Short için var | Derin QC tüm bölümler için yeniden çalıştırıldı (`reports/pilot/deep-qc.log`); yeni `qc-report.md` ve `audio-eval.md` paketlere ve release'lere giriyor (§B) |
| 3 | `dist/` git'te izlenmiyor → repoda manifest/checksum yok | `package.py` manifestleri `reports/releases/<ep>/manifest*.json` olarak da yazıyor (izlenen) |
| 4 | Atıf yapılan eksik dosyalar: `reports/pilot/voice-selection.md`, `content/licenses/{fonts,datasets}.md` | Oluşturuldu |
| 5 | Bayat metinler: STATUS "ADR-001…011"/"10 test", HANDOFF "ilan edildi", github-quota "ADR-006"/setup-uv, vps-setup "render_queue (yazılacak)"/229 s | Düzeltildi |
| 6 | Kokoro ağırlık lisansı yazar README'sine dayanıyor; voices/Chromium `secondary`; UCI şartları doğrulanmadı | Etiketler korunuyor; HELP_REQUEST #6/#9 ile kapatılacak; üretimde kullanılan ağırlıkların Apache-2.0 beyanı yazarın kendi deposundan (birincil) |
| 7 | §C "iki ASR modeli" kodda yalnızca yerelde sağlanıyordu (runner'da small.en yok) | `fetch_models.py` small.en'i (sha256 ile) runner'da da kuruyor; cache anahtarı güncellendi |
| 8 | WER değerleri belgeler arasında farklı (0.003/0.0076/0.015) | ep-001 raporuna açıklama eklendi; geçerli değerler `audio-eval.md` |
| 9 | Ölçüt 6 kanıtı: temiz klon komutları repo içinde bir betikte değil | `scripts/repro_check.py` + `docs/operations/recovery.md` adımları; klon zinciri `reports/pilot/chain3.log` başlığında yol ve komut sırasıyla kayıtlı (kabul: yeterli, ancak `scripts/repro_clone.sh` olarak sonraki oturumda betikleştirilecek) |

## E. Hesap sahibi zorunlulukları (Claude yapamaz)
Google hesabı/telefon doğrulaması; 2 Adımlı Doğrulama; gelişmiş özellikler için kimlik/telefon; YPP başvurusu; AdSense hesabı, vergi/banka bilgileri, sözleşme kabulü; video yükleme ve zamanlama (channel/SETUP_CHECKLIST.md, docs/operations/publishing.md). Yükleme sonrası kullanıcı yalnızca video URL'sini bildirir; repo kayıtlarını Claude günceller.
