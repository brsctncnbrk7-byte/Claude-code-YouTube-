# GitHub Actions — ep-002 release koşusu
| Run | Tetik | Sonuç | Build (uzun+Short) | Release |
|---|---|---|---|---|
| (head 732e2df, 2026-10-03 20:58→21:08 UTC) | `release-requests/ep-002.request` | ✅ | ~9 dk (3.0 dk video + Short) | `ep-002` yayınlandı: 21 varlık; `ep-002.mp4`, `ep-002-short.mp4`, `qc-report.md` indirildi → `manifest*.json` sha256 **eşleşti**; runner QC: `QC_PASS`; süre 179.6 s |
Not: Bu koşu, espeak sabitlemesinden önceki koda aittir (ses içeriği geçerli ve QC_PASS; ancak yeniden üretilebilirlik düzeltmesinden sonra ep-001/ep-002 yeniden yayımlanacak — bkz. reproducibility.md Koşu 3).

# ep-003 release koşusu
| Run 37157099672 | `release-requests/ep-003.request` | ✅ | ~9 dk (2.6 dk video + Short) | `ep-003` yayınlandı 22:21 UTC, 21 varlık; sha256 eşleşti; runner MP4'leri yerel derlemelerle bit-aynı; QC_PASS |
