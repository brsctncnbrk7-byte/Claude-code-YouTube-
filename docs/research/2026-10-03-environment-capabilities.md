# Ortam yetenekleri — 2026-10-03 (ölçülmüş)

Kaynak: bu Claude Code bulut oturumunda çalıştırılan komutlar (`nproc`, `free`, `df`, `ffmpeg -encoders/-filters`, `curl` HEAD/GET probları, proxy `/__agentproxy/status`). Tekrarlamak için: `bash scripts/env_check.sh`.

## Donanım / OS
| Kalem | Değer |
|---|---|
| CPU | 4 vCPU |
| RAM | 15 GiB (swap yok) |
| Disk | ~30 GB yazılabilir alan (oturum başı sabit; `df` "Avail" yanıltıcı olabilir) |
| OS | Ubuntu 24.04.4 LTS, kernel 6.18 |
| Python | 3.11.15 (+ `uv`) |
| Node | 22.22.0 (npm 10.9), global `playwright@1.56.1` |
| FFmpeg | 6.1.1; encoders: libx264, libx264rgb, libvpx/vp9, aac, libopus; filters: drawtext, subtitles, ass, xfade, zoompan, loudnorm, blackdetect, silencedetect |
| Playwright | Chromium build **1194** hazır (`/opt/pw-browsers/chromium-1194`, `PLAYWRIGHT_BROWSERS_PATH` ayarlı). Python `playwright==1.56.0` bu build ile çalıştı (ölçüldü). |
| ImageMagick | `convert` var (`magick` yok); inkscape/rsvg yok |
| Fontlar | DejaVu, Liberation, FreeSans/Serif/Mono, Noto Color Emoji, Unifont (hepsi özgür lisans) |
| apt | archive/security.ubuntu.com erişilebilir; `espeak-ng 1.51` kuruldu |
| docker | istemci var (kullanılmıyor) |

## Ağ (proxy politikası)
Erişilebilir: `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`, `archive.ubuntu.com`, `security.ubuntu.com`, `github.com` (release indirmeleri dahil, HEAD 200), `raw.githubusercontent.com`, `api.github.com` (yalnızca bu repo; diğer repolar 403).

**Engelli (proxy CONNECT 403):** `support.google.com`, `www.youtube.com`, `googleapis.com`, `developers.google.com`, `huggingface.co`, `docs.github.com`, `en.wikipedia.org`, `commons.wikimedia.org`, `api.openverse.org`, `fonts.google.com`, `cdn.jsdelivr.net`, `unpkg.com`, ve denenen tüm üçüncü taraf bloglar (ör. vidiq.com). `WebFetch` aracı aynı politikaya tabi (EGRESS_BLOCKED). **`WebSearch` çalışır** ve özet + URL listesi verir; birincil sayfa içeriğini vermez.

Sonuç: Resmî YouTube/Google sayfaları bu ortamdan doğrudan okunamaz. Politika kayıtları `unverified`/`chatgpt-verified` etiketleriyle tutulur (bkz. `docs/policies/README.md`).

## Ölçülen performans (2026-10-03)
| İş | Sonuç |
|---|---|
| Kokoro-82M (kokoro-onnx 0.6.1, onnxruntime 1.30, CPU 4 thread) | ~24 s ses için 5.4–7.6 s; **RTF ≈ 0.25–0.32**; 24 kHz |
| Whisper base.en (sherpa-onnx 1.13.8, int8) | 24 s ses için ~2.6 s ASR; WER 0.000–0.016 (6 ses) |
| Playwright kare yakalama 1920×1080 | PNG **16 fps**, JPEG q92 **19 fps** (tek sayfa, tek süreç) |
| FFmpeg libx264 crf18 1080p30 (90 kare) | < 2 s |

Çıkarım: 8 dakikalık 1080p30 video ≈ 14.400 kare → tek süreçte ~15 dk kare yakalama; TTS ≈ 2–3 dk; ASR-QC ≈ 1 dk. 4 vCPU'da 2 paralel sayfa ile kare yakalama yaklaşık yarıya iner (ölçülecek).

## GitHub
- Repo `brsctncnbrk7-byte/Claude-code-YouTube-`: **public**, default branch `main` (henüz commit yok), izinler admin/push.
- `gh` CLI'nin GH_TOKEN'ı geçersiz → GitHub işlemleri MCP araçları veya `git` ile.
- Actions: standart runner'lar public repoda ücretsiz (ikincil kaynak; `docs/operations/github-quota.md`).
