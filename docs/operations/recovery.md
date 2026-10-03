# Kurtarma ve devam

- **Oturum koptu / konteyner sıfırlandı:** repo tek doğruluk kaynağı. `git clone` → `uv sync --frozen --extra dev` → `uv run python scripts/fetch_models.py` → `make pilot`. Modeller GitHub release'lerinden sha256 doğrulamalı iner.
- **Yarım kalan build:** `build/<ep>/<fmt>/ck/*.done` checkpoint'leri; `uv run ytf build <ep>` kaldığı yerden devam eder (TTS cümle önbelleği `build/_tts_cache`, sahne segmentleri). Tamamen yeniden üretim: `--force`.
- **Hata kaydı:** `build/<ep>/<fmt>/error.log` (retry denemeleri). FFmpeg/Chromium adımları 2–3 denemeli.
- **Bozuk çıktı:** `uv run ytf qc <ep>` raporu `reports/<ep>/<fmt>/qc-report.md`; kare örnekleri `frames/`.
- **Actions koşusu başarısız:** `reports/quota/` ve Actions log; en sık neden: Chromium kurulumu veya model indirme → workflow'da `playwright install --with-deps chromium` ve `fetch_models.py` adımları.
- **Teslim dosyası bütünlüğü:** `dist/<ep>/manifest.json` sha256 ile indirilen dosya karşılaştırılır.
- **Model kaynağı erişilemez olursa:** sha256'ları bilinen dosyalar; alternatif ayna yalnızca lisansı aynı olan resmî dağıtımlardan (kokoro-onnx/sherpa-onnx release'leri).
