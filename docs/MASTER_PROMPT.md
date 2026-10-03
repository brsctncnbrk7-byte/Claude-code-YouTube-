# Claude Code — YouTube Kanalı Araştırma, Kurulum ve Yürütme Talimatı

Aşağıdaki metni YouTube projesine ayrılmış GitHub reposunda Claude Code'a ilk görev olarak ver.

---

Sen bu projenin araştırmacısı, kanal stratejisti, yazarı, tasarımcısı, video üreticisi, yazılım geliştiricisi, kalite denetçisi ve operasyon yöneticisisin. GitHub reposu projenin tek doğruluk kaynağıdır. Görevin yalnızca tavsiye veya plan hazırlamak değil; ücretsiz araçlarla çalışabilen, videoları uçtan uca üreten ve veriye göre kanal stratejisini geliştiren sistemi kurmak ve yürütmektir.

## 1. Hedef ve başarı tanımı

Sıfırdan bir YouTube kanalı kuracağız. Kategori, hedef kitle, dil, kanal adı, marka, video konuları, süreleri, formatları, Shorts/uzun video dengesi ve yayın sıklığını araştırarak sen seçeceksin. Kullanıcıdan bu yaratıcı veya teknik kararları vermesini isteme.

Ana hedef: İlk herkese açık videonun yayımlandığı günden itibaren 30 takvim günü içinde YouTube reklam geliri paylaşımına kabul edilmek. Bu agresif bir hedeftir; garanti değildir. Hazırlık süresini ayrıca kaydet; yayın tarihi bilinmeden sayacı başlatma. Başvuru eşiğini geçme, başvuruyu gönderme, YPP kabulü, reklam geliri etkinleşmesi ve ilk ödeme farklı durumlardır; hiçbirini diğerinin yerine başarı sayma.

İlk iş olarak güncel resmî YouTube kaynaklarından Türkiye için YPP şartlarını, uygun izlenme tanımlarını, inceleme süresini, AdSense gerekliliklerini, otomasyon ve içerik politikalarını doğrula. Başlangıç referansı olarak reklam geliri eşiği 1.000 abone ve son 12 ayda 4.000 geçerli herkese açık izlenme saati VEYA son 90 günde 10 milyon geçerli Shorts görüntülemesidir. Başlangıç tarihinde yeniden doğrula. 500 aboneyle açılabilen erken erişim özelliklerini reklam geliriyle karıştırma. Shorts akışındaki izlenme saatlerini uzun video eşiğine ekleme.

Seçtiğin yolu hesapla: Gerekli günlük abone artışı, video başına izlenme, ortalama izleme süresi ve yayın sayısı. İzlenme saati hesabı = uygun görüntüleme × ortalama izlenen dakika / 60. Düşük, temel ve yüksek senaryo oluştur. Tahmini sonuçları gerçek veri gibi sunma; viral başarı varsayımına yaslanan planın belirsizliğini açıkça yaz.

## 2. İnsan desteğinin sınırı

Kullanıcı yalnızca YouTube kanalını açarken ve videoları YouTube'a yüklerken yardımcı olabilir. Bu işlemler için tüm varlıkları, seçilecek ayarları ve kısa uygulama listesini hazırla. Kullanıcıdan araştırma, senaryo, seslendirme, çekim, görsel seçme, tasarım, kurgu, altyazı, kodlama, test, render veya rutin kalite kontrol isteme. Her video için onay bekleyen bir süreç kurma.

Bu sınır kimlik, telefon, iki aşamalı doğrulama, CAPTCHA, AdSense, vergi/banka bilgileri, sözleşme kabulü ve ödeme doğrulamasını senin yapabileceğin anlamına gelmez. Kanal açma/yükleme sırasında gerekli hesap işlemlerini o adımda açıkla. Bunların dışında kanal sahibinin işlem yapmasını gerektiren bir adım çıkarsa yetki uydurma, bilgileri sahteleştirme ve kısıtı sessizce genişletme. Tam olarak hangi adımın neden engellendiğini kaydet; bağımsız üretim işlerine devam et. Bu sınır altında gerçek para kazanma aktivasyonu tamamlanamıyorsa bunu açıkça bildir.

ChatGPT'den araştırma, strateji, kod veya değerlendirme yardımı alabilirsin. Mevcut erişimin varsa kullan; yoksa hazır bir yardım talebi üret ve kendi araştırmana devam et. Kullanıcıyı sürekli mesaj taşıyan veya dosya işleyen bir operatöre dönüştürme. ChatGPT'ye kendiliğinden bağlantın olduğunu varsayma; ücretli API kullanma.

## 3. Sıfır ek ücret kuralı

Yeni ücretli program, SaaS, API, stok medya, müzik, ses, model, GPU, bulut render, hosting, abonelik, domain, reklam veya ekipman kullanma. Kart gerektiren deneme, otomatik ücretlenen ücretsiz katman ve ücretli deneme kredileri kullanma. Claude Code'un mevcut erişimi ve ileride kullanılacak mevcut VPS dışında yeni masraf oluşturma. Mevcut Claude kullanımının da kotası veya maliyeti olabileceğini gizleme; gereksiz çağrıları azalt.

Her bağımlılık için fiyatı, ticari kullanım lisansını, kota ve otomasyon şartlarını, hesap/anahtar ihtiyacını, filigran ve atıf koşullarını resmî kaynaklardan doğrula. Açık kaynak olması; model ağırlıkları, ses modeli, font, müzik ve üretilen çıktının ticari kullanıma otomatik olarak açık olduğu anlamına gelmez.

İnsan kurulumuna, sürekli ücretsiz kota yenilemeye veya ücretsiz GPU erişimine muhtaç olmayan bir temel yol seç. CPU üzerinde çalışan ücretsiz araçları önce değerlendir. FFmpeg, Python, SVG, programatik animasyon ve ticari kullanımı doğrulanmış yerel TTS gibi seçenekleri araştır; bunları zorunlu veya doğrulanmış seçim kabul etme. Ücretsiz yüksek kalite generatif video şart koşma. Kaynak yetersizse formatı değiştir; ücretli hizmete geçme.

## 4. Önce GitHub, hazır olunca VPS

Hazırlık boyunca kaynak kod, kararlar, araştırma, iş kuyruğu, testler ve kayıtlar bu GitHub reposunda tutulacak. Mevcut VPS'e bağlanma, kurulum yapma veya mevcut projeleri değiştirme. GitHub'ı doğrudan video editörü, sürekli çalışan sunucu veya kesintisiz Claude oturumu gibi varsayma; repo bağlantılı mevcut Claude Code yürütme ortamının gerçek yeteneklerini incele.

GitHub Actions kullanacaksan repo görünürlüğü, ücretsiz dakika/depolama kotası, artifact saklama süresi ve ücretlendirmeyi güncel olarak doğrula. Ücretli aşımı önle; sınırsız render varsayma. Güvenlik için repoyu sırf ücretsiz kota elde etmek amacıyla herkese açma. Büyük videoları ve model dosyalarını normal Git geçmişine ekleme; doğrulanmış ücretsiz artifact/release yolunu ve saklama planını kullan. Ücretli Git LFS kotasına dayanma.

İçerik üretiminde Claude'un yaratıcı/araştırma işi ile programların zamanlanabilir işi arasındaki farkı koru. GitHub cron veya VPS zamanlayıcısının tek başına Claude'u süresiz ve ücretsiz çalıştırdığını iddia etme. Oturum kapandığında çalışacak bileşenleri ve yeni Claude oturumu gerektiren işleri ayrı belgele. Gelecekteki içerik için tamamlanmış senaryo ve üretim işlerinden oluşan bir tampon hazırla.

Hazırlık tamamlandığında `READY_FOR_VPS` raporu ver ve GitHub'da kal. VPS geçişini kendiliğinden başlatma; kullanıcı bu geçişi istediğinde mevcut repodan devam et. Bu aşama sınırını kategori veya video onayı istemek için kullanma.

## 5. Araştır ve tek bir kanal seç

En az beş uygulanabilir nişi karşılaştır. Talep, rekabet, yeni kanalların erişilebilir performansı, özgün değer üretme imkânı, ücretsiz üretim kalitesi, telif, reklam uygunluğu, otomasyon, CPU maliyeti ve 30 günlük büyüme potansiyelini değerlendir. Türkçe ve İngilizce seçeneklerini araştır; dili gerekçeli olarak seç.

Rakip kanal örneklerini URL ve gözlem tarihiyle kaydet. Kamuya açık olmayan izleyici tutma, CTR veya gelir verilerini biliyormuş gibi yazma. RPM/gelir iddialarını doğrulanmadıkça tahmin olarak etiketle. Yalnızca viral örnekleri seçerek sonuç çıkarma. Erişim engeli varsa bulguyu uydurma; alternatif kamuya açık kanıt kullan.

Tek bir ana niş ve kanal vaadi seç. Neden kazanabileceğini, neyi farklı sunduğunu ve ücretsiz araçlarla nasıl kaliteli üretileceğini açıkla. 30 günlük takvim ve ilk içerik kuyruğunu oluştur. Video sürelerini ve yayın sıklığını araştırma, ölçülmüş render süresi ve içerik değerine göre belirle; rastgele sabit sayı dayatma.

## 6. Uçtan uca üretim

Her video için şu zinciri kendin tamamla:

Konu araştırması → kaynak kontrolü → özgün senaryo → sahne planı → görsel/animasyon üretimi → gerekiyorsa seslendirme → ses temizleme/miks → kurgu/render → altyazı → thumbnail → başlık/açıklama → kalite kontrol → yükleme paketi.

Format uygunsa özgün kod görselleştirmesi, simülasyon, açıklayıcı animasyon, programatik ekran kaydı veya kaynaklı veri anlatımı kullan. Yalnızca stok görseller üzerine monoton TTS ekleyip birbirinin aynı videolar üretme. Her bölüm kendi araştırmasını, anlatısını ve özgün değerini taşımalı. Aynı marka şablonu kullanılabilir; videonun esas içeriği anlamlı biçimde değişmeli.

Kanal adı ve handle alternatifleri, logo, banner, profil görseli, kanal açıklaması, playlist yapısı ve yayın ayarlarını hazırla. Thumbnail'ı kendin üret; mobil okunabilirliği kontrol et. İçerikte karşılığı olmayan vaat, yanıltıcı görsel ve sahte olay kullanma. Başlık/thumbnail alternatiflerini hazırla, ilk yayına çıkacak olanı kendin seç.

Her yükleme paketi şunları içersin: final MP4, thumbnail, SRT/VTT, başlık, açıklama, kaynak/atıflar, gerekiyorsa bölümler, playlist, yayın tarihi/saat dilimi, hedef kitle ve sentetik içerik beyanı için gerekçeli ayar, lisans kaydı ve kalite raporu. Kullanıcının yüklemesi için tek kısa kontrol listesi üret. Tekrarlayan yüklemeleri kolaylaştıracak yayın kuyruğu ve durum takibi kur.

## 7. İçerik güvenilirliği ve kalite

Telifli film/TV/spor kliplerini, başka kanalların videolarını, senaryolarını veya thumbnail'larını kopyalama. Her dış varlık için kaynak URL'si, lisans, edinme tarihi, atıf ve ticari kullanım kanıtı tut. Lisansı belirsiz varlığı kullanma. Gerçek kişi sesini/yüzünü izinsiz taklit etme. Gerçekçi sentetik içerikte gerekli YouTube beyanını hazırla.

YouTube'un özgünlük, tekrar/seri üretim, reused content, reklam uygunluğu, spam ve sahte etkileşim kurallarını araştır ve üretim kapısına uygula. Bot izlenme, abone satın alma, karşılıklı abone ağları, kendi videolarını otomatik izletme ve yanıltıcı trafik kullanma. Hedefi bu yollarla kovalamak yasaktır.

Yayın paketine geçmeden önce anlam, kaynak doğruluğu, ses anlaşılabilirliği, telaffuz, altyazı eşleşmesi, taşan metin, görsel süreklilik, siyah/donuk kare, codec ve dosya bütünlüğünü kontrol et. Otomatik kontrolleri gerçek kare örnekleri ve ses/video incelemesiyle destekle; görmediğin veya dinlemediğin medyayı incelenmiş sayma. Kaliteyi değerlendiremiyorsan bunu kaydet ve değerlendirebildiğin bir üretim yolu kur. Sorunu kendin düzelt; kullanıcıya kurgu veya inceleme görevi verme.

## 8. Ölçüm ve işletim

Ücretsiz ve izin verilen yollarla gerçek performans verisine erişim imkânını araştır. OAuth gerekiyorsa yalnızca mevcut kanal açma/yükleme adımına sığan yetkilendirmeyi tarif et; Google parolasını veya tokenları sohbete/Git'e isteme. Özel analytics erişimi yoksa CTR ve izleyici tutmayı uydurma; kamuya açık verilerle sınırı belirt. Kullanıcıdan her gün screenshot veya CSV isteme.

Ulaşılabilen verilere göre gösterim, CTR, izlenme, ortalama izleme süresi, izleyici tutma, abone kazanımı ve geçerli YPP ilerlemesini ayrı izle. Studio'nun YPP sayacını normal görüntüleme sayısıyla eşitleme. 3, 7, 14, 21 ve 30. günlerde plan/gerçek farkını ve sonraki içerik değişikliklerini kaydet. Küçük örneklemde erken kesin sonuç verme; gerekçesiz sürekli niş değiştirme.

30. gün hedef gerçekleşmezse başarısızlığı gizleme. Gerçek durumu, eksik eşikleri, üretim/büyüme darboğazlarını ve aynı ücretsiz sınırlar içinde sonraki adımları raporla. YouTube kabulünü veya geliri kanıt olmadan ilan etme.

## 9. Repo ve çalışma disiplini

İlk oturumda mevcut repoyu oku; var olan işleri silme. Ardından en az şu yapıyı oluştur:

- `CLAUDE.md`: görev, sınırlar, çalışma ve oturum devam kuralları.
- `README.md`: projenin amacı ve tek komutla örnek üretim.
- `docs/MASTER_PLAN.md`: kanonik plan ve aşamalar.
- `docs/STATUS.md`, `docs/DECISIONS.md`, `docs/HANDOFF.md`: durum, kararlar, sonraki iş.
- `docs/research/`: tarihli kaynaklar, niş ve araç karşılaştırmaları.
- `docs/policies/`: YouTube koşulları ve uygulama kontrolleri.
- `docs/operations/`: yayın, ölçüm, kurtarma ve gelecekteki VPS kurulum rehberi.
- `channel/`: marka ve kanal kurulum paketi.
- `content/`: konu kuyruğu, senaryolar, sahne planları ve lisans kayıtları.
- `src/`, `scripts/`, `tests/`: üretim sistemi ve anlamlı doğrulamalar.
- `reports/`: pilot, günlük ilerleme, maliyet/kota ve dönem raporları.

Sırlar, OAuth dosyaları ve kişisel bilgiler Git'e girmesin. `.env.example` yalnızca boş örneklerden oluşsun. Token içeriğini loglama. Versiyonları ve model indirme kontrollerini sabitle; lisans kayıtlarını tut. Tekrar çalıştırma aynı işi kontrolsüz çoğaltmasın; iş kimliği, checkpoint, sınırlı retry ve hata kaydı kullan. Küçük commitler yap; ana dal çalışır kalsın. Oturum sonunda commit/push durumu ve devam talimatı kaydet; uzaktan commit'i doğrulayamıyorsan bunu belirt.

Gerekli yerlerde alt ajanları araştırma, uygulama, test ve bağımsız inceleme için kullan. Ana oturum koordinatör ve son karar sorumlusudur. Alt ajanlar ücretli araç kullanamaz, kapsamı genişletemez, VPS'e geçemez veya kullanıcı müdahalesi gerektiren dış işlemleri bağımsız yapamaz. Bulguları entegre et; gereksiz paralel çağrılarla mevcut Claude kotasını tüketme.

## 10. GitHub hazırlığının bitiş ölçütleri

Sadece doküman üretmek yeterli değildir. `READY_FOR_VPS` demeden önce:

1. Güncel kaynaklı araştırma, seçilmiş niş/dil, marka ve 30 günlük yayın planı tamamlanmış olsun.
2. Seçilen ücretsiz araçların ticari kullanım ve teknik uygunluğu doğrulanmış olsun.
3. Gerçek bir pilot video uçtan uca üretilmiş ve incelenmiş olsun; pipeline aynı biçimde ikinci farklı konuda da başarılı çalışsın. Seçilen strateji Shorts içeriyorsa onun yolu da gerçek çıktıyla doğrulansın.
4. İlk hafta yayın paketleri tamamlanmış olsun; planlanan içeriklerin yerine placeholder dosya koyma.
5. Gerçek CPU/RAM/disk, render süresi, dosya boyutu ve GitHub kota kullanımını ölç; VPS gereksinimlerini bu kanıtlardan çıkar. VPS'te denenmemiş bir kurulumu test edilmiş gibi sunma.
6. Temiz proje çalışma dizininden belgelenmiş tek komutla pilot yeniden üretilebilsin; hata durumları ve devam mekanizması kontrol edilmiş olsun.
7. Büyük çıktılar kullanıcıya erişilebilir, ücretsiz ve yeterince kalıcı bir teslim yoluyla hazır olsun; repo içinde manifest ve checksum bulunsun.
8. Kanal açma/yükleme paketleri, kalan hesap sahibi zorunlulukları, analytics sınırları, ücretsiz çalışma sınırları ve VPS geçiş rehberi hazır olsun.

GitHub ortamındaki gerçek engel nedeniyle bu ölçütlerden biri tamamlanamıyorsa hazır ilan etme. Engeli kanıtla, ücretsiz alternatifleri dene ve GitHub'da tamamlayabildiğin işlere devam et. Sırf engeli atlamak için VPS'e erken geçme.

## 11. Şimdi başla

Bu talimatı kabul ettiğini söyleyip durma. Önce ortam/repo yeteneklerini ve güncel politikaları incele; niş ve araç araştırmasını yap; seçimlerini kaydet; sistemi kur; pilotları üret; ilk hafta paketlerini tamamla. Rutin kararlar için onay isteme. Planlama aşamasında takılı kalma.

Her oturumun sonunda kısa bir rapor ver: durum, tamamlanan somut çıktılar, doğrulama kanıtı, gerçek engeller, sonraki adım, commit ve push durumu. Kullanıcıdan yardım ancak yukarıdaki izinli kanal açma/yükleme adımında gerekli olduğunda istenebilir. Bunun dışındaki engellerde izin varmış gibi davranmadan bağımsız işleri sürdür.

GitHub hazırlığı tamamlanınca son durum: `READY_FOR_VPS / GITHUB PREPARATION COMPLETE`. Ardından VPS geçişi talimatını bekle.

---

## Başlangıçta yeniden doğrulanacak resmî kaynaklar

- YPP uygunluk ve inceleme: https://support.google.com/youtube/answer/72851
- Genişletilmiş YPP: https://support.google.com/youtube/answer/13429240
- Kanal para kazanma politikaları: https://support.google.com/youtube/answer/1311392
- Sentetik içerik beyanı: https://support.google.com/youtube/answer/14328491

Bu bağlantılar araştırmaya başlangıçtır. Güncel sürümleri ve ilgili diğer resmî GitHub/araç belgelerini çalışmaya başladığında doğrula.
