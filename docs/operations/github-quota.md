# GitHub kota ve teslim yolu — 2026-10-03

Kullanıcı kararı (ADR-003/004): repo public kalır; yalnızca ücretsiz standart runner; "sınırsız" varsayılmaz; sınırlar doğrulanır ve kullanım izlenir.

## Bilinen sınırlar (etiketli)
| Kalem | Değer | Kanıt |
|---|---|---|
| Actions dakika, public repo, standart runner | ücretsiz, dakika sayacı yok | `secondary` (WebSearch: GitHub community discussion #70492, warpbuild, cicdcalculator — 2026). docs.github.com engelli. |
| Standart Linux runner (public) | 4 vCPU / 16 GB RAM | `secondary` |
| Artifact saklama | varsayılan 90 gün; public repoda 1–90 gün ayarlanabilir | `secondary` |
| Artifact/cache depolama (public) | ücretsiz | `secondary` |
| Release varlığı | dosya başına < 2 GiB; toplam release boyutu/bant genişliği sınırı yok | `secondary` (GitHub community #73875) |
| Repo boyutu önerisi | < 1 GB önerilir, 5 GB üstü uyarı | `secondary` |
| Daha büyük runner'lar (8/16 core) | **ücretli** — kullanılmaz | `secondary` |

## Teslim yolu kararı
- **Ana yol:** her bölüm için GitHub Release (`ep-001` tag'i) → MP4, thumbnail PNG, SRT/VTT, metadata.yaml, manifest.json (sha256). Kalıcı, ücretsiz, kullanıcı tarayıcıdan indirir.
- **Yedek:** Actions artifact (90 gün, `retention-days: 90`).
- **Git'e girmez:** MP4/WAV/ONNX (`.gitignore`); repo içinde manifest + checksum kopyaları `reports/releases/<ep>/manifest*.json`.

## Tetikleme kararı (ADR-004 / ADR-004a)
- `GITHUB_TOKEN` ile oluşturulan tag/commit'in başka workflow'u **tetiklemediği** varsayılır (GitHub'ın tekrar-tetikleme koruması; `secondary`). Bu nedenle render ve release **aynı workflow koşusunda** yapılır: workflow kullanıcı tag push'u veya `workflow_dispatch` ile başlar, render eder, `softprops/action-gh-release` yerine `gh release create` (runner'da `gh` var, `GITHUB_TOKEN`) ile release'i aynı job'da oluşturur. Ek kullanıcı tokenı gerekmez.
- `workflow_dispatch` yalnızca workflow dosyası **default branch'te** varsa API/UI'dan listelenir (`secondary`; doğrulanacak). Default branch `main` henüz boş → ilk aşamada çalışma dalına `push` tetikleyicisi (`paths: .github/workflows/**, src/**`) ile küçük test; `main` oluşunca `workflow_dispatch` eklenir.
- İzinler: `permissions: contents: read` varsayılan; yalnızca release job'u `contents: write`.

## Runner kurulumu (Claude ortamından ayrı — ADR-005)
Runner'da hazır varsayılmaz: FFmpeg, fontlar, Chromium, modeller, espeak-ng. Workflow adımları:
1. `actions/setup-python@v5` (3.11) + `pip install uv==<sabit>` (setup-uv aksiyonu GitHub API oran sınırına takıldı, run 37156263709) → `uv sync --frozen`
2. `sudo apt-get install -y ffmpeg espeak-ng fonts-dejavu-core`
3. `uv run playwright install --with-deps chromium` (runner'da indirilebilir; Claude ortamında **çalıştırılmaz**)
4. `uv run python scripts/fetch_models.py` (GitHub release'lerinden, sha256 doğrulamalı; `actions/cache` ile önbellek)
5. `uv run ytf build <ep> && uv run ytf qc <ep> && uv run ytf package <ep>`
6. Release job: `gh release create ep-XXX dist/ep-XXX/* --notes-file dist/ep-XXX/RELEASE_NOTES.md`

## Kullanım izleme
Her koşunun süresi ve release boyutu oturumda `reports/quota/actions-*.md`'ye işlenir (Actions API adım zamanları). Workflow'un runner'da yazdığı `reports/quota/run-<id>-<ep>.md` dosyaları commit edilmez (yalnızca artifact içinde); otomatik commit, GITHUB_TOKEN push kısıtı nedeniyle kullanılmaz.
