# Ölçüm ve izleme

## Erişilebilen veri
- **Kamuya açık:** video görüntüleme ve abone sayısı (kanal sayfası). Bu ortam youtube.com'a erişemez; sayılar kullanıcı yükleme adımında bakıp iletirse veya ileride VPS'ten kamuya açık sayfa okunarak alınır.
- **Studio (özel):** gösterim, CTR, ort. izleme süresi, izleyici tutma, trafik kaynakları, **YPP sayacı** (abone + geçerli izlenme saati). Yalnızca kanal sahibi görür. Kullanıcıdan günlük ekran görüntüsü/CSV **istenmez**; yükleme adımında zaten Studio'daysa 30 saniyelik "gün N notu" şablonunu doldurması yeterlidir (`reports/progress/TEMPLATE.md`).
- **YouTube Analytics API (OAuth):** yalnızca kanal sahibinin kendi makinesinde yetkilendirme ile mümkün; token sohbete/Git'e girmez. Bu projenin GitHub aşamasında kurulmaz; VPS aşamasında isteğe bağlı (`vps-setup.md`).

## Ayrı izlenen metrikler
gösterim · CTR · izlenme · ort. izleme süresi · izleyici tutma eğrisi (ilk 30 sn düşüşü) · abone kazanımı · **YPP sayacı** (Studio'daki değer; genel görüntüleme sayısıyla eşitlenmez)

## Kontrol noktaları
Gün 3, 7, 14, 21, 30: `reports/progress/dayNN.md` — plan/gerçek farkı, hangi bölümler öne çıktı, sonraki içerik değişikliği (başlık/thumbnail/konu/süre). Kural: küçük örneklemde kesin sonuç yok; niş değişikliği 14. günden önce yok ve gerekçeli.

## 30. gün raporu
Hedef gerçekleşmezse gizlenmez: eşiklerin neresinde kalındı, üretim/büyüme darboğazları, aynı ücretsiz sınırlar içinde sonraki adımlar. YPP kabulü/gelir kanıt (Studio ekranı) olmadan ilan edilmez.
