# Kararlar (ADR) — tarihli, gerekçeli

Biçim: Bağlam → Karar → Gerekçe → Sonuçlar/İzleme. Yeni karar sona eklenir; eski karar değişirse "superseded by" notu alır.

---
## ADR-001 — Ortam ve ağ kısıtıyla çalışma (2026-10-03)
**Bağlam:** Claude Code bulut ortamının ağ politikası support.google.com, youtube.com, huggingface.co, docs.github.com ve çoğu üçüncü taraf siteyi engelliyor; WebSearch çalışıyor. Kullanıcı mevcut izinlerle devam kararı verdi.
**Karar:** Araştırma WebSearch + erişilebilir birincil kaynaklarla (GitHub raw/README/LICENSE, PyPI metadata, release tarball içi MODEL_CARD) yapılır. Resmî kaynaktan doğrulanamayan politika/lisans **doğrulanmış sayılmaz**; `docs/policies/README.md` etiket şeması uygulanır. Lisansı belirsiz varlık üretimde kullanılmaz. Erişilemeyen bağlantılar ve açık sorular tek dosyada toplanır: `docs/research/HELP_REQUEST_chatgpt.md`.
**Sonuç:** YPP sayfaları `chatgpt-verified` (kullanıcı 2026-10-03'te ChatGPT doğrulamasını iletti); diğer Google sayfaları `unverified`.

## ADR-002 — Repo public kalır (2026-10-03, kullanıcı kararı)
**Karar:** Repo public. Senaryo, kod ve strateji belgeleri açık. Token/parola/OAuth/kişisel bilgi repoya ve loglara girmez (`.gitignore`, `scripts/secret_scan.sh`, log maskeleme).
**Gerekçe:** Public repoda standart runner'lar ücretsiz; şeffaflık kabul edildi.
**Sonuç:** Actions teslim yolu mümkün; bkz. ADR-004.

## ADR-003 — Yalnızca ücretsiz standart runner; sınırlar doğrulanır (2026-10-03, kullanıcı kararı)
**Karar:** `ubuntu-latest` standart runner. Ücretli runner/ek kapasite yok. "Her şey sınırsız" varsayılmaz; artifact saklama, release boyutu, repo boyutu sınırları `docs/operations/github-quota.md`'de etiketli; kullanım `reports/quota/` altında izlenir.

## ADR-004 — Teslim yolu: GitHub Release, aynı workflow koşusunda (2026-10-03)
**Bağlam:** `GITHUB_TOKEN` ile yapılan push/tag yeni workflow tetiklemez (resmî davranış; `secondary` kaynak: GitHub Docs özeti, community #25617). `workflow_dispatch` için workflow dosyasının default branch'te olması gerekir (`secondary`).
**Karar:** Render + QC + paket + `gh release create` **tek workflow koşusunda**. Tetikleyici: kullanıcı/oturum tarafından push edilen `ep-*` tag'i veya `workflow_dispatch` (main oluşunca). Ek kullanıcı tokenı yok. `contents: write` yalnızca release job'una. İlk doğrulama küçük test çıktısıyla (workflow → release → indirme → sha256) yapılır; büyük render sonra.
**Sonuç:** `.github/workflows/release.yml`; Actions çıktısı `secondary` kaynaklı sınırlar içinde.

## ADR-005 — Runner ortamı Claude ortamından ayrıdır (2026-10-03)
**Karar:** Workflow içinde Python (setup-python + uv), FFmpeg/espeak-ng/fontlar (apt), Chromium (`playwright install --with-deps chromium`), modeller (`scripts/fetch_models.py`, sha256, cache) açıkça kurulur. `/opt/pw-browsers` runner'da varsayılmaz. Claude ortamında `playwright install` çalıştırılmaz (hazır build 1194 kullanılır; `PLAYWRIGHT_BROWSERS_PATH` zaten ayarlı).

## ADR-006 — Dil: İngilizce; TTS: Kokoro-82M (2026-10-03)
**Bağlam:** Ticari kullanıma açık **Türkçe** TTS bulunamadı: Piper `tr_TR-dfki` CC BY-NC-SA; `fahrettin`/`fettah` veri seti CC0 ama `en_US-lessac` (Blizzard 2013, "research purposes") tabanından fine-tune → türev ağırlıkların ticari durumu belirsiz (bkz. `docs/research/tools-and-licenses.md`). Coqui XTTS CPML. espeak-ng Türkçe kalitesi yayın için yetersiz. Hugging Face engelli. Ayrıca Türkiye CPM'i global İngilizce kitleye göre belirgin düşük (`secondary`: 0.5–5 $ vs 5–20 $).
**Karar:** Kanal dili **İngilizce** (global kitle). TTS **Kokoro-82M** (ağırlıklar Apache-2.0 — hexgrad/kokoro README, GitHub) `kokoro-onnx` (MIT) ile CPU'da; ses paketi `voices-v1.0.bin`. Ses seçimi pilot ASR/fonem/spektrogram değerlendirmesiyle (`reports/pilot/voice-selection.md`).
**İzleme:** HF LICENSE/VOICES.md doğrudan okunamadı → ChatGPT yardım talebi maddesi. Türkçe seçeneği ticari lisanslı bir Türkçe ses doğrulanırsa yeniden açılır.

## ADR-007 — Render yolu: HTML/CSS/SVG sahneleri + Playwright kare yakalama + FFmpeg (2026-10-03)
**Bağlam:** Ölçüm: Playwright 1920×1080 PNG 16 fps, JPEG 19 fps; FFmpeg libx264 hızlı. Manim ek sistem bağımlılığı; Remotion lisans belirsizliği; Pillow ile tipografi/animasyon kalitesi düşük.
**Karar:** Sahneler HTML/CSS/JS (deterministik sanal saat `setFrame(i)`), Playwright ile kare kare PNG, FFmpeg ile h264 1080p30. Stok görsel/video yok; müzik yok veya programatik üretilir (lisans riski sıfır). 2 paralel sayfa ile hızlandırma pilotta ölçülür.
**Sonuç:** 8 dk video için tahmini kare yakalama ~8–15 dk (4 vCPU).

## ADR-008 — Ses QC: fonem + ASR round-trip + spektrogram; insan dinlemesi yerine geçmez (2026-10-03, kullanıcı düzeltmesi #4)
**Karar:** `docs/policies/production-gate.md` §C. ASR: Whisper base.en (MIT) sherpa-onnx (Apache-2.0) ile; modeller GitHub release'inden. Ölçüm: 6 Kokoro sesi için WER 0.000–0.016 (örnek metin). Teknik ölçümler telaffuz onayı değildir; üç katman tamamlanmadan `QC_PASS` verilmez; eksikse `QC_PASS_TECHNICAL_ONLY` ve açık engel kaydı.

## ADR-009 — Altyazı: TTS cümle zamanlamasından (2026-10-03)
**Karar:** SRT/VTT, cümle bazlı sentez sürelerinden üretilir (ASR gerekmez); ASR yalnızca QC'de doğrulama için kullanılır ve altyazı-ASR uyumu raporlanır.

## ADR-010 — Niş ve kanal vaadi (2026-10-03)
Bkz. `docs/research/niche-comparison.md`. **Karar:** "Data detective stories": gerçek tarihî/bilimsel vakaların bir veri, grafik veya istatistiksel akıl yürütmeyle nasıl çözüldüğünü (ya da yanlış yönlendirdiğini) anlatan, her bölümde ilgili veriyi **yeniden çizip canlandıran** 6–9 dakikalık İngilizce açıklayıcı videolar; her bölüme eşlik eden 1 Short (keşif amaçlı). Çalışma adı **"Plotted Past"** (alternatifler `channel/brand.md`).
**Gerekçe:** (1) Eğitim/bilim nişi en yüksek RPM bandında (`secondary`); (2) tamamen programatik, kaynaklı veri görselleriyle üretilebilir — stok medya/telif riski yok; (3) her bölüm kendi araştırması ve verisiyle zorunlu olarak farklı → inauthentic content riskine yapısal direnç (uygunluğu yine bölüm bazında denetlenir); (4) aramada bu konuya adanmış bir kanal bulunamadı; var olanlar tekil videolar (Tableau, Flourish, ders videoları); (5) evergreen; (6) konu havuzu geniş (≥ 40 vaka listelendi).
**Riskler:** Olgusal doğruluk WebSearch kaynaklarına bağlı (birincil tarihsel yayınlar çoğu kez erişilemez) → her iddia kaynaklı, belirsizler yumuşatılır. 30 günde YPP eşiği istatistiksel olarak düşük olasılık (`secondary`: ortalama 1.000 aboneye ~254 gün) — plan bunu açıkça yazar.

## ADR-011 — Format dengesi ve sayaç (2026-10-03)
**Karar:** Ana ürün uzun video (izlenme saati eşiği için). Shorts yalnızca keşif/abone için; Shorts saatleri 4.000 saat eşiğine eklenmez; 10M Shorts yolu hedeflenmez. Yayın sıklığı pilot render ölçümünden sonra kesinleşir (başlangıç varsayımı: haftada 3 uzun + 3 Short; `docs/MASTER_PLAN.md`).

## ADR-004a — Tetikleme düzeltmesi: release-request dosyası (2026-10-03)
**Bağlam:** Bu ortamın git proxy'si tag push'unu reddediyor ("remote end hung up"; yalnızca çalışma dalı push edilebiliyor). `workflow_dispatch` default branch gerektiriyor; `main` yok ve izinsiz oluşturulmaz.
**Karar:** Workflow, `release-requests/<ep>.request` dosyasını ekleyen/değiştiren push ile tetiklenir; yalnızca workflow dosyasına dokunan push smoke testi çalıştırır. Release tag'i `gh release create` ile koşunun içinde oluşturulur (GITHUB_TOKEN; başka workflow tetiklemez). Ek kullanıcı tokenı yok. Bkz. `release-requests/README.md`.

## ADR-012 — TTS deterministikliği: cümle başına tohumlanmış ONNX oturumu (2026-10-03)
**Bağlam:** Temiz klon testi (`reports/pilot/reproducibility.md`): Kokoro çıktısı aynı metin için çalıştırmalar arası farklı (örnek değerlerde ±0.13, cümle sürelerinde 200 ms'ye kadar). Neden: ONNX grafiği rastgele gürültü çekiyor; ORT tek iş parçacığında bile farklı. Deney: `onnxruntime.set_seed(s)` oturum oluşturulmadan önce çağrılırsa aynı çağrı sırası **bit-düzeyinde aynı** çıktı veriyor.
**Karar:** Her cümle için `seed = hash(metin|ses|hız|dil)` ile yeni oturum; böylece her cümle tek başına deterministik, önbellek sırası önemsiz. Maliyet: cümle başına oturum yükleme (ölçüm `render-benchmark.md`). Yeniden üretilebilirlik tanımı (MASTER_PLAN §6) korunur; MP4 sha256 eşitliği yine zorunlu değil.

## ADR-013 — Lansman formatı 3–6 dakika; 6–9 dakika hedefi ikinci aşamaya (2026-10-03)
**Bağlam:** Üç pilot/ilk hafta bölümü 450–600 kelimelik senaryolarla 2.6–4.8 dk çıktı. Aynı veri ve tezle 6–9 dk'ya çıkmak ya dolgu (inauthentic riski) ya da her bölüm için 2–3 ek veri sahnesi ve ek kaynak araştırması gerektiriyor.
**Karar:** İlk hafta bölümleri ölçülen uzunlukta yayımlanır (3–6 dk, yoğun ve kaynaklı). 6–9 dk hedefi, 7. gün verisinden sonra (izleyici tutma eğrisi) yeniden değerlendirilir; uzatma yalnızca ek veri/olgu ile yapılır. MASTER_PLAN §4 ve eşik matematiği buna göre güncellendi (ort. izlenen dk varsayımı 2.0–3.5).
**Risk:** Daha kısa videolar izlenme saati eşiğini zorlaştırır (saat = izlenme × dk/60); planın belirsizlik beyanı zaten bunu kapsıyor. Shorts yalnızca keşif için kalır.
