# Örnek inceleme linkleri — ep-001, ep-002 (2026-10-04)

Kullanıcı isteği: telefondan indirip izlemek için doğrudan release asset URL'leri. Yeniden render yapılmadı; mevcut release varlıkları kullanıldı.
Doğrulama: her URL `curl -L` ile indirildi (HTTP 200), sha256 release içindeki `manifest.json` / `manifest-short.json` ile birebir eşleşti, süre `ffprobe` ile okundu.

| Bölüm | Dosya | Süre | Boyut | sha256 (manifest = indirilen) | URL |
|---|---|---|---|---|---|
| ep-001 | ep-001.mp4 (1920×1080, 30 fps, h264/aac) | 288.1 s (4:48) | 14 816 085 B (14.1 MiB) | 12e4f6d2…8cb0e73 | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-001/ep-001.mp4 |
| ep-001 | ep-001-short.mp4 (1080×1920) | 30.0 s | 1 533 612 B (1.5 MiB) | 62289458…02a1ba5 | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-001/ep-001-short.mp4 |
| ep-001 | thumbnail_A.png (seçili, 1280×720) | — | 196 548 B | 4e565a11…0aefbe844 | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-001/thumbnail_A.png |
| ep-001 | thumbnail_B.png / thumbnail_C.png (alternatif) | — | 225 241 B / 156 573 B | 9ae9a7cb… / b927b4c6… | …/ep-001/thumbnail_B.png · …/ep-001/thumbnail_C.png |
| ep-002 | ep-002.mp4 (1920×1080, 30 fps, h264/aac) | 179.6 s (3:00) | 8 777 106 B (8.4 MiB) | 6bb9a2f8…8cb069e | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-002/ep-002.mp4 |
| ep-002 | ep-002-short.mp4 (1080×1920) | 24.1 s | 1 108 056 B (1.1 MiB) | d8097cef…ebcee06 | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-002/ep-002-short.mp4 |
| ep-002 | thumbnail_A.png (seçili, 1280×720) | — | 170 287 B | 5d2f593f…7f670502 | https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-/releases/download/ep-002/thumbnail_A.png |
| ep-002 | thumbnail_B.png / thumbnail_C.png (alternatif) | — | 211 336 B / 115 460 B | 637f40cf… / 94146cdb… | …/ep-002/thumbnail_B.png · …/ep-002/thumbnail_C.png |

Durum: kullanıcı incelemesi bekleniyor. İçerik kabulü ve `first_public_publish_utc` kullanıcı adına kaydedilmedi.
