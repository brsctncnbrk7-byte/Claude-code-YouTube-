# GitHub Actions — ep-001 release koşuları (public repo, standart `ubuntu-latest`)

| Run | Tetik | Sonuç | Kurulum (apt+uv+Chromium+modeller+testler) | Build (uzun+Short, TTS önbelleksiz) | Artifact | Release | Toplam |
|---|---|---|---|---|---|---|---|
| 37149042055 (#3) | workflow dosyası push (smoke) | ✅ | ~45 s | 3 s test videosu | — | `smoke-37149042055` (3 dosya, sha256 doğrulandı) | 58 s |
| 37151370173 (#4) | `release-requests/ep-001.request` | ❌ release adımı | 1:14 (apt 18 s, Chromium 16 s, modeller 23 s, testler 12 s) | **13:39** | 15.4 MB zip (ep-001-37151370173, 90 gün) | `gh release create` "short: is a directory" → düzeltildi (yalnızca dosyalar) | 15:00 |
| 37152335267 (#5) | request bump (retry 2, tohumlu TTS) | ✅ | 1:20 | **14:07** | 15.4 MB zip | **`ep-001` yayınlandı: 21 varlık** (ep-001.mp4 14.8 MB, Short 1.5 MB, SRT/VTT, 3 thumbnail, metadata, manifest, QC raporu `QC_PASS`) | 15:41 |

Gözlemler:
- Runner build süresi (13.6 dk) bu Claude ortamının ~2 katı (lokal: 5.4 dk uzun + 1 dk Short, önbellekli TTS). Runner'da TTS önbelleği yok; modeller `actions/cache` ile saklanıyor (ikinci koşuda indirme atlanır).
- Ücretsiz standart runner; dakika sayacı public repoda uygulanmıyor (`secondary`). Artifact depolama public repoda ücretsiz (`secondary`); yine de `retention-days: 90` ve bölüm başına ~15 MB.
- Node 20 → 24 uyarısı (actions sürümleri); işlevi etkilemiyor.

## Doğrulama (2026-10-03 20:58 UTC, bu ortamdan)
`ep-001.mp4`, `ep-001-short.mp4`, `ep-001.en.srt`, `thumbnail_A.png`, `qc-report.md` release'ten indirildi; `manifest.json` / `manifest-short.json` sha256 değerleri **birebir eşleşti**. ffprobe: h264 1920×1080, AAC, 288.1 s; Short 1080×1920, 30.0 s. Runner'daki QC raporu: `QC_PASS`.
Sonuç: workflow → release → indirme → checksum zinciri gerçek bölümle doğrulandı (READY ölçütü 7).
