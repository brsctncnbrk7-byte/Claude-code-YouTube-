# VPS kurulum rehberi (TASLAK — VPS'te denenmedi)

> Bu rehber bu Claude ortamındaki gerçek ölçümlerden türetilmiştir; **VPS'te test edilmemiştir**. Geçiş yalnızca kullanıcı talebiyle başlar (CLAUDE.md §5).

## Ölçülen gereksinimler (2026-10-03, ep-001 pilot; derleme 1: 229 s, yayımlanan sürüm: 288 s)
| Kaynak | Ölçüm | VPS önerisi |
|---|---|---|
| CPU | 4 vCPU; build %207 CPU ortalaması (2 Playwright işçisi + ffmpeg) | ≥ 2 vCPU çalışır (2× yavaş), 4 vCPU ideal |
| RAM | tepe RSS 1.34 GB (build, cümle başına tohumlu TTS oturumu), Whisper QC ~1 GB | ≥ 3 GB boş; 4 GB rahat |
| Disk | modeller 560 MB + çıkarılmış whisper 300 MB; build/ep başına ~150 MB (kareler silinir); dist/ep ~15 MB | ≥ 10 GB boş |
| Süre | derleme 1: TTS 59 s (229 s ses), render 310 s, QC 56 s; yayımlanan 288 s sürüm temiz klonda 9:49 (tohumlu TTS ~2 dk); derin ses QC (iki ASR + DNSMOS) +3–5 dk | 5 dk video ≈ 12–15 dk/ep (4 vCPU) |
| Ağ | GitHub release indirme (modeller), pypi/apt | çıkış erişimi gerekli |

## Kurulum adımları (Ubuntu 22.04/24.04)
```bash
sudo apt-get update && sudo apt-get install -y git ffmpeg espeak-ng fonts-dejavu-core time curl
curl -LsSf https://astral.sh/uv/install.sh | sh          # uv (ücretsiz)
git clone https://github.com/brsctncnbrk7-byte/Claude-code-YouTube-.git && cd Claude-code-YouTube-
uv sync --frozen --extra dev
uv run playwright install --with-deps chromium           # Chromium + sistem bağımlılıkları
uv run python scripts/fetch_models.py                    # sha256 doğrulamalı
uv run pytest -q && make pilot                           # doğrulama
```
## Zamanlayıcı (örnek cron; yalnızca `scripted` bölümleri render eder)
```
0 3 * * * cd ~/Claude-code-YouTube- && git pull -q && ./scripts/render_queue.sh >> logs/cron.log 2>&1
```
`scripts/render_queue.sh` (mevcut, VPS'te denenmedi): `content/queue.yaml`'da `status: scripted` olan ilk bölümü `ytf all` ile üretir, `dist/` çıktısını release-request commit'iyle GitHub'a gönderir. Senaryo üretimi her zaman Claude oturumu ister (docs/operations/session-continuity.md).

## Mevcut projelere dokunmama
Ayrı kullanıcı (`ytf`) ve ayrı dizin; sistem paketleri dışında global değişiklik yok; mevcut servisler/portlar kullanılmaz (sunucu gerekmez).
