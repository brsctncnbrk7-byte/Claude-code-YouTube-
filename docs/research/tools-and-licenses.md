# Araç ve lisans doğrulaması (ayrı ayrı) — 2026-10-03

Kural: kod, model ağırlığı, ses modeli/veri seti, fonemizer, font, veri seti **ayrı satır**. Bir reponun lisansı indirme paketine genellenmez. Durumlar: `verified-primary` (lisans dosyası bu ortamdan okundu), `secondary`, `unverified`, `REJECTED`.

## Kullanılan (üretim hattı)
| Bileşen | Sürüm | Rol | Lisans | Kanıt | Durum |
|---|---|---|---|---|---|
| FFmpeg (Ubuntu paketi) | 6.1.1 | kurgu/encode | LGPL/GPL (araç; çıktıya kısıt yok) | `ffmpeg -version` | verified-primary |
| Python | 3.11.15 | runtime | PSF | sistem | verified-primary |
| Playwright (Python) | 1.56.0 | HTML→kare yakalama | Apache-2.0 | PyPI metadata | verified-primary |
| Chromium (Playwright build 1194) | — | render motoru | BSD-3 + bileşen lisansları | Playwright dağıtımı | secondary |
| kokoro-onnx | 0.6.1 | TTS çalıştırıcı | MIT | raw.githubusercontent.com/thewh1teagle/kokoro-onnx/main/LICENSE | verified-primary |
| **Kokoro-82M model ağırlığı** (`kokoro-v1.0.onnx`) | v1.0 | TTS modeli | Apache-2.0 | hexgrad/kokoro README ("Apache-licensed weights", GitHub); HF model kartı ön-matter `license: apache-2.0` (GitHub aynası zboyles/Kokoro-82M README) | verified-primary (GitHub) / HF LICENSE dosyası okunamadı → ChatGPT talebinde |
| **Kokoro ses paketleri** (`voices-v1.0.bin`) | v1.0 | ses stilleri | Apache-2.0 (aynı HF reposunun parçası; kokoro-onnx release'inde yeniden paketlenmiş) | kokoro-onnx README "License: kokoro model: Apache 2.0" | secondary — HF VOICES.md okunamadı; ChatGPT talebinde |
| Kokoro eğitim verisi beyanı | — | — | Yazar beyanı: "permissive/non-copyrighted audio" + kapalı TTS'lerden sentetik ses | model kartı (GitHub aynası) | bilgi notu; lisansı etkilemez |
| onnxruntime | 1.30.0 | inference | MIT | PyPI | verified-primary |
| phonemizer | 3.4.0 | G2P (kokoro-onnx bağımlılığı) | **GPL-3.0** | PyPI | verified-primary — kütüphane olarak süreç içinde; çıktıya etkisi yok; repo kodumuz MIT dağıtılır, kullanıcı birleştirir (not: `docs/operations/licensing-notes.md`) |
| espeak-ng (apt) + libespeak-ng | 1.51 | fonemleştirici arka uç | GPL-3.0 | Ubuntu paketi | verified-primary — aynı not |
| espeakng-loader | 0.2.4 | lib yükleyici | MIT | PyPI | verified-primary |
| sherpa-onnx + sherpa-onnx-core (pip) | 1.13.8 | ASR çalıştırıcı (QC); `-core` ikili kütüphaneleri taşır (libonnxruntime, c-api) | Apache-2.0 | raw.githubusercontent.com/k2-fsa/sherpa-onnx/master/LICENSE | verified-primary |
| **Whisper base.en ağırlıkları** (sherpa-onnx dönüştürme) | — | ASR (QC, yayınlanmaz) | MIT (OpenAI) | raw.githubusercontent.com/openai/whisper/main/LICENSE | verified-primary (orijinal); dönüştürülmüş dosya sherpa release'inden (`asr-models`) |
| **DNSMOS P.835** (`sig_bak_ovr.onnx`, Microsoft DNS-Challenge) | repo master | ses kalitesi tahmini (yalnızca QC; çıktıya girmez) | **CC BY 4.0** (repo LICENSE, raw.githubusercontent.com/microsoft/DNS-Challenge/master/LICENSE) — atıf: Reddy et al., DNSMOS P.835 (ICASSP 2022) | sha256 269fbebdb513aa23…; `models/dnsmos/LICENSE` | verified-primary |
| Whisper small.en (sherpa-onnx dönüştürme) | — | ikinci ASR görüşü (QC) | MIT (OpenAI) | sherpa `asr-models` release | verified-primary (isteğe bağlı; runner'da kullanılmaz) |
| soundfile / numpy / Pillow / pydantic / PyYAML / pytest | sabit (`uv.lock`) | yardımcı | BSD/MIT/HPND | PyPI | verified-primary |
| Fontlar: DejaVu Sans | sistem | tipografi | Bitstream Vera/DejaVu lisansı (özgür, gömme serbest) | sistem paketi | verified-primary |
| Fontlar: Inter (Google Fonts repo) | github.com/google/fonts/ofl/inter | tipografi | SIL OFL 1.1 | raw.githubusercontent.com/google/fonts/main/ofl/inter/OFL.txt (HTTP 200) | verified-primary (indirilecek, sha256 kaydı `content/licenses/fonts.md`) |

## Veri kaynakları (bölüm bazında ayrıca doğrulanır)
| Kaynak | Lisans | Kanıt | Not |
|---|---|---|---|
| `datasets/population` (Frictionless) | ODC-PDDL-1.0; kaynak World Bank | datapackage.json | World Bank'in kendi CC BY 4.0 koşulu **ayrı** kontrol edilir (unverified — worldbank.org engelli olabilir) |
| `datasets/co2-fossil-global` | ODC-PDDL-1.0; kaynak Global Carbon Project 2025v15 | datapackage.json | GCP'nin kendi CC BY 4.0 atıf şartı ayrı kontrol |
| Natural Earth (`nvkelso/natural-earth-vector`) | Kamu malı | LICENSE.md (HTTP 200) | harita geometrisi |
| OWID (`owid/owid-datasets`) | repo **arşivlenmiş**; LICENSE dosyası yok (404) | README | **Kullanılmaz**; OWID verisi gerekiyorsa veri seti bazında kaynak lisansı doğrulanmadan kullanılmaz |
| Rdatasets (vincentarelbundock) | paket bazında değişir | datasets.csv (HTTP 200) | klasik veri setleri (ör. Snow 1854, Nightingale) **yalnızca** orijinal kaynağı kamu malı/CC olanlar; her biri ayrı kayıt |
| Tarihî birincil veriler (19. yy yayınları) | kamu malı (telif süresi dolmuş) | yayın yılı + kaynak | sayılar yeniden çizilir; orijinal görseller taranmış kopya olarak kullanılmaz (tarayan kurumun koşulları belirsiz) |

## Değerlendirildi ve REDDEDİLDİ
| Bileşen | Neden |
|---|---|
| Piper `tr_TR-dfki-medium` | Veri seti CC BY-NC-SA 4.0 → ticari kullanım yok (MODEL_CARD, sherpa release tarball'ından okundu) |
| Piper `tr_TR-fahrettin-medium`, `tr_TR-fettah-medium` | Veri seti CC0 (NabuCasa) **ama** `en_US-lessac` tabanından fine-tune; lessac = Blizzard 2013 "research purposes" lisansı; türev ağırlıkların ticari durumu topluluk tartışmalı (rhasspy/piper #271, OHF-Voice/piper1-gpl #314, k2-fsa/sherpa-onnx #3947 — `secondary`) → **belirsiz = kullanılmaz** |
| Piper İngilizce `lessac`, `ryan`, `joe` vb. | lessac tabanı / NC veri setleri → belirsiz |
| Coqui XTTS v2 | CPML lisansı (ticari yok) |
| Remotion | şirket lisansı koşulları; gereksiz |
| Hugging Face'ten doğrudan model indirme | ağ engeli; yalnızca GitHub release aynaları (k2-fsa/sherpa-onnx, thewh1teagle/kokoro-onnx) |
| Stok görsel/müzik servisleri | yeni hesap/lisans belirsizliği + ağ engeli; gerekmiyor (programatik görsel, müzik yok veya programatik) |

## Model dosyaları (sha256, GitHub release kaynakları)
| Dosya | URL | sha256 |
|---|---|---|
| kokoro-v1.0.onnx (325.5 MB) | github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/kokoro-v1.0.onnx | beb0d1848dee9a49da392cc3df26958d46cfa35d321edf434f52949153f0df3a |
| voices-v1.0.bin (28.2 MB) | github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/voices-v1.0.bin | bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d |
| sherpa-onnx-whisper-base.en.tar.bz2 (208.6 MB) | github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.en.tar.bz2 | (scripts/fetch_models.py kaydeder) |
