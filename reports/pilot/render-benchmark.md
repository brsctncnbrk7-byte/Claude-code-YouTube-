# Render benchmark — Claude Code cloud environment (4 vCPU, 15 GB RAM), 2026-10-03

| Build | Narration | Scenes | Frames | TTS | Render (capture+encode) | Mux+loudness | Total wall | CPU avg | Peak RSS | Output |
|---|---|---|---|---|---|---|---|---|---|---|
| ep-001 long, build 1 (12 scenes) | 228.9 s (44 sentences) | 12 | 6,866 | 58.7 s | 310.0 s | ~10 s | 6:24 | 207 % | 830 MB | 11.8 MB |
| ep-001 long, build 2 (14 scenes; TTS cache warm) | 287.9 s (57 sentences) | 14 | 8,637 | 19.3 s (13 new sentences) | 238.9 s (cached scenes skipped) | ~10 s | 5:21 | 183 % | 784 MB | — |
| ep-001 short (1080×1920) | 29.9 s (9 sentences) | 3 | 898 | 7.5 s | 43.9 s | ~5 s | 0:59 | 196 % | 689 MB | — |

Per-scene capture rate (Playwright PNG screenshots, 1920×1080, 2 worker processes): 12–15 fps per worker → ~25 fps aggregate.
Kokoro-82M TTS real-time factor ≈ 0.26 (CPU, 4 threads). Whisper base.en QC: ~22 s for 229 s of audio.

**Projection (this machine):** an 8-minute episode ≈ 14,400 frames → ~10 min capture + ~1 min encode + ~2 min TTS + ~1.5 min QC ≈ **15 min per long episode**, ~1.5 min per Short.
**GitHub Actions standard runner (4 vCPU/16 GB, secondary source):** similar order; plus ~3 min setup (apt, uv, Chromium, cached models). Verified so far only with the 3-second smoke job (run 37149042055, 58 s total).

Disk: models 560 MB (+300 MB extracted Whisper), TTS cache ~1 MB/min of speech, frames are deleted after each scene encode (peak ~150 MB per scene), dist per episode ~15–25 MB.
