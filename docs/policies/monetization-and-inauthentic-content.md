# Para kazanma politikaları ve "inauthentic content" — kayıt 2026-10-03

## Kaynaklar
- Kanal para kazanma politikaları: https://support.google.com/youtube/answer/1311392 — `unverified` (bu ortamdan açılamadı; ChatGPT yardım talebinde).
- 15 Temmuz 2025 güncellemesi: "repetitious content" → **"inauthentic content"** adı; şablon/seri üretim izlenimi veren, yaratıcının özgün içgörüsünü eklemeyen AI içerik ve düşük eğitim değerli tekrar içerik reklam geliri için uygun değil. Üç aşamalı yaptırım (uyarı → 90 gün askıya alma → YPP'den çıkarma) rapor ediliyor. — `secondary` (WebSearch: fliki.ai, tubebuddy.com, umbrellacreators.com, 2025–2026).

## Bu projeye uygulanan kural (üretim kapısı)
**Üretim yöntemi tek başına uygunluk sağlamaz.** Programatik görsel, TTS veya herhangi bir araç içeriği "özgün" yapmaz. Her video için ayrı ayrı denetlenir ve `qc-report.md`'ye yazılır:
1. **Özgün anlatı**: senaryo bu proje için araştırılıp yazılmış; başka video/metin yeniden anlatımı değil. Bölümün tezi/açısı bir cümleyle yazılabilir.
2. **Doğru araştırma**: her olgusal iddia `sources.md`'de kaynaklı; doğrulanamayan iddia senaryodan çıkar veya "iddia edilir" diye işaretlenir.
3. **Anlamlı görsel açıklama**: görseller anlatıyı açıklar (veri, mekanizma, karşılaştırma); dekoratif tekrar değil. Her sahnenin "bu görsel neyi gösteriyor" satırı `scenes.yaml`'da.
4. **Önceki bölümlerden farklı değer**: konu, veri, görsel yapı ve sonuç önceki bölümlerle çakışmaz; aynı marka şablonu serbest, içerik değil.
5. **Yanıltma yok**: başlık/thumbnail içerikte karşılığı olan vaatler; sahte olay/görsel yok.
6. **Yasak büyüme yolları yok** (bot izlenme, abone satın alma, sub4sub, kendi videolarını izletme, yanıltıcı trafik).

## Reklam uygunluğu (advertiser-friendly)
- Kaynak: https://support.google.com/youtube/answer/6162278 — `unverified`. Konu seçimi şiddet, trajedi, tıbbi ayrıntı gibi hassas alanlarda ölçülü dil kullanır; her bölüm için "reklam uygunluğu notu" `metadata.yaml`'da.
