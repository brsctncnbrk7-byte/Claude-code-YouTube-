# CLAUDE.md — Proje Talimatı (Claude Code için)

Bu repo, sıfırdan kurulan bir YouTube kanalının **tek doğruluk kaynağıdır**: araştırma, kararlar, üretim sistemi, içerik kuyruğu, kalite kontrol ve raporlar burada yaşar. Orijinal görev metni: `docs/MASTER_PROMPT.md`. Kanonik plan: `docs/MASTER_PLAN.md`.

## Görev (tek cümle)
Ücretsiz araçlarla, videoları uçtan uca üreten ve kanal stratejisini veriye göre geliştiren sistemi GitHub'da kur ve yürüt; hazırlık bitince `READY_FOR_VPS` raporu ver ve GitHub'da kal.

## Ana hedef
İlk herkese açık yayından itibaren 30 takvim günü içinde YouTube reklam geliri paylaşımına (YPP) **kabul edilmek**. Agresif hedef, garanti değil. Şu durumlar ayrı izlenir ve biri diğerinin yerine başarı sayılmaz: eşiğe ulaşma → başvuru gönderme → YPP kabulü → reklam geliri etkinleşmesi → ilk ödeme. Kabul/inceleme süresi bizim kontrolümüzde değildir.

## Kesin sınırlar
1. **Sıfır ek ücret.** Yeni ücretli program, SaaS, API, stok medya, müzik, ses, model, GPU, bulut render, hosting, abonelik, domain, reklam, ekipman yok. Kart isteyen deneme ve otomatik ücretlenen katman yok. GitHub Actions'ta yalnızca ücretsiz standart runner (`ubuntu-latest`).
2. **İnsan desteği yalnızca** kanal açma ve YouTube'a yükleme adımında. Kullanıcıdan araştırma, senaryo, seslendirme, görsel seçme, kurgu, altyazı, kodlama, test, render, dinleme veya rutin QC istenmez. Video başına onay süreci kurulmaz.
3. **Lisansı doğrulanmayan araç/varlık üretimde kullanılmaz.** Kod, model ağırlığı, ses modeli, fonemizer, font, veri seti lisansları **ayrı ayrı** doğrulanır; bir reponun lisansı indirme paketine genellenmez. Kayıt: `docs/research/tools-and-licenses.md`.
4. **Resmî kaynaktan doğrulanamayan politika "doğrulanmış" sayılmaz**; `unverified` etiketi taşır (bkz. `docs/STATUS.md` → Açık doğrulamalar).
5. **VPS'e bağlanma, kurulum yapma, mevcut projeleri değiştirme yok.** `READY_FOR_VPS` ilan edilse bile geçiş kullanıcı talebiyle başlar.
6. **Sırlar Git'e ve loglara girmez.** Token, parola, OAuth dosyası, kişisel bilgi yok. `.env.example` yalnızca boş örnek. Commit öncesi `scripts/secret_scan.sh`.
7. **Yasak büyüme yolları:** bot izlenme, abone satın alma, sub4sub, kendi videolarını otomatik izletme, yanıltıcı trafik, yanıltıcı başlık/thumbnail.
8. **Telif:** başka kanalların videoları, senaryoları, thumbnail'ları, film/TV/spor klipleri kopyalanmaz. Her dış varlık için kaynak URL, lisans, edinme tarihi, atıf kaydı tutulur.
9. Ana dal (`main`) çalışır kalır. Küçük commitler. Büyük medya (MP4/WAV/ONNX) Git'e girmez; release/artifact + `manifest.json` (sha256).

## Ortam gerçekleri (bkz. `docs/research/2026-10-03-environment-capabilities.md`)
- Bu Claude Code bulut ortamı: 4 vCPU, 15 GB RAM, ~30 GB disk, Ubuntu 24.04, Python 3.11, Node 22, FFmpeg 6.1, Playwright Chromium 1194 (`/opt/pw-browsers`), `uv`, `apt` çalışır.
- **Ağ politikası** support.google.com, youtube.com, googleapis.com, huggingface.co, docs.github.com, wikipedia ve çoğu üçüncü taraf siteyi engeller (`WebFetch` dahil). Çalışan: `WebSearch`, pypi, npm, apt, github.com, raw.githubusercontent.com, GitHub release indirmeleri.
- Repo **public** (kullanıcı kararı, ADR-003). GitHub Actions standart runner'lar public repoda ücretsiz; bu "her şey sınırsız" demek değildir (bkz. `docs/operations/github-quota.md`).
- Actions runner ortamı bu ortamdan farklıdır: Python, FFmpeg, fontlar, Chromium ve modeller workflow içinde açıkça kurulur; `/opt/pw-browsers` runner'da varsayılmaz.

## Oturum protokolü
**Başlangıç:** `docs/STATUS.md` → `docs/HANDOFF.md` → `content/queue.yaml` sırasıyla oku; `bash scripts/env_check.sh` çalıştır; `git status`/`git log -5`.
**Çalışma:** Rutin yaratıcı/teknik kararlar için onay isteme. Kararları `docs/DECISIONS.md`'ye ADR olarak yaz. Araştırma bulgularını tarihli dosyalara, kaynak URL + erişim tarihi + birincil/ikincil etiketiyle yaz.
**Bitiş:** `docs/STATUS.md` ve `docs/HANDOFF.md` güncelle → `scripts/secret_scan.sh` → commit → `git push -u origin <çalışma dalı>` → push çıktısını kaydet (doğrulanamazsa belirt) → kısa rapor: durum, çıktılar, doğrulama kanıtı, engeller, sonraki adım, commit/push durumu.

## Çalışma dalı
Geliştirme `claude/new-session-dop2fl` dalında. Kullanıcı istemeden PR açılmaz, başka dala push edilmez.

## Alt ajanlar
Araştırma, uygulama, test ve bağımsız inceleme için kullanılabilir. Ana oturum koordinatör ve son karar sahibidir. Alt ajanlar ücretli araç kullanamaz, kapsamı genişletemez, VPS'e geçemez, kullanıcı müdahalesi gerektiren dış işlem yapamaz. Gereksiz paralel çağrı ile kota tüketilmez.

## Üretim kapısı (her video)
`docs/policies/production-gate.md` kontrol listesi geçilmeden paket üretilmez: özgün anlatı, kaynak doğruluğu, anlamlı görsel açıklama, önceki bölümlerden farklı değer, lisans kayıtları, teknik QC, **ses değerlendirmesi** (teknik ölçümler + fonem incelemesi + ASR round-trip; bunlar insan dinlemesinin yerine geçmez ve rapor bunu açıkça söyler).

## Komutlar
```
uv sync                      # bağımlılıklar (sabit sürümler)
bash scripts/env_check.sh    # ortam raporu → reports/env/
uv run pytest -q             # testler
uv run ytf build ep-001      # bölüm üret (checkpoint'li)
uv run ytf qc ep-001         # kalite kontrol raporu
uv run ytf package ep-001    # yükleme paketi → dist/ep-001/
uv run ytf status            # kuyruk durumu
make pilot                   # temiz klondan pilot
```
