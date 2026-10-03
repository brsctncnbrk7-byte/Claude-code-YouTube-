# Plotted Past — YouTube üretim sistemi (çalışma adı)

Sıfırdan kurulan, **ücretsiz araçlarla uçtan uca video üreten** bir YouTube kanalı projesi. Bu repo tek doğruluk kaynağıdır: araştırma, kararlar, üretim hattı, içerik kuyruğu, kalite kontrol, raporlar.

- Görev metni: `docs/MASTER_PROMPT.md` • Plan: `docs/MASTER_PLAN.md` • Kararlar: `docs/DECISIONS.md`
- Durum: `docs/STATUS.md` • Sonraki iş: `docs/HANDOFF.md` • Claude çalışma kuralları: `CLAUDE.md`

## Ne üretir?
İngilizce, 6–9 dakikalık "data detective" açıklayıcı videolar: gerçek bir vaka, orijinal sayılardan yeniden çizilen ve canlandırılan grafiklerle anlatılır. Anlatım sentetik ses (Kokoro-82M, Apache-2.0). Tüm görseller programatik (HTML/SVG → Playwright → FFmpeg). Stok medya yok.

## Tek komutla pilot
```bash
uv sync --frozen                      # bağımlılıklar (Python 3.11)
uv run python scripts/fetch_models.py # Kokoro + Whisper modelleri (GitHub release, sha256 doğrulamalı)
make pilot                            # ep-001'i üretir, QC yapar, dist/ep-001/ paketini çıkarır
```
Ayrıntı: `uv run ytf --help`. Sistem gereksinimleri: ffmpeg, espeak-ng, Chromium (Playwright). Bu Claude ortamında Chromium hazırdır; GitHub Actions runner'ında `playwright install --with-deps chromium` çalışır (`.github/workflows/`).

## Dizin yapısı
```
docs/            plan, kararlar, durum, araştırma, politika, operasyon
channel/         marka ve kanal kurulum paketi
content/         bölüm kuyruğu, senaryolar, sahne planları, lisans kayıtları
src/ytf/         üretim hattı (tts, render, assemble, qc, package, jobs)
scripts/         env_check, secret_scan, fetch_models
tests/           pytest
reports/         pilot, kota, ilerleme raporları
assets/fonts/    Inter (OFL 1.1) + lisans metni
```
Büyük çıktılar (MP4/WAV/ONNX) Git'e girmez; GitHub Release varlığı olarak teslim edilir, `manifest.json` sha256 ile.

## Lisans
Kod ve belgeler MIT (`LICENSE`). Bileşen lisansları: `docs/research/tools-and-licenses.md`.
