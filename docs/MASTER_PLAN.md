# MASTER PLAN — Plotted Past (çalışma adı)

Kanonik plan. Değişiklikler ADR ile (`docs/DECISIONS.md`). Orijinal görev: `docs/MASTER_PROMPT.md`.

## 1. Hedef ve başarı tanımı
**Ana hedef:** İlk herkese açık videonun yayımlandığı günden itibaren **30 takvim günü içinde YouTube reklam geliri paylaşımına (YPP) kabul edilmek.** Agresif; garanti değil.

Ayrı izlenen durumlar (hiçbiri diğerinin yerine başarı sayılmaz):
| # | Durum | Kimin kontrolünde | Kayıt |
|---|---|---|---|
| 1 | Eşiğe ulaşma (1.000 abone + 4.000 saat/12 ay) | içerik + kitle | Studio YPP sayacı (kullanıcı yükleme adımında bakar; günlük ekran görüntüsü istenmez) |
| 2 | Başvuru gönderme | kullanıcı (tek tık) | tarih |
| 3 | YPP kabulü | **YouTube** — süre kontrolümüzde değil | tarih/sonuç |
| 4 | Reklam geliri etkinleşmesi | YouTube + AdSense | tarih |
| 5 | İlk ödeme | AdSense eşiği | tarih |

Hazırlık süresi ayrı sayılır; 30 gün sayacı yayın tarihi bilinmeden başlamaz.

## 2. Eşik matematiği (2026 şartları; 2027 eşikleri uygulanmaz)
İzlenme saati = uygun görüntüleme × ortalama izlenen dakika / 60. Shorts akışı saatleri sayılmaz.

30 günde 4.000 saat → **133 saat/gün ≈ 8.000 izlenen dakika/gün** (ortalama, ilk günden itibaren — gerçekte büyüme eğrisi geç başlar, bu yüzden son haftalarda çok daha yüksek gerekir).

| Senaryo | Uzun video sayısı (30 gün) | Ort. izlenen dk/görüntüleme | Gerekli görüntüleme/gün (ort.) | 30 gün toplam görüntüleme | Abone dönüşümü varsayımı | Beklenen abone | Sonuç |
|---|---|---|---|---|---|---|---|
| Düşük | 10 | 2.0 | 3.200 | 96.000 | %1.0 | ~960 | saat **ve** abone büyük olasılıkla **ulaşılmaz** |
| Temel | 13 | 3.0 | 2.300 | 69.000 | %1.5 | ~1.030 | saat için geç başlayan eğri nedeniyle ulaşılması **olasılık dışı değil ama düşük**; abone sınırda |
| Yüksek | 13 + 13 Short | 3.5 | 1.800 (+Shorts aboneleri) | 54.000 uzun + Shorts | %2 uzun + Shorts | >1.000 | ancak bir-iki videonun öneri sistemine girmesiyle |

**Belirsizlik beyanı:** Yeni kanallarda 1.000 aboneye ortalama ~254 gün rapor ediliyor (`secondary`). 30 günlük hedef, en az bir videonun öneri akışında güçlü performans göstermesine ("viral varsayımı") dayanır; bu bir plan değil, umuttur. Plan, hedefe ulaşılmazsa da değer üreten bir kanal ve sistem bırakmayı garanti eder. Tahminler gerçek veri değildir.

## 3. Niş, dil, vaat (ADR-006, ADR-010)
- **Niş:** Data detective stories — gerçek vakaların veri/grafik/istatistikle çözülmesi; her bölümde veri yeniden çizilir ve canlandırılır.
- **Dil:** İngilizce. **Kitle:** 18–45, meraklı genel izleyici; öğrenciler, veri/bilim/tarih ilgilileri; global.
- **Vaat:** "Every episode, a real mystery solved by a chart — rebuilt from the original numbers."
- **Fark:** Hikâye + orijinal veri + canlı yeniden çizim; stok görsel yok; her iddia kaynaklı; sentetik ses açıkça beyan edilir.

## 4. Format
- Uzun: lansmanda 3–6 dk (ölçülen; ADR-013), hedef 6–9 dk ikinci aşamada; 1920×1080 30fps, anlatıcı (Kokoro), programatik görseller, bölüm işaretleri, altyazı.
- Short: 45–60 sn dikey, bölümün "kanca" kesiti + kanala yönlendirme (saatlere sayılmaz; keşif için).
- Yayın sıklığı: başlangıç varsayımı haftada 3 uzun + 3 Short; pilot render ölçümüyle kesinleşir (ADR-011).

## 5. Aşamalar ve bitiş ölçütleri
| Faz | İçerik | Bitiş kanıtı |
|---|---|---|
| 0 Repo iskeleti | CLAUDE.md, docs, scripts, .gitignore | ilk push |
| 1 Araştırma/kararlar | politika, lisans, niş, dil, hedef matematiği | bu belge + ADR'ler + `docs/research/*` |
| 2 Hat MVP + Pilot #1 | `ytf` paketi, testler, ep-001 uçtan uca, QC | `reports/pilot/ep-001.md` (teknik + içerik ayrı) |
| 3 Pilot #2 + Shorts | ep-002 farklı konu; `--format short`; temiz klon yeniden üretim; ölçümler | `reports/pilot/ep-002.md`, `render-benchmark.md`, `reproducibility.md` |
| 3b Actions teslim zinciri | küçük test çıktısıyla workflow → release → indirme → sha256 | `reports/quota/actions-smoke.md` |
| 4 İlk hafta paketleri | pilotlar başarılıysa 3 uzun + 3 Short tam paket; placeholder yok | `dist/ep-00X/`, `content/publish-queue.yaml` |
| 5 Kanal kiti + operasyon | marka, banner/logo, açıklama, playlist, kurulum listesi, ölçüm/kurtarma/VPS rehberi | `channel/`, `docs/operations/` |
| 6 READY_FOR_VPS | 8 ölçütün kanıt bağlantıları | `reports/READY_FOR_VPS.md` |

**Kural (kullanıcı düzeltmesi #9):** İki farklı konudaki pilot tamamlanıp teknik ve içerik kalitesi ayrı raporlanmadan ilk hafta üretimine geçilmez; başarısız yaklaşım haftaya çoğaltılmaz.

## 6. Yeniden üretilebilirlik tanımı (kullanıcı düzeltmesi #6)
Temiz klondan `make pilot` sonrası:
- Aynı girdiler (episode.yaml, script, scenes, sabit sürümler `uv.lock`, model sha256).
- Aynı süre (±1 kare), aynı kare sayısı, aynı çözünürlük/fps, aynı SRT segment sayısı.
- Görsel tolerans: örneklenen karelerde ortalama mutlak piksel farkı < 1/255 (metin render farkları toleranslı).
- Ses tolerans: cümle süreleri ±20 ms; loudness ±0.5 LU.
- MP4 sha256 eşitliği **zorunlu değil** (encoder zaman damgaları vb.); eşitse ayrıca raporlanır. sha256 teslim bütünlüğü içindir.

## 7. 30 günlük yayın takvimi (taslak; ilk yayın tarihi kullanıcı yükleme adımında belirlenir)
Hafta 1: ep-001, ep-002, ep-003 (+3 Short) • Hafta 2: ep-004–006 • Hafta 3: ep-007–009 • Hafta 4: ep-010–013. Konu kuyruğu: `content/queue.yaml`. Yayın saati: 15:00 UTC (ABD sabahı / Avrupa öğleden sonra; `secondary`), Studio'da zamanlanmış.

## 8. Ölçüm (gün 3, 7, 14, 21, 30)
Kullanıcıdan günlük veri istenmez. Yükleme adımlarında Studio'dan okunabilen (gösterim, CTR, izlenme, ort. izleme süresi, abone, YPP sayacı) `reports/progress/dayNN.md` şablonuna işlenir; yoksa yalnızca kamuya açık sayılar (görüntüleme, abone) kaydedilir ve sınır belirtilir. Küçük örneklemde kesin sonuç yok; niş değişikliği yalnızca 14. gün sonrası ve gerekçeli.

## 9. İnsan desteği sınırı
Yalnızca kanal açma ve yükleme. O adımlarda gereken hesap sahibi işlemleri (kimlik, telefon, 2FA, AdSense, vergi/banka, sözleşme) açıkça `channel/SETUP_CHECKLIST.md` ve `docs/operations/publishing.md`'de. Başka engel çıkarsa yetki uydurulmaz; engel kaydedilir, bağımsız işler sürer.
