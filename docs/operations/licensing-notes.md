# Lisans notları (repo kodu ve araç zinciri)

- Bu reponun kodu ve belgeleri: **MIT** (`LICENSE`). Senaryolar ve üretilen videolar: proje sahibine ait; yayın koşulları YouTube ile.
- Üretim hattı çalışma zamanında GPL-3.0 bileşenler kullanır (`phonemizer`, `espeak-ng`). Bu bileşenler yalnızca süreç içinde çağrılır; **üretilen ses/video çıktısı GPL kapsamında değildir** (GPL çıktıya uzanmaz). Repo yalnızca kaynak kod dağıtır; birleştirme kullanıcı kurulumunda olur. Daha katı yorum istenirse `kokoro` (hexgrad, Apache-2.0, `misaki` G2P ile) alternatifine geçilebilir — ADR gerektirir.
- Model ağırlıkları (Kokoro, Whisper) repoya girmez; `scripts/fetch_models.py` sha256 ile indirir; lisans kayıtları `docs/research/tools-and-licenses.md`.
- Fontlar: sistem DejaVu; Inter (OFL 1.1) `assets/fonts/` altında OFL metniyle birlikte (OFL dağıtıma izin verir).
- Veri setleri: bölüm bazında `content/<ep>/sources.md` + `content/licenses/datasets.md`.
