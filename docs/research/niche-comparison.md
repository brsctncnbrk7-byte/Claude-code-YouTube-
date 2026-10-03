# Niş karşılaştırması — 2026-10-03

Yöntem: WebSearch (ikincil) + ortam kısıtları (ücretsiz, CPU, lisans, ağ). Kamuya açık olmayan metrikler (CTR, izleyici tutma, gelir) **yazılmaz**; RPM değerleri `secondary` ve **tahmin**. YouTube sayfaları bu ortamdan açılamadığı için abone sayıları arama özetlerinden alınmıştır (`secondary`, gözlem tarihi 2026-10-03).

## Puan matrisi (1–5; yüksek iyi)
| Kriter | A. Data detective stories | B. Algoritmalar görsel | C. Açık veri hikâyeleri | D. Harita/tarih animasyon | E. Programlama kavramları | F. Türkçe eğitim (A/B'nin TR'si) | G. Shorts-first simülasyon |
|---|---|---|---|---|---|---|---|
| Talep (eğitim/bilim izleyicisi) | 4 | 3 | 4 | 5 | 4 | 3 | 3 |
| Rekabet (düşük=iyi) | 4 | 2 | 3 | 1 | 2 | 3 | 2 |
| Yeni kanal erişilebilirliği | 4 | 3 | 3 | 2 | 3 | 3 | 3 |
| Özgün değer üretme imkânı | 5 | 3 | 4 | 3 | 3 | 4 | 2 |
| Ücretsiz üretim kalitesi (programatik) | 5 | 5 | 5 | 4 | 4 | 2 (TTS yok) | 4 |
| Telif/lisans riski (düşük=iyi) | 4 | 5 | 3 (veri lisansı) | 4 | 5 | 4 | 5 |
| Reklam uygunluğu | 4 | 5 | 4 | 3 (savaş/şiddet) | 5 | 4 | 4 |
| Otomasyon uyumu | 4 | 4 | 4 | 3 | 4 | 4 | 5 |
| CPU maliyeti (düşük=iyi) | 4 | 4 | 4 | 3 | 4 | 4 | 5 |
| 30 gün büyüme potansiyeli | 3 | 2 | 3 | 3 | 3 | 2 | 2 (10M yolu gerçekçi değil) |
| RPM bandı (`secondary`) | 5 (Eğitim/Bilim ~10 $ medyan) | 4 (Tech 4–12 $) | 4 | 4 (Tarih 3–9 $) | 4 | 1 (TR CPM 0.5–5 $) | 2 |
| **Toplam** | **46** | 40 | 41 | 35 | 41 | 34 | 37 |

## Nişler ve gözlemler
**A. Data detective stories** — gerçek vakaların veri/grafik/istatistikle çözülmesi (Snow 1854 kolera haritası; Nightingale'in gül diyagramı; Minard'ın Napolyon grafiği; Challenger O-ring verisi; Abraham Wald ve bombardıman uçakları; Semmelweis; Simpson paradoksu — Berkeley kabulleri; Benford yasası ile dolandırıcılık; Anscombe dörtlüsü; Literary Digest 1936 anket fiyaskosu; Monty Hall; Sally Clark davası ve savcı yanılgısı; Ignaz Semmelweis; Halley'in ölüm tabloları; Playfair'in ilk çubuk grafiği…). Aramada bu konuya adanmış kanal bulunamadı; tekil videolar var: "Data Visualization in the Time of Cholera" (YouTube, Tableau), "London Cholera Outbreak: Early Data Visualizations" (ders), Flourish/ProPublica blogları. Komşu büyük kanallar: Veritasium (16.2M), Numberphile, Stand-up Maths — hepsi genel; bu formatı seri yapmıyor. (Gözlem 2026-10-03, `secondary`.)
**B. Algoritmalar görsel** — Reducible (~337k), Polylog (~119k), Spanning Tree (~1.2k), 3Blue1Brown devasa. Kalite çıtası çok yüksek; kitle dar.
**C. Açık veri hikâyeleri** — veri erişimi bu ortamda sınırlı (OWID arşiv/lisanssız; datasets/* PDDL fakat kaynak koşulları ayrı). Her bölüm veri lisansı doğrulaması ister; A nişinin tarihî verileri kamu malı → daha temiz.
**D. Harita/tarih** — Kings and Generals, History Matters, Ollie Bye gibi çok güçlü rakipler; savaş içeriği reklam uygunluğu riski.
**E. Programlama kavramları** — Fireship (3M+) ve yüzlerce kanal; TTS anlatımla fark yaratmak zor.
**F. Türkçe** — ticari lisanslı Türkçe TTS doğrulanamadı (ADR-006); CPM düşük.
**G. Shorts-first** — 90 günde 10M görüntüleme yeni kanal için gerçekçi değil; Shorts yalnızca destek.

## Dil kararı
İngilizce (ADR-006): TTS lisansı + kitle büyüklüğü + RPM. Türkçe yeniden değerlendirme koşulu: ticari lisansı birincil kaynaktan doğrulanmış Türkçe ses.

## Kaynaklar (erişim 2026-10-03, hepsi `secondary`)
- RPM/niş: air.io "YouTube RPM by niche 2026", fluxnote.io, outlierkit.com
- Büyüme süresi: scalelab.com (1.000 aboneye ortalama ~254 gün), vidiq.com/research/youtube-subscriber-benchmarks-2026
- Shorts/uzun: air.io, miraflow.ai, ytgrowth.io (Shorts saatleri 4.000 saate sayılmaz; karma format daha hızlı abone)
- Kanal büyüklükleri: WebSearch özetleri (Reducible, Polylog, Spanning Tree, Veritasium)
- Türkiye CPM: maliyeti.com.tr, hesabiniyap.com, camdalio.com
