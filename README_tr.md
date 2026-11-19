<div align="center">

<a href="https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=banner&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/images/banner.png" alt="Awesome Gemini 4 Hydrogen guide and use cases banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![View Hydrogen in your browser](https://img.shields.io/badge/View_Hydrogen-Browser-4285f4)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_try)
[![Gemini Native API via the Hydrogen model page](https://img.shields.io/badge/Gemini_Native_API-Model_Page-f22f3d)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=badge&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-577590)](README_ru.md)

</div>

# Seçilmiş Gemini 4 Hydrogen Rehberi ve Kullanım Örnekleri

## 🍌 Giriş

Kaynaklarla desteklenen uygulamalar, kodlama iş akışları ve pratik karşılaştırmalar üzerinden Gemini 4 Hydrogen'ı keşfedin.

**225 örnek, Hydrogen’in nasıl kullanıldığını ve sonuçların hangi noktalarda yetersiz kaldığını gösteriyor.**

Her örnek kaynağına bağlantı verir ve yazarını belirtir. Demolar, sağlayıcı örnekleri ve üretici karşılaştırmaları notlarda işaretlenir; eksik istemler yeniden oluşturulmaz.

## 📊 Genel bakış

- Toplam 225 vaka var. 17 Kasım’da 1.304 X gönderisi incelendikten sonra 185 vaka eklendi. Yeni kaynaklar toplandığında 30’dan fazla beğeniye sahipti.
- Beş kategori; ajanları, öğrenme ve uygulamaları, e-tablolar ve Search'ü, etkileşimli 3B'yi, karşılaştırma ve sınırlamaları kapsar.
- 264 özgün görsel kaynak, önizlemeli 168 oynatılabilir video ve 96 görsel içeriyor.
- Gemini 4 Hydrogen, 12 Kasım 2026'da duyuruldu. Modeli ve mevcut erişim seçeneklerini EvoLink'te keşfedin.

> [!NOTE]
> Aksi belirtilmedikçe model atıfları, maliyetler, süreler ve sonuçlar kaynakların iddialarıdır. Video incelemesinde tam işlevsel testler değil, örneklenmiş kareler kullanılmıştır. Kodlanmış uygulamaların kayıtları, yerel video üretiminin kanıtı değildir. Farklı çalıştırma ortamları, akıl yürütme seviyeleri veya yineleme sayıları nedeniyle karşılaştırmalar kontrollü değildir.

**Resmî kaynaklar: [Google duyurusu](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Google DeepMind model kartı](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)**

**Buradan başlayın: [Hydrogen'ı EvoLink'te keşfedin](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=readme&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=landing_overview) · [API anahtarı alın (model sayfası üzerinden)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=overview&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)**

<a id="quick-start"></a>
## ⚡ Hızlı başlangıç

EvoLink'te başlayın; Hydrogen'ı bir uygulamaya entegre etmek istediğinizde Gemini yerel API'sini kullanın.

1. [Gemini 4 Hydrogen’ı tarayıcıda görüntüleyin](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=browser_try)
2. [EvoLink API anahtarı oluşturun veya yönetin (model sayfası üzerinden)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_api_key)

Asgari yerel API isteği

```bash
export EVOLINK_API_KEY="your_api_key_here"

curl --fail-with-body --silent --show-error \
  --request POST \
  --url "https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent" \
  --header "Authorization: Bearer $EVOLINK_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{"contents":[{"role":"user","parts":[{"text":"Reply exactly: OK"}]}],"generationConfig":{"candidateCount":1,"maxOutputTokens":2048,"temperature":0,"thinkingConfig":{"thinkingLevel":"low"}}}'
```

`POST https://direct.evolink.ai/v1beta/models/gemini-4-hydrogen:generateContent`

[Gemini Yerel API hızlı başlangıç rehberini okuyun (İngilizce) (model sayfası üzerinden)](https://evolink.ai/gemini-4-hydrogen?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-gemini-4-hydrogen-guide-and-use-cases&utm_content=model_for_docs)

> [!TIP]
> Üretilen metni yanıtın candidates[].content.parts[].text alanlarından okuyun.

> [!IMPORTANT]
> API anahtarınızı bir ortam değişkeninde tutun ve asla depoya işlemeyin. Akış, akıl yürütme ve diğer istek seçenekleri için API belgelerine bakın.

## 📑 Menü

| Bölüm | Örnekler |
|---|---|
| [⚡ Ajanlar ve kodlama iş akışları](#agents) | 30 |
| [💻 Uygulamalar ve öğrenme](#apps-learning) | 37 |
| [📊 E-tablolar ve Search](#data-search) | 9 |
| [🎮 Etkileşimli 3B ve arayüzler](#interactive-3d) | 48 |
| [🧪 Karşılaştırmalar ve sınırlamalar](#comparisons-limits) | 101 |
| [İlgili depolar](#related-repositories) |  |
| [Hızlı başlangıç](#quick-start) |  |
| [Teşekkürler](#acknowledge) |  |

| Örnek | Kategori | Denenecekler | Tür |
|---|---|---|---|
| [Antigravity'de kod tabanı bakımı](#case-1) | Ajanlar ve kodlama iş akışları | Düzenlemeleri, araç kullanımını ve doğrulamayı birlikte değerlendirmek için sınırları belirli bir bakım görevi kullanın. | Demo |
| [Paralel çalışan on altı canvas uygulaması](#case-2) | Ajanlar ve kodlama iş akışları | Geliştirmeyi bağımsız modüllere ayırın; planlama, uygulama ve kalite kontrol rollerini açıkça belirleyin. | Demo |
| [Çok modelli bir sürüyle kızıl güve](#case-3) | Ajanlar ve kodlama iş akışları | Etkileşimli bir yaratıcı kodlama projesinde orkestrasyon ve uygulama rollerini ayırın. | Demo |
| [3D Medic ile inceleme ve onarım](#case-4) | Ajanlar ve kodlama iş akışları | Bir 3B dosyayı inceleyen, hataları bulan ve dışa aktarmadan önce onarım öneren bir ajanı keşfedin. | Demo |
| [Devin'de oluşturulmuş bir yelkenli sahnesi](#case-5) | Ajanlar ve kodlama iş akışları | Modeli gerçekten kullanmayı planladığınız kodlama ajanı ortamında değerlendirin. | Demo |
| [Lingo City'de dil pratiği](#case-6) | Uygulamalar ve öğrenme | Bağlama dayalı dil pratiği için çalışma kartlarını etkileşimli bir sokak sahnesiyle birleştirin. | Demo |
| [3B kâğıt tiyatrosu olarak Romeo ve Juliet](#case-7) | Uygulamalar ve öğrenme | Belirli bir dersi, net bir öğrenme hedefi olan etkileşimli bir sahneye dönüştürün. | Demo |
| [Tasarım görselinden okuma sitesine](#case-8) | Uygulamalar ve öğrenme | Görsel anlayışı ve çalışan ön yüz uygulamasını değerlendirmek için bir referans tasarım kullanın. | Demo |
| [Yirmi modülde oluşturulmuş koi bahçesi](#case-9) | Uygulamalar ve öğrenme | Tek bir istemden eksiksiz sonuç beklemek yerine büyük bir sahneyi küçük modüllerle oluşturun. | Demo |
| [Proton füzyonunu öğreten bir oyun](#case-10) | Uygulamalar ve öğrenme | Bilimsel bir sürecin etkileşimli açıklamasını prototipleyin, ardından temelindeki bilimi kontrol edin. | Demo |
| [Google Sheets'te hareketli manzara](#case-11) | E-tablolar ve Search | Üretilen kodu ve hücre düzeyindeki güncellemeleri incelemek için alışılmadık bir e-tablo animasyonu kullanın. | Demo |
| [Folio etkileşimli veri sitesi](#case-12) | E-tablolar ve Search | Küçük bir web prototipinde tanıtım sayfası düzenini etkileşimli veri görselleştirmeleriyle birleştirin. | Demo |
| [Çok parçalı arama sorularına görsel yanıtlar](#case-13) | E-tablolar ve Search | Çok sayıda koşul içeren ayrıntılı bir arama isteğini test ederken yanıt düzenini ve kaynak bağlantılarını karşılaştırın. | Demo |
| [Sheets'te etkileşimli finansal tahmin](#case-14) | E-tablolar ve Search | Varsayımları görünür bir finansal model prototipi oluşturun ve üretilen formülleri ve grafikleri inceleyin. | Demo |
| [Etkileşimli bir yemek odası](#case-15) | Etkileşimli 3B ve arayüzler | Bir sahneyi sabit görselden değerlendirmek yerine nesne etkileşimlerini, aydınlatmayı ve durum değişikliklerini kontrol edin. | Demo |
| [Minyatür dünyalı bir ses kaydırıcısı](#case-16) | Etkileşimli 3B ve arayüzler | Hem etkileşim tasarımını hem de hareketli sahnenin ayrıntılarını test etmek için tanıdık bir kontrol kullanın. | Demo |
| [Three.js ile bir Japon evi](#case-17) | Etkileşimli 3B ve arayüzler | Ayrıntılı bir 3B gezintiyi değerlendirirken kod üretimini görüntüleme süresinden ayırın. | Demo |
| [3B bisiklet süren pelikan](#case-18) | Etkileşimli 3B ve arayüzler | Koordinasyonu, hareketi ve sahne tutarlılığını incelemek için hareketli bir karakter kullanın. | Demo |
| [Önce planlanan bir gezegen simülatörü](#case-19) | Etkileşimli 3B ve arayüzler | Karmaşık bir sahneyi düzenlemesini istemeden önce kodlama modeline somut bir plan verin. | Demo |
| [Antigravity Swarm ile liman adası](#case-20) | Etkileşimli 3B ve arayüzler | Çok ajanlı sahne oluşturma davranışını incelemek için gezilebilir küçük bir ortam kullanın. | Demo |
| [Eyfel Kuleli yüzen ada](#case-21) | Etkileşimli 3B ve arayüzler | Kompakt bir anıt sahnesinde kompozisyonu, kamera hareketini ve modelin ürettiği kodu değerlendirin. | Demo |
| [Uçarak gezilebilen fütüristik şehir](#case-22) | Etkileşimli 3B ve arayüzler | İlk çıktının nihai olduğunu varsaymak yerine prosedürel bir dünyada sonraki düzenlemeleri test edin. | Demo |
| [Gün doğumundan geceye bir deniz uçağı](#case-23) | Etkileşimli 3B ve arayüzler | Etkileşimli bir 3B sahnede ortam kontrollerini ve ışık geçişlerini inceleyin. | Demo |
| [Neon çöp adam animasyonu: Hydrogen ve Opus](#case-24) | Karşılaştırmalar ve sınırlamalar | Aynı çalıştırma ortamlarını varsaymadan tamamlanmış animasyonu bildirilen süre ve maliyetle birlikte karşılaştırın. | Evaluation |
| [Robotik görevler ve fark edilen hatalar](#case-25) | Karşılaştırmalar ve sınırlamalar | Robotik değerlendirmeye görev tamamlamayı ve küçük hataları fark etmeyi dahil edin. | Evaluation |
| [Doğal dille yönetilen laboratuvar çalışma hücresi](#case-26) | Karşılaştırmalar ve sınırlamalar | Araç çalıştırmayı ve hata yönetimini, öne çıkan kıyaslama puanlarından ayrı değerlendirin. | Evaluation |
| [Buzdağı ve römorkör: Hydrogen ve Carbon](#case-27) | Karşılaştırmalar ve sınırlamalar | Uzun bir 3B geliştirmeyi karşılaştırırken akıl yürütme seviyesini ve çalıştırma ortamının kısıtlarını kaydedin. | Evaluation |
| [Jöle koi göleti: Hydrogen ve Sonnet](#case-28) | Karşılaştırmalar ve sınırlamalar | Bir kıyaslama sıralamasını model tercihine dönüştürmeden önce somut bir sahneyi inceleyin. | Evaluation |
| [Ortak istemli yaratıcı kodlama koleksiyonu](#case-29) | Karşılaştırmalar ve sınırlamalar | Tek bir çekici çıktıdan aşırı genelleme yapmamak için çeşitli görsel görevler kullanın. | Evaluation |
| [Megamind vokselleri: maliyet ve kalite için bir karşı örnek](#case-30) | Karşılaştırmalar ve sınırlamalar | Bir modelin sürekli daha ucuz veya görsel açıdan daha güçlü olup olmadığını değerlendirirken başarısız örnekleri koruyun. | Limit |
| [Dört mevsimde jonglör aslan](#case-31) | Karşılaştırmalar ve sınırlamalar | Yalnızca çevredeki arayüzün görsel kalitesini değil, istenen hareketi kontrol edin. | Limit |
| [Üç modelli çöp adam dövüşü: daha yavaş, daha pahalı sonuç](#case-32) | Karşılaştırmalar ve sınırlamalar | Bir modelin tanıtılan verimliliğini gerçek görev raporlarıyla karşılaştırırken karşı örnekleri koruyun. | Limit |
| [Çiftlikte bisiklet sahnesi: Hydrogen ve Flash](#case-33) | Karşılaştırmalar ve sınırlamalar | Hareketi ve sahne kalitesini, üreticinin bildirdiği tamamlanma süresiyle birlikte karşılaştırın. | Evaluation |
| [Tandem bisikletlerde bir kız ve kedi](#case-34) | Karşılaştırmalar ve sınırlamalar | Farklı kodlama ortamlarını görünür tutarak isteme bağlılığı ve ek ayrıntıları karşılaştırın. | Evaluation |
| [Dört model Three.js ile Mario oyunu oluşturuyor](#case-35) | Karşılaştırmalar ve sınırlamalar | Aynı istemle üretilen oyunları karşılaştırmadan önce eşit olmayan akıl yürütme ayarlarını kaydedin. | Evaluation |
| [Üç Gemini modeli oyun kumandası çiziyor](#case-36) | Karşılaştırmalar ve sınırlamalar | Aile içinde bir hiyerarşi varsaymak yerine göreve özgü gerileme ve iyileşmelere bakın. | Evaluation |
| [Uygulama ve Studio'da farklı görsel yanıtlar](#case-37) | Karşılaştırmalar ve sınırlamalar | Bir görsel sonucuna güvenmeden önce aynı görüntüyü kullanmayı planladığınız üründe test edin. | Limit |
| [Roket fırlatma sahnesi: Hydrogen ve Flash](#case-38) | Karşılaştırmalar ve sınırlamalar | Bildirilen geliştirme süresinin yanı sıra gerçek fırlatma animasyonunu da karşılaştırın. | Evaluation |
| [Dört SVG animasyon görevi](#case-39) | Karşılaştırmalar ve sınırlamalar | Görevler arası tutarlılığı incelemek için birden fazla etkileşim ve animasyon motifi kullanın. | Evaluation |
| [Üç model savanada bir atı canlandırıyor](#case-40) | Karşılaştırmalar ve sınırlamalar | Genel maliyet veya kalite iddialarını kabul etmeden önce hareketi ve görsel ayrıntıyı doğrudan inceleyin. | Evaluation |
| [Uzay Görsellerinden HTML Sahnesine](#case-41) | Etkileşimli 3B ve arayüzler | Az sayıda referansla, oluşturulan sahnenin ayırt edilebilir bir görsel üslup taşıyıp taşımadığını sınayın. | Demo |
| [Gemini Canvas'ta Formula 1 Prototipi](#case-42) | Etkileşimli 3B ve arayüzler | Üretilen araç modelini farklı açılardan incelemek için birkaç kamera görünümü ekleyin. | Demo |
| [API'de Hydrogen ve Antigravity'de Carbon](#case-43) | Karşılaştırmalar ve sınırlamalar | Aynı istemden çıkan görselleri karşılaştırırken her çalıştırmanın ortamını kaydedin. | Evaluation |
| [Hydrogen ve Astra Karşılaştırmasında Gölge Ayrıntısı](#case-44) | Karşılaştırmalar ve sınırlamalar | Küçük görüntü ayrıntılarını iki çalıştırmanın maliyeti ve süresiyle birlikte değerlendirin. | Evaluation |
| [Prosedürel 3B Hareket Karşılaştırması](#case-45) | Karşılaştırmalar ve sınırlamalar | Prosedürel bir animasyonda akıcılık ve kompozisyonu karşılaştırırken üretim süresini kaydedin. | Evaluation |
| [PokéBench'te 89 Dakikalık Görsel Test](#case-46) | Karşılaştırmalar ve sınırlamalar | Uzun bir görsel ajan testinde görev sonucuyla birlikte hamleleri ve API hatalarını kaydedin. | Benchmark |
| [Hydrogen ve DeepSeek Aynı 3B Sahneyi Kuruyor](#case-47) | Karşılaştırmalar ve sınırlamalar | Görsel çıktıları karşılaştırırken süreyi ve API ücretini ayrı ayrı kaydedin. | Evaluation |
| [SVG Olarak BMW Yan Profili](#case-48) | Etkileşimli 3B ve arayüzler | Oranları, silüeti ve küçük ayrıntıları bir aracın SVG yan görünümünden inceleyin. | Demo |
| [Bir Gökbilimcinin Yüzen Adası](#case-49) | Etkileşimli 3B ve arayüzler | Küçük bir sahneye belirgin bir tema verip nesnelerin ve ışığın bunu nasıl desteklediğini inceleyin. | Demo |
| [Referans Görselden Gezilebilir 3B Manzaraya](#case-50) | Etkileşimli 3B ve arayüzler | Görselden oluşturulan sahnenin hem referansa sadakatini hem de hareket olanağını sınayın. | Demo |
| [3B Bloklardan Minyatür Diorama](#case-51) | Etkileşimli 3B ve arayüzler | Bloklarla kurulan bir minyatürde şekillerin bütünlüklü bir sahne oluşturup oluşturmadığına bakın. | Demo |
| [Etkileşimli Kiraz Çiçeği Ağacı](#case-52) | Etkileşimli 3B ve arayüzler | Tek bir hareketli nesne ve birkaç denetimle küçük bir sahnedeki anlık değişiklikleri keşfedin. | Demo |
| [Agent Arena'da Görev Başına Süre ve Maliyet](#case-53) | Karşılaştırmalar ve sınırlamalar | Toplam başarıyla birlikte görev başına gecikmeyi, maliyeti ve çıktı token'larını inceleyin. | Benchmark |
| [Görsel Belge ve Terminal Kıyaslamaları](#case-54) | Karşılaştırmalar ve sınırlamalar | Akıl yürütme bütçesi seçerken belge ve terminal sonuçlarını ayrı değerlendirin. | Benchmark |
| [Vals Index ve Tax Agent Sonuçları](#case-55) | Karşılaştırmalar ve sınırlamalar | Uzmanlık gerektiren bir görevin puanını genel değerlendirmeyle birlikte inceleyin. | Benchmark |
| [CursorBench'te Varsayılan Ayarla Hydrogen](#case-56) | Karşılaştırmalar ve sınırlamalar | Varsayılan ayardaki puanı kendi deponuzda yapacağınız testler için başlangıç noktası olarak kullanın. | Benchmark |
| [Dört Modelle Okçu Savaşı Animasyonu](#case-57) | Karşılaştırmalar ve sınırlamalar | Her animasyonun savaşçıların hareketlerini ne kadar anlaşılır aktardığını karşılaştırın. | Evaluation |
| [On Beş Dakikada Minecraft Tarzı Prototip](#case-58) | Uygulamalar ve öğrenme | Bir voksel oyununda kazma ve envanter gibi sistemlerin uyumunu sınayın. | Demo |
| [n8n'de Hydrogen ile Araç Kullanımı](#case-59) | Ajanlar ve kodlama iş akışları | n8n'deki araç çağrısı döngülerini Hydrogen'a atayıp planlamayı ayrı bir adımda yürütün. | Integration |
| [Box Agent ile Karmaşık Kurumsal Belgeler](#case-60) | E-tablolar ve Search | Gerçekçi bir belge iş yükünde doğruluk, çalışma süresi ve token kullanımını kontrol edin. | Benchmark |
| [Devin FrontierCode'da Hydrogen](#case-61) | Karşılaştırmalar ve sınırlamalar | Yamaların birleştirmeye uygunluğunu karşılaştırıp ajan test ortamını kaydedin. | Benchmark |
| [Küçük Bir Etkileşimli Animasyonda Kırılma](#case-62) | Etkileşimli 3B ve arayüzler | Sahneyi büyütmeden önce optik bir etkiyi kısa önizlemelerle iyileştirin. | Demo |
| [Yokuş Yukarı Akan Nehir](#case-63) | Etkileşimli 3B ve arayüzler | Alışılmadık bir hareket yönüyle küçük bir sahne kurup görsel etkiyi inceleyin. | Demo |
| [Açık Talimata Rağmen Web Araması](#case-64) | Karşılaştırmalar ve sınırlamalar | Tarama yapmadan yanıt gerektiren bir iş akışında araçların çağrılıp çağrılmadığını kontrol edin. | Limit |
| [Antigravity Swarm'da Kota Takibi](#case-65) | Karşılaştırmalar ve sınırlamalar | Çok ajanlı bir çalıştırmada toplam token sayısını ve tüketilen kotayı kaydedin. | Evaluation |
| [Mesleki Görev Testlerinde Araç Çağrıları](#case-66) | Karşılaştırmalar ve sınırlamalar | Bir ajanın mesleki görevi yerine getirmeden önce bağlamı nasıl topladığını inceleyin. | Benchmark |
| [Hydrogen ile 3B Portre](#case-67) | Etkileşimli 3B ve arayüzler | Üç boyutlu bir gösterimde kişinin tanınabilirliğini portreyle sınayın. | Demo |
| [Dört Model Bir Büyücü ve Ejderhayı Canlandırıyor](#case-68) | Karşılaştırmalar ve sınırlamalar | Aynı fantastik sahnenin farklı sürümlerinde düzeni, hareketlerin anlaşılırlığını ve efektleri karşılaştırın. | Evaluation |
| [Çok Ajanlı Kurulumda Kimlik Doğrulama](#case-69) | Ajanlar ve kodlama iş akışları | Ajan başka bir sağlayıcıya iş aktardığında kimlik doğrulamasını hangi istemcinin yaptığını kontrol edin. | Limit |
| [Antigravity'de Goal Mode Çalıştırması](#case-70) | Ajanlar ve kodlama iş akışları | Uzun bir kodlama oturumunda planı, kod değişikliklerini ve test sonuçlarını izleyin. | Demo |
| [MazeBench'te Düşük Başarı Oranları](#case-71) | Karşılaştırmalar ve sınırlamalar | Uzamsal akıl yürütmeye güvenmeden önce labirent görevleriyle sınayın. | Benchmark |
| [Üç Gemini Modeli Yelkenli Sahnesi Kuruyor](#case-72) | Karşılaştırmalar ve sınırlamalar | Temalı bir Three.js sahnesinde hareket ve çevre ayrıntılarını karşılaştırın. | Evaluation |
| [Antigravity Orchestrator'da Carbon ve Hydrogen](#case-73) | Ajanlar ve kodlama iş akışları | Daha hızlı uygulama modeli takıldığında planlama modelinin devreye girmesini sağlayın. | Integration |
| [Workspace Verilerinden Grafik ve Rapor](#case-74) | E-tablolar ve Search | Eksik analiz, grafik veya rapor çıktısını bir takip isteminin tamamlayıp tamamlamadığını kontrol edin. | Demo |
| [Forma Numarası Okurken Tükenen Bütçe](#case-75) | Karşılaştırmalar ve sınırlamalar | Küçük bir görsel ayrıntıyı okumak için çaba sınırı ve alternatif yöntem belirleyin. | Limit |
| [Model Ailelerinin ClutterBench Performansı](#case-76) | Karşılaştırmalar ve sınırlamalar | Bir model ailesinin genel güçlü yanlarının karmaşık sahnelere yansıyıp yansımadığını test edin. | Benchmark |
| [Haber Özetinden Anlatımlı Klibe](#case-77) | Uygulamalar ve öğrenme | Araştırılmış bir haber özetinden kısa bir anlatımlı video hazırlayıp kullanılan olguları kontrol edin. | Demo |
| [Minecraft Tarzı Anatomik Kesit Büstü](#case-78) | Karşılaştırmalar ve sınırlamalar | Oluşturulan kesitte istenen iç yapıların yer alıp almadığını kontrol edin. | Evaluation |
| [Üç Model Aynı Sahne Nesnesini Üretiyor](#case-79) | Karşılaştırmalar ve sınırlamalar | Bir testte daha ucuz model daha çok token kullanabildiğinde kaliteyi ve token sayısını ayrı izleyin. | Evaluation |
| [Tümevarım Testi ve Token Tüketimi](#case-80) | Karşılaştırmalar ve sınırlamalar | Zor görevlerde akıl yürütme puanıyla birlikte faturalanan giriş ve çıkış token'larını izleyin. | Benchmark |
| [Google E-Tablolar'da Gemini ile Piksel Sanatı](#case-81) | E-tablolar ve Search | Gemini seçeneklerini aynı Google E-Tablolar çizim göreviyle karşılaştırın. | Evaluation |
| [Referans Görselden Daire Maketinin Baskısına](#case-82) | Etkileşimli 3B ve arayüzler | Görselden 3B model üretme testini fiziksel baskıya kadar götürün. | Demo |
| [Üç Modelle 3B Hayvan Animasyonu](#case-83) | Karşılaştırmalar ve sınırlamalar | Aynı 3B hayvan modelleme görevinde anatomiyi ve hareketi inceleyin. | Evaluation |
| [ts-bench'te Hydrogen ve Qwen](#case-84) | Karşılaştırmalar ve sınırlamalar | Genel kıyaslama sonucuyla birlikte araç çağrısı hatalarını inceleyin. | Benchmark |
| [Vending-Bench İşletme Simülasyonu](#case-85) | Karşılaştırmalar ve sınırlamalar | Simüle edilen geliri ajanın işletim maliyetiyle birlikte karşılaştırın. | Benchmark |
| [Golden Merry Gemi Sahnesi](#case-86) | Etkileşimli 3B ve arayüzler | Tanıdık bir kurmaca gemiyle deniz sahnesinin görsel düzenini sınayın. | Demo |
| [OpenClaw'da Hydrogen](#case-87) | Ajanlar ve kodlama iş akışları | Kullanmayı düşündüğünüz ajan çerçevesinde model seçimini kontrol edin. | Integration |
| [Bulutların İçinde Hareket Eden Balina](#case-88) | Etkileşimli 3B ve arayüzler | Kodla üretilen bir hayvan sahnesinde akıcı hareketi ve göz tasarımını ayrı değerlendirin. | Demo |
| [Dört Model Minyatür Ada Kuruyor](#case-89) | Karşılaştırmalar ve sınırlamalar | Ada tasarımlarını her ortamın çalışma süresi ve maliyetiyle birlikte karşılaştırın. | Evaluation |
| [Web Kamerasıyla Havada Çizim](#case-90) | Uygulamalar ve öğrenme | Havada çizgiler çizin ve arayüzün hareketleri nasıl takip ettiğine bakın. | Demo |
| [Kodla Üretilen Kumaş Yırtılmalarının Karşılaştırması](#case-91) | Karşılaştırmalar ve sınırlamalar | Aynı animasyon görevinde esneme, yırtılma ve kürkle etkileşimi sınayın. | Evaluation |
| [Gemini Canvas'ta Bir Su Altı Şehri](#case-92) | Etkileşimli 3B ve arayüzler | Küçük bir 3B sahneden başlayıp birkaç turda gezilebilir alanlar ve hareketli canlılar ekleyin. | Demo |
| [Tek Çalıştırmada Web Portalı](#case-93) | Uygulamalar ve öğrenme | Tek tek akışları sınamadan önce ilk arayüzü portal düzeni üzerinden değerlendirin. | Demo |
| [İzlenemeyen Kaynakla Doğruluk Kontrolü](#case-94) | Karşılaştırmalar ve sınırlamalar | Bir ekran görüntüsü hakkındaki yargıya dayanarak hareket etmeden önce incelenebilir kaynak isteyin. | Limit |
| [Cities: Skylines Tarzı Bir Şehir Kurma Oyunu](#case-95) | Uygulamalar ve öğrenme | Bir şehir oyunu prototipi hazırlayıp denetimlerin ve simülasyonların uyumunu inceleyin. | Demo |
| [Hydrogen ve Sol ile 2B Pelikan](#case-96) | Karşılaştırmalar ve sınırlamalar | Aynı basit 2B animasyon görevinde süreyi ve hareket kalitesini karşılaştırın. | Evaluation |
| [Blender MCP ile Taht Salonu](#case-97) | Ajanlar ve kodlama iş akışları | Oluşturulan sahnenin kompozisyonunu Blender MCP ile düzenleyicide inceleyin. | Integration |
| [Dört Modelle Ağda Sallanma Oyunu](#case-98) | Karşılaştırmalar ve sınırlamalar | Aynı tek dosya kısıtıyla oluşturulan oyunlarda hareketi ve denetimleri karşılaştırın. | Evaluation |
| [Three.js ile Gri Tonlu Korsan Gemisi](#case-99) | Etkileşimli 3B ve arayüzler | Three.js sahnesini gri tonla sınırlayıp ışığın geometriyi görünür kılıp kılmadığını sınayın. | Demo |
| [Dört Model Bina Dioraması Oluşturuyor](#case-100) | Karşılaştırmalar ve sınırlamalar | Aynı mimari görevde farklı modellerin çıktısını ve ışık tercihlerini karşılaştırın. | Evaluation |
| [CadXStudio'da Parametrik Masa Lambası](#case-101) | Etkileşimli 3B ve arayüzler | Oluşturulan CAD modelinin parça ölçülerini ve düzenlenebilirliğini inceleyin. | Integration |
| [C++ ile Tapınak Yolu Animasyonu](#case-102) | Etkileşimli 3B ve arayüzler | Modelin web altyapısı olmadan çalışan animasyon yazmasını küçük bir yerel sahneyle sınayın. | Demo |
| [Üç Model Tren Sahnesi Oluşturuyor](#case-103) | Karşılaştırmalar ve sınırlamalar | Bir tren sahnesiyle kullandığınız model ayarlarının sürelerini karşılaştırın. | Evaluation |
| [Extra Ayarında Yağmurlu Chinatown](#case-104) | Karşılaştırmalar ve sınırlamalar | Yoğun bir animasyonda akıl yürütme ayarını seçmeden önce süreyi ölçüp bitmiş sahneyi inceleyin. | Evaluation |
| [30 Modülden Kurulan Kasaba Sahnesi](#case-105) | Etkileşimli 3B ve arayüzler | Sahneyi istemlerle ayrı modüller halinde oluşturup birleşik görünümü inceleyin. | Demo |
| [Üç Model Bir Gezegen Görselleştiricisi Kuruyor](#case-106) | Karşılaştırmalar ve sınırlamalar | Bilimsel bir görsel arayüz için aynı istemi birkaç modelle deneyin. | Evaluation |
| [Dört Model Chrome Dino'yu Yeniden Yapıyor](#case-107) | Karşılaştırmalar ve sınırlamalar | Tanıdık bir oyunun her sürümünün süresini ölçüp oynanabilir sonuçları karşılaştırın. | Evaluation |
| [Yüzen Adada Postane](#case-108) | Etkileşimli 3B ve arayüzler | Küçük bir bina tarif edip malzeme ve ışığın sahneye katkısını inceleyin. | Demo |
| [İki Kodlama Ajanı Farklı Gemiler Yapıyor](#case-109) | Karşılaştırmalar ve sınırlamalar | Seçtiğiniz ortamda ilk kullanılabilir çıktıyı ve düzeltme maliyetini karşılaştırın. | Evaluation |
| [Koi Courtyard'da Su ve Balıklar](#case-110) | Etkileşimli 3B ve arayüzler | Hareketli balıklar içeren sahnede yüzey yansımalarıyla su ışığının tutarlılığını inceleyin. | Demo |
| [Dört Modelle Mancınık ve Katı Cisim Fiziği](#case-111) | Karşılaştırmalar ve sınırlamalar | Aynı görevde oynanabilir fizik prototiplerini karşılaştırıp akıl yürütme ayarlarını kaydedin. | Evaluation |
| [Gemini Uygulamasında Canlı 3B Sahne](#case-112) | Etkileşimli 3B ve arayüzler | Gemini web arayüzünde etkileşimli ışık ve parçacıklar prototipleyin. | Demo |
| [Tarayıcı CAD'inde Beton Mikseri Montajı](#case-113) | Ajanlar ve kodlama iş akışları | Oluşturulan montajı CAD akışında kullanmadan önce parça ağacını ve parçaların uyumunu inceleyin. | Integration |
| [Blender'da Prosedürel Balta Modelleme](#case-114) | Ajanlar ve kodlama iş akışları | Prosedürel bir Blender varlığını referans silüeti ve birkaç düzenleyici görünümüyle inceleyin. | Integration |
| [Tek HTML Dosyasında Pembe 3B Sahne](#case-115) | Etkileşimli 3B ve arayüzler | Harici varlık kullanmadan Three.js sahnesi kurup kompozisyonun anlaşılabilirliğini inceleyin. | Demo |
| [FrontierMemory'de Kalıcı Ajan Belleği](#case-116) | Karşılaştırmalar ve sınırlamalar | Uzun ömürlü ajan belleği için model seçerken puanı ve çalıştırma başına maliyeti karşılaştırın. | Benchmark |
| [Arızalı LiveKit Sesli Ajanında Hydrogen](#case-117) | Karşılaştırmalar ve sınırlamalar | Kontrollü bir araç hatasıyla ajanın desteklenmeyen sonuçlar bildirip bildirmediğini sınayın. | Evaluation |
| [28 Modüllü Ember Isle Projesi](#case-118) | Ajanlar ve kodlama iş akışları | Büyük sahneyi modüllere bölüp her üretimin süresini kaydedin. | Demo |
| [Yalnızca Kodla Büyük Patlama Simülasyonu](#case-119) | Etkileşimli 3B ve arayüzler | Kısa bir animasyonla görsel bir açıklama tasarlayıp bilimsel çerçevesini kontrol edin. | Demo |
| [Patlatılmış Montaj Görünümlü Helikopter](#case-120) | Etkileşimli 3B ve arayüzler | 3B prototipte uçuş denetimlerinin faydalı inceleme görünümleriyle bir araya gelip gelmediğini sınayın. | Demo |
| [Röntgen ve Tel Kafes Görünümlü Hydrogen Express](#case-121) | Etkileşimli 3B ve arayüzler | Denetlenebilir 3B prototipe birden fazla inceleme modu ekleyin. | Demo |
| [Gökyüzünde Yakıt İstasyonu](#case-122) | Etkileşimli 3B ve arayüzler | Davranışını demoda görünür kılmak için sahneye hareketli nesneler ve değişen ışık ekleyin. | Demo |
| [Üç Gemini Modeli Bisikletliyi Canlandırıyor](#case-123) | Karşılaştırmalar ve sınırlamalar | Aynı görevde kısa hareketli sahneleri karşılaştırıp süreleri ayrı kaydedin. | Evaluation |
| [Kimya Kitabından Etkileşimli Derse](#case-124) | Uygulamalar ve öğrenme | İpuçları, sesli anlatım ve isteğe bağlı metinle kendi kendine öğrenme dersi oluşturun. | Demo |
| [Vocaloid Şarkı Prototipi](#case-125) | Uygulamalar ve öğrenme | Tek seferde oluşturulan bestenin karaktere ve müzik tarzına uygunluğunu inceleyin. | Demo |
| [İki Model LEGO Dünyası Kuruyor](#case-126) | Karşılaştırmalar ve sınırlamalar | Her modelin verilen sürede temalı dünyanın ne kadarını oluşturduğunu karşılaştırın. | Evaluation |
| [İki Depoya Ekilen Hataları Onarma](#case-127) | Karşılaştırmalar ve sınırlamalar | Kodlama ajanının hangi hataları bulup düzelttiğini ölçmek için bilinen kusurlar ekleyin. | Benchmark |
| [İki Modelle Çöp Adam ve İmleç](#case-128) | Karşılaştırmalar ve sınırlamalar | İki etkileşimli animasyonun işaretçiye tepkisini karşılaştırın. | Evaluation |
| [Tek HTML Dosyasında Su Değirmeni](#case-129) | Etkileşimli 3B ve arayüzler | Hızlı bir 3B prototipi, hareketi fark edilen nesnelere sahip küçük bir manzarayla sınayın. | Demo |
| [İki Model Dağ Manzarası Oluşturuyor](#case-130) | Karşılaştırmalar ve sınırlamalar | Manzara animasyonunda kompozisyonu, üretim süresini ve maliyeti ayrı karşılaştırın. | Evaluation |
| [Özel Test Ortamında İngilizceden Farsçaya Çeviri](#case-131) | Karşılaştırmalar ve sınırlamalar | Zor bir çeviriyi insan çevirisiyle karşılaştırıp değerlendirin. | Evaluation |
| [Hydrogen Extra ile Blender Sahnesi](#case-132) | Etkileşimli 3B ve arayüzler | Görsel ayrıntıları artırmadan önce Blender'da geometriyi ve malzemeleri denetleyin. | Demo |
| [Dört Model Batan Gemi Sahnesi Kuruyor](#case-133) | Karşılaştırmalar ve sınırlamalar | Aynı sahne testinde görsel sadakati, süreyi ve maliyeti ayrı kaydedin. | Evaluation |
| [Görselden Karmaşık Bir İntegrali Okuma](#case-134) | Uygulamalar ve öğrenme | Uzun ifadeyi sadeleştirmeden önce modelin eşit integral sınırlarını fark edip etmediğini kontrol edin. | Evaluation |
| [Dört Modelle Kör Reklam Metni Karşılaştırması](#case-135) | Karşılaştırmalar ve sınırlamalar | Yazı iş akışında kullanacağınız çıktıyı seçmeden önce model adlarını gizleyin. | Evaluation |
| [Akıl Yürütme Ayarına Göre Görsel Algılama ve Okuma](#case-136) | Karşılaştırmalar ve sınırlamalar | Her akıl yürütme düzeyinde algılama, metin doğruluğu, maliyet ve gecikmeyi ayrı ölçün. | Benchmark |
| [Dört Model Yukarı Bak'taki Evi Yeniden Yapıyor](#case-137) | Karşılaştırmalar ve sınırlamalar | 3B modeller arasındaki farkları aynı referans görseli ve görevle karşılaştırın. | Evaluation |
| [WebGL2 ile İnsan Hücresi Ansiklopedisi](#case-138) | Uygulamalar ve öğrenme | Hücre içindeki uzamsal ilişkileri etkileşimli kesitle anlatın. | Demo |
| [Hydrogen ile İki Parçacık Animasyonu](#case-139) | Etkileşimli 3B ve arayüzler | Basit görsel efektlerde şekil ve hareketi iki farklı parçacık sahnesiyle inceleyin. | Demo |
| [Parking Bench'te Yalnızca Görselle Oynayan Rakip](#case-140) | Uygulamalar ve öğrenme | Bulmaca rakibini tek durum girdisi olarak tahta görüntüsüyle sınayın. | Integration |
| [Google Dokümanlar İçin Videolu Anlatım](#case-141) | Uygulamalar ve öğrenme | Mobil düzenlemeyi ekran görüntüleri ve numaralı işaretlerle anlatın. | Demo |
| [Minyatür Dünyada Gece Gündüz Düğmesi](#case-142) | Etkileşimli 3B ve arayüzler | Arayüz durumları arasındaki geçişin akıcılığını basit bir düğmeyle sınayın. | Demo |
| [65 Modülde Bir Çevre Kurmak](#case-143) | Etkileşimli 3B ve arayüzler | Oluşturulan sahne büyüdükçe yapım süresini ve birleştirme işini izleyin. | Demo |
| [Sabit Kamerayla Dans Klibi](#case-144) | Karşılaştırmalar ve sınırlamalar | Referanslı animasyonun karakter tasarımını, kompozisyonu ve kamera konumunu koruyup korumadığını sınayın. | Evaluation |
| [Başlangıç Testinde Takılan Kodlama Ajanı](#case-145) | Karşılaştırmalar ve sınırlamalar | Düzeltmeyi beklemeden önce başlangıç testinin süresini sınırlayın ve ilerlemeyi kontrol edin. | Limit |
| [MZ-1500 İçin BASIC Ortamı](#case-146) | Uygulamalar ve öğrenme | Retro bir BASIC ortamı prototipleyin ve çevre birimi desteğini ayrı kontrol edin. | Demo |
| [İki Model Etkileşimli Robot Kolu Yapıyor](#case-147) | Karşılaştırmalar ve sınırlamalar | Three.js robot kolunun eklemlerinin kullanıcı girdisine tutarlı tepki verip vermediğini sınayın. | Evaluation |
| [Etkileşimli FAA Yer Durdurma Haritası](#case-148) | E-tablolar ve Search | Operasyon durdurması bitince kuyruğun neden sürdüğünü zaman çizelgesi ve haritayla gösterin. | Demo |
| [Minyatür Pagoda Bahçesi](#case-149) | Etkileşimli 3B ve arayüzler | Minyatürde mimari ile çevre düzenlemesinin uyumunu inceleyin. | Demo |
| [Ayrı Modellerle Planlama, Uygulama ve İnceleme](#case-150) | Ajanlar ve kodlama iş akışları | Planlama, uygulama ve inceleme için ayrı roller tanımlayın ve model başına toplamları karşılaştırın. | Demo |
| [Hydrogen ve Sol ile Kış Köyü](#case-151) | Karşılaştırmalar ve sınırlamalar | Kodlama karşılaştırmasında süre, harcama ve sahne kalitesini ayrı değerlendirin. | Evaluation |
| [High ve Ultra Ayarlarında Three.js Adası](#case-152) | Karşılaştırmalar ve sınırlamalar | Ürünlerin kotalarını ayrı ele alarak görselleri, süreyi ve akıl yürütme düzeyini karşılaştırın. | Evaluation |
| [II. Dünya Savaşı Havaalanı Dioraması](#case-153) | Etkileşimli 3B ve arayüzler | Görünüşün yanı sıra işlevi sınamak için 3B demoya görsel referanslar ve mekanik hareket gereksinimleri verin. | Demo |
| [Kodlama İstemcisinde Hydrogen Kurulumu](#case-154) | Ajanlar ve kodlama iş akışları | Desteklenen bir istemcide Google API anahtarıyla birlikte tam model kimliğini kullanın. | Tutorial |
| [Hydrogen ile SuperARIS Araştırma Ekibi](#case-155) | Ajanlar ve kodlama iş akışları | Çok modelli ajan ekibinde Hydrogen'a belirli araştırma ve metin görevleri atayın. | Integration |
| [Dört Modelle Bir Çekirdek Modülü Baştan Yazmak](#case-156) | Ajanlar ve kodlama iş akışları | Yeniden yazım için ajan seçerken kodu anlama, tasarım ve uygulama becerisini karşılaştırın. | Evaluation |
| [3B PS5 Kumandasında Ayrıntı Karşılaştırması](#case-157) | Karşılaştırmalar ve sınırlamalar | Kumanda modellerinde düğme gölgelerini ve arka donanım ayrıntılarını inceleyin. | Evaluation |
| [Muse İşleri Antigravity CLI'a Aktarıyor](#case-158) | Ajanlar ve kodlama iş akışları | Uzaktaki asistanı yerel kodlama ortamına bağlayın ve varsayılan yazı modelini seçin. | Integration |
| [Farklı Akıl Yürütme Bütçeleriyle CursorBench](#case-159) | Karşılaştırmalar ve sınırlamalar | Hızlı bir varsayılan ayar seçmeden önce farklı akıl yürütme düzeylerinin başarısını karşılaştırın. | Benchmark |
| [Üç Model Yıldız Temalı Tapınak Oluşturuyor](#case-160) | Karşılaştırmalar ve sınırlamalar | 3B görevde görüntü kararlılığını görsel ayrıntıdan ayrı değerlendirin. | Evaluation |
| [Bir Dakikada HTML Nişancı Oyunu](#case-161) | Uygulamalar ve öğrenme | Tek HTML dosyasıyla bir nişancı oyununun temel denetim ve geri bildirim döngüsünü sınayın. | Demo |
| [Mevcut Geçiş Tasarımını Sorgulamak](#case-162) | Karşılaştırmalar ve sınırlamalar | Kodlama ajanlarından geçiş sırasında mevcut mimarinin değiştirilip değiştirilmemesini değerlendirmelerini isteyin. | Limit |
| [AITuber OnAir'de Hydrogen ile Sohbet](#case-163) | Uygulamalar ve öğrenme | Live2D avatarının arkasındaki sohbet modeli olarak Hydrogen'ı deneyin. | Integration |
| [Kodla Oluşturulan Tanıtım Videosu](#case-164) | Uygulamalar ve öğrenme | Kodlama modeline kısa bir tanıtım görevi verip hareketli grafikleri inceleyin. | Demo |
| [İki Model Tapınaktan Kaçış Oyununu Yorumluyor](#case-165) | Karşılaştırmalar ve sınırlamalar | Aynı oyun fikrinde ışık ve atmosferin sahneyi ne kadar anlaşılır kıldığını karşılaştırın. | Evaluation |
| [Üç Gemini Modeli Ralli Aracı Canlandırıyor](#case-166) | Karşılaştırmalar ve sınırlamalar | Eğimli virajda süspansiyon davranışının ve lastik tutuşunun inandırıcılığını değerlendirin. | Evaluation |
| [Prosedürel Kızılgerdan Animasyonu](#case-167) | Etkileşimli 3B ve arayüzler | Oluşturulan uçuş animasyonunda kanat ve gövde hareketlerini inceleyin. | Demo |
| [Antigravity Orchestrator ve Swarm Arasında Seçim](#case-168) | Ajanlar ve kodlama iş akışları | Sıralı görevlerde modeller arasında iş devri, paralel görevlerde bağımsız uygulayıcı ve doğrulayıcı kullanın. | Tutorial |
| [İki Modelle Chasing Views Animasyonu](#case-169) | Karşılaştırmalar ve sınırlamalar | Çıktıyı ve süreyi modellerin akıl yürütme ayarlarıyla birlikte karşılaştırın. | Evaluation |
| [Design Creativity Bench'te Hız ve Maliyet](#case-170) | Karşılaştırmalar ve sınırlamalar | Yaratıcılık puanıyla birlikte tasarım başına üretim süresini ve maliyeti karşılaştırın. | Benchmark |
| [Referans Görselden SolidWorks Modeline](#case-171) | Ajanlar ve kodlama iş akışları | Bir ajanın SolidWorks modelleme iş akışını 3B referans görselle sınayın. | Integration |
| [Dört Model Çölde Dörtnala Koşan Atı Canlandırıyor](#case-172) | Karşılaştırmalar ve sınırlamalar | Işığa veya modelleme ayrıntısına geçmeden önce toynağın zemine temasını ve ağırlık aktarımını karşılaştırın. | Evaluation |
| [Jung'un Eşzamanlılığı Üzerine Sunum](#case-173) | Uygulamalar ve öğrenme | İlgili kavramların açıkça anlatılması gereken bir konuyla slayt üretimini sınayın. | Demo |
| [FrontierCS 2'de Bilgisayar Bilimi Araştırması](#case-174) | Karşılaştırmalar ve sınırlamalar | Standart kodlama testlerine bir araştırma kıyaslaması ekleyip çalışma ortamını kaydedin. | Benchmark |
| [Dört Modelle Bulutların Üzerinde Rio](#case-175) | Karşılaştırmalar ve sınırlamalar | Aynı yaratıcı görevde maliyet, süre ve algılanan kaliteyi karşılaştırın. | Evaluation |
| [GBENCH Teknik Görevlerinde Hydrogen](#case-176) | Karşılaştırmalar ve sınırlamalar | Teknik işi değerlendirirken fiyat ve süreyle birlikte doğrulanabilir kodlu ve kodsuz sonuçlara bakın. | Benchmark |
| [Arabalara Paralel Park Öğretmek](#case-177) | Karşılaştırmalar ve sınırlamalar | Oluşturulan simülasyonlarda öğrenme ilerlemesini ve son başarı oranlarını karşılaştırın. | Evaluation |
| [Etkileşimli Mitokondri Motoru](#case-178) | Uygulamalar ve öğrenme | Etkileşimli bir şemayla moleküler hareketi ATP üretimiyle ilişkilendirin. | Demo |
| [Qix Tarzı Alan Ele Geçirme Oyunu](#case-179) | Uygulamalar ve öğrenme | Kısa bir arcade oyunu tarifiyle ilk çıktının etkileşimli döngü içerip içermediğini sınayın. | Demo |
| [Hydrogen ile HTML Slaytları](#case-180) | Uygulamalar ve öğrenme | HTML üretimini sınarken slaytların görsel hiyerarşisini ve düzenini inceleyin. | Demo |
| [Terminal-Bench 4.0'da Hydrogen](#case-181) | Karşılaştırmalar ve sınırlamalar | Komut satırı kodlama modeli seçerken tamamlama oranını ve görev maliyetini birlikte değerlendirin. | Benchmark |
| [Tek HTML Dosyasında İllüstrasyon](#case-182) | Etkileşimli 3B ve arayüzler | Görsel referansın harici varlık olmadan kodla yeniden oluşturulup oluşturulamadığını sınayın. | Demo |
| [Üç Gemini Modeli Ahtapotu Canlandırıyor](#case-183) | Karşılaştırmalar ve sınırlamalar | Kayanın kavranmasının gövdeyi ileri taşıyıp taşımadığına bakın. | Evaluation |
| [Chrome'da Yapılandırılmış YouTube Özeti](#case-184) | E-tablolar ve Search | Chrome'daki Gemini panelinden zaman damgalı özet ve kaynaklı arka plan isteyin. | Tutorial |
| [Dersten Kısa Videoya](#case-185) | Uygulamalar ve öğrenme | Dersi videoya dönüştürürken anlatımın doğruluğunu ve temposunu kontrol edin. | Demo |
| [Durağan Sahneden Deniz Papağanı Animasyonu](#case-186) | Etkileşimli 3B ve arayüzler | Mevcut HTML sahnesini prosedürel animasyonun ilk karesi olarak kullanın. | Demo |
| [Bir Kale Modelleme Testi](#case-187) | Karşılaştırmalar ve sınırlamalar | Farklı model çalıştırmalarında kale çıktılarını ve kaynak kullanımını karşılaştırın. | Evaluation |
| [Antigravity Swarm'da Tarayıcı Kullanımı](#case-188) | Ajanlar ve kodlama iş akışları | Swarm değerlendirirken ajan görevleriyle birlikte tarayıcı etkinliğini inceleyin. | Demo |
| [Google Drive Üzerinden Muse'a İş Devri](#case-189) | Ajanlar ve kodlama iş akışları | Sıradaki adımı ikinci bir ajan yürütecekse araştırmayı izlenen Drive klasörü üzerinden devredin. | Integration |
| [Gemini Canvas'ta Blok Flüt Rehberi](#case-190) | Uygulamalar ve öğrenme | Notayı enstrüman yönergeleriyle eşleştiren alıştırma aracı için hızlı modu deneyin. | Demo |
| [Kapsam Büyüyünce Değişen Proje Tahmini](#case-191) | Karşılaştırmalar ve sınırlamalar | Teslim tahmini belirgin şekilde değiştiğinde modelden kapsamı ve varsayımları açıklamasını isteyin. | Limit |
| [Antigravity Swarm Pelikanı Canlandırıyor](#case-192) | Ajanlar ve kodlama iş akışları | Animasyon ve sesi kodlama ajanlarına atayıp birleşik sahneyi inceleyin. | Demo |
| [Artık Yılı da İçeren Takvim Sorusu](#case-193) | Karşılaştırmalar ve sınırlamalar | Basit bir dönüşüm sorusunda takvime özgü durumların hesaba katılıp katılmadığını kontrol edin. | Evaluation |
| [Tek HTML Dosyasında TAJ VICE](#case-194) | Uygulamalar ve öğrenme | Tek dosya sınırıyla gezilebilir harita prototipleyip kalan hataları sınayın. | Demo |
| [Google Cloud Projesi Üzerinden Antigravity](#case-195) | Ajanlar ve kodlama iş akışları | Yönetilen kimlik bilgileriyle Hydrogen'ı etkinleştirirken doğrulamayı ve proje faturalamasını denetleyin. | Tutorial |
| [Yanıtta Güncelliğini Yitirmiş Abonelik Sınırları](#case-196) | Karşılaştırmalar ve sınırlamalar | Araştırma asistanını değerlendirirken güncel plan şartlarını ve model adlarını birincil kaynaklardan doğrulayın. | Limit |
| [WebGL Animasyonunun Hikâyesini İyileştirmek](#case-197) | Karşılaştırmalar ve sınırlamalar | Teknik açıdan karmaşık ilk sürümde akış belirsizse daha güçlü bir hikâye isteyin. | Limit |
| [Mobil Tasarımı Carbon Planlıyor, Hydrogen Uyguluyor](#case-198) | Ajanlar ve kodlama iş akışları | Etkileşim tasarımını planlama modeline, uygulamayı yürütme modeline verin. | Demo |
| [İki Model Dağda Ejderha Dövüşünü Kodluyor](#case-199) | Karşılaştırmalar ve sınırlamalar | Aynı sahnede iki karakterin etkileşiminin nasıl canlandırıldığını karşılaştırın. | Evaluation |
| [Tek İstemden 3B Minyatür Ada](#case-200) | Etkileşimli 3B ve arayüzler | Tek çalıştırmada suyun, arazinin ve önemli noktaların anlaşılır biçimde yerleştirilip yerleştirilmediğini sınayın. | Demo |
| [Yeniden Kullanılabilir Three.js Pelikan İstemi](#case-201) | Karşılaştırmalar ve sınırlamalar | Bisiklet animasyonunda bacak, tekerlek ve yön hareketlerinin uyumunu sınayın. | Evaluation |
| [T3 Code Kurulumunda Hydrogen](#case-202) | Ajanlar ve kodlama iş akışları | Gerçekçi bir oturumda kodlama istemcisini deneyip kayan ve haftalık kotaları takip edin. | Integration |
| [Elle Çizilmiş Görünümlü Kamu Spotu](#case-203) | Uygulamalar ve öğrenme | Bir kamu mesajıyla elle çizilmiş görsel üslubu değerlendirin. | Demo |
| [On Sanat Tarzında Bisikletli Tavus Kuşu](#case-204) | Ajanlar ve kodlama iş akışları | Görsel geçişleri oluşturmak ve sesi eşlemek için çok modelli Swarm kullanın. | Demo |
| [Üç Ortamda Aynı Kır Evi İstemi](#case-205) | Karşılaştırmalar ve sınırlamalar | Görsel bir görevi başka model ayarı veya platforma taşırken çıktı biçimini kontrol edin. | Evaluation |
| [Tek İstemle Pano Karşılaştırması](#case-206) | Karşılaştırmalar ve sınırlamalar | Ortak bir arayüz istemiyle düzeni ve bilgi hiyerarşisini karşılaştırın. | Evaluation |
| [Görselden React.gg Sitesini Yeniden Yapmak](#case-207) | Uygulamalar ve öğrenme | Referans görselden başlayıp hangi ayrıntıların düzenleme gerektirdiğini inceleyin. | Demo |
| [Tekillik Temalı Etkileşimli Panel](#case-208) | Etkileşimli 3B ve arayüzler | Tek bir görsel fikir etrafında kısa etkileşimli akış prototipleyin. | Demo |
| [İki Model Yandan Kaydırmalı Animasyon Kodluyor](#case-209) | Karşılaştırmalar ve sınırlamalar | Oluşturulan aksiyon sahnelerinde hareket sürekliliğine ve yapım maliyetine bakın. | Evaluation |
| [Koşu Antrenörü Olarak Gemini](#case-210) | Uygulamalar ve öğrenme | Antrenman kaydını önerilerle karşılaştırıp hedefleri başlangıç seviyenize göre ayarlayın. | Demo |
| [Zincir Üzerinde Skor Tutan Tarayıcı Oyunu](#case-211) | Uygulamalar ve öğrenme | Masaüstü oyununu deneyin ve skor kaydını oynanıştan ayrı doğrulayın. | Demo |
| [Japonca Yanıtta Görüntülenmeyen Formüller](#case-212) | Karşılaştırmalar ve sınırlamalar | TeX komutlu yanıtlarda doğrulukla birlikte matematiğin ekranda nasıl göründüğünü sınayın. | Limit |
| [Japonca İstemden MIDI Üreten Beste Uygulaması](#case-213) | Uygulamalar ve öğrenme | Japonca girdiyi MIDI, WAV ve piyano rulosuna dönüştüren bir aracı prototipleyin. | Demo |
| [Sessiz Kalma Talimatını Sınamak](#case-214) | Karşılaştırmalar ve sınırlamalar | İş akışı gerektiriyorsa modelin hiç yanıt üretmemesini sınayın. | Evaluation |
| [Tek Sayfalık Konser Özeti](#case-215) | Uygulamalar ve öğrenme | Etkinlik bilgisini kolay taranabilen görsel bir sayfaya dönüştürün. | Demo |
| [Üç Model Elektrik Motorunu Açıklıyor](#case-216) | Karşılaştırmalar ve sınırlamalar | Aynı simülasyon istemiyle görsel netliği ve öğretici denetimleri karşılaştırın. | Evaluation |
| [İki Model Akışıyla Masa Sahnesi Animasyonu](#case-217) | Karşılaştırmalar ve sınırlamalar | Sahne ayrıntılarını, ses düzeyini ve sondaki sabit kareyi asıl istemle karşılaştırın. | Evaluation |
| [Avatardan Günlük Yaşam Montajı](#case-218) | Uygulamalar ve öğrenme | Tek avatar ve dört gündelik sahneyle kısa storyboard uyarlamasını değerlendirin. | Demo |
| [Hydrogen ComfyUI Karakter Klibini Planlıyor](#case-219) | Uygulamalar ve öğrenme | Kostümü ve arka planı sabit tutup video boyunca ifadeleri ve hareketleri değiştirin. | Integration |
| [Almance Vale'i 100 Modüle Çıkarmak](#case-220) | Ajanlar ve kodlama iş akışları | Mevcut uygulamayı bir kodlama ajanına taşıyıp modül eklerken üslubu korumasını isteyin. | Demo |
| [Prosedürel Sesli 2B Köy](#case-221) | Karşılaştırmalar ve sınırlamalar | Yapım süresinin yanında seslerin ekrandaki olaylara uyup uymadığını kontrol edin. | Evaluation |
| [Bir Şarkı İçin Geniş Ekran Görselleştirmesi](#case-222) | Uygulamalar ve öğrenme | Şarkı ve çerçeve tarifi verip hareketin müziğin enerjisini nasıl taşıdığını inceleyin. | Demo |
| [Yedi Hydrogen Alt Ajanıyla Niagara Şelalesi](#case-223) | Ajanlar ve kodlama iş akışları | Koordinatöre farklı sahne öğeleri vererek bunları uygulayıcı ajanlara dağıtmasını sağlayın. | Demo |
| [İki Tarihî Romantik Klipte Süreklilik](#case-224) | Uygulamalar ve öğrenme | İkinci klipte devam ederken hangi ayrıntıların korunacağını belirtin. | Demo |
| [Gemini Uygulamasında Su Küresi](#case-225) | Etkileşimli 3B ve arayüzler | Basit bir optik sahneyle parlak noktaların ve kırılmanın ilişkisini inceleyin. | Demo |

<a id="agents"></a>
## ⚡ Ajanlar ve kodlama iş akışları

<a id="case-1"></a>
### Örnek 1: [Antigravity'de kod tabanı bakımı](https://x.com/antigravity/status/2120944334023389476) (hazırlayan [@antigravity](https://x.com/antigravity))

**Düzenlemeleri, araç kullanımını ve doğrulamayı birlikte değerlendirmek için sınırları belirli bir bakım görevi kullanın.**

Antigravity'nin tanıtım demosu, Hydrogen'ın bir kod tabanının bakımını yaptığını gösteriyor. Bu, platformun hazırladığı bir örnektir; bağımsız olarak tekrarlanmış bir mühendislik kıyaslaması değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042-poster.jpg" alt="Case 1 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U042.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-2"></a>
### Örnek 2: [Paralel çalışan on altı canvas uygulaması](https://x.com/shengzheyao/status/2120944141559550409) (hazırlayan [@shengzheyao](https://x.com/shengzheyao))

**Geliştirmeyi bağımsız modüllere ayırın; planlama, uygulama ve kalite kontrol rollerini açıkça belirleyin.**

Google DeepMind'daki bir Antigravity CLI geliştiricisi, Hydrogen bağımlılıksız 16 canvas mini uygulaması oluştururken Carbon'ın koordinasyon, doğrulama ve entegrasyon yaptığını anlatıyor. Bu, birden fazla model kullanan bir iş akışıdır; sonuç yalnızca Hydrogen'a atfedilmemelidir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044-poster.jpg" alt="Case 2 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U044.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-3"></a>
### Örnek 3: [Çok modelli bir sürüyle kızıl güve](https://x.com/thtbee_/status/2120958666480513310) (hazırlayan [@thtbee_](https://x.com/thtbee_))

**Etkileşimli bir yaratıcı kodlama projesinde orkestrasyon ve uygulama rollerini ayırın.**

Üretici, Hydrogen çalışanları kızıl güve eserini oluştururken Carbon'ın bir Antigravity sürüsünü yönettiğini söylüyor. Bildirilen 45 dakikalık süre bu çok modelli iş akışını kapsıyor ve bağımsız olarak ölçülmedi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024-poster.jpg" alt="Case 3 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U024.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-4"></a>
### Örnek 4: [3D Medic ile inceleme ve onarım](https://x.com/GoogleAI/status/2120940683233984862) (hazırlayan [@GoogleAI](https://x.com/GoogleAI))

**Bir 3B dosyayı inceleyen, hataları bulan ve dışa aktarmadan önce onarım öneren bir ajanı keşfedin.**

Google AI'ın 3D Medic demosu, AI Studio'da oluşturulmuş bir Managed Agent uygulaması kullanıyor. Bu, bir dosya onarım iş akışını gösterir; herhangi bir 3B varlığın doğru onarılacağının kanıtı değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053-poster.jpg" alt="Case 4 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U053.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-5"></a>
### Örnek 5: [Devin'de oluşturulmuş bir yelkenli sahnesi](https://x.com/Da7_Tech/status/2120967690722677144) (hazırlayan [@Da7_Tech](https://x.com/Da7_Tech))

**Modeli gerçekten kullanmayı planladığınız kodlama ajanı ortamında değerlendirin.**

Kaynak, Devin içinde çalışan Hydrogen'a atfedilen bir yelkenli sahnesi sunuyor. Kısa gönderi; tam istemi, yineleme geçmişini veya tekrarlanabilir bir kurulumu açıklamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018-poster.jpg" alt="Case 5 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U018.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-59"></a>
### Örnek 59: [n8n'de Hydrogen ile Araç Kullanımı](https://x.com/n8n_io/status/2120947273534197886) (hazırlayan [@n8n_io](https://x.com/n8n_io))

**n8n'deki araç çağrısı döngülerini Hydrogen'a atayıp planlamayı ayrı bir adımda yürütün.**

n8n, Hydrogen desteğini belgeliyor. Planlamada Carbon ya da Argon, uygulamada Hydrogen kullanılmasını öneriyor ve kurulum bağlantısını paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947273534197886-1-url-1c58346dec35.jpg" alt="Case 59 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-12

---

<a id="case-69"></a>
### Örnek 69: [Çok Ajanlı Kurulumda Kimlik Doğrulama](https://x.com/studio_yebisu/status/2120969033260646551) (hazırlayan [@studio_yebisu](https://x.com/studio_yebisu))

**Ajan başka bir sağlayıcıya iş aktardığında kimlik doğrulamasını hangi istemcinin yaptığını kontrol edin.**

Yazar, Claude'dan Antigravity CLI üzerinden Hydrogen kullanmasını istediğini bildiriyor. Claude Code'un doğrudan kimlik doğrulamayı denediğini ve Antigravity erişiminin askıya alındığını söylüyor. Ekran görüntüsünde askıya alma bildirimi var. Nedeni istemcinin izlediği yola bağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120969033260646551-1-url-67a0e9f6f2bc.png" alt="Case 69 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-70"></a>
### Örnek 70: [Antigravity'de Goal Mode Çalıştırması](https://x.com/Inmerson/status/2120973427788124345) (hazırlayan [@Inmerson](https://x.com/Inmerson))

**Uzun bir kodlama oturumunda planı, kod değişikliklerini ve test sonuçlarını izleyin.**

Yazar, Hydrogen Extra ile planlama, uygulama ve testleri kapsayan 105 dakikalık bir Goal Mode oturumu bildiriyor. Test sonuçları yazarın beyanına dayanıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-1-url-d2827ec85ec0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-1-url-d2827ec85ec0.png" alt="Case 70 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-2-url-352705a2d20c.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973427788124345-2-url-352705a2d20c.png" alt="Case 70 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-73"></a>
### Örnek 73: [Antigravity Orchestrator'da Carbon ve Hydrogen](https://x.com/Google/status/2120982566891356279) (hazırlayan [@Google](https://x.com/Google))

**Daha hızlı uygulama modeli takıldığında planlama modelinin devreye girmesini sağlayın.**

Google, Carbon'un planlayıp sorunlarda devreye girdiğini, Hydrogen'ın düzenleyip test ettiğini açıklıyor. Terminal-Bench 4.0'da Carbon'a yakın başarı, daha az kota kullanımı ve daha kısa süre bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-poster-b8f89a40d358.jpg" alt="Case 73 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120982566891356279-1-url-75314f0e4450.mp4)

Tür: Integration | Tarih: 2026-11-12

---

<a id="case-87"></a>
### Örnek 87: [OpenClaw'da Hydrogen](https://x.com/openclaw/status/2121098531205501401) (hazırlayan [@openclaw](https://x.com/openclaw))

**Kullanmayı düşündüğünüz ajan çerçevesinde model seçimini kontrol edin.**

OpenClaw Hydrogen desteğini duyuruyor ve ekran görüntüsü paylaşıyor. Gönderi kıyaslama sonucu veya kurulum dökümü içermiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121098531205501401-1-url-7d8612587051.jpg" alt="Case 87 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-97"></a>
### Örnek 97: [Blender MCP ile Taht Salonu](https://x.com/ashen_one/status/2121165467821936651) (hazırlayan [@ashen_one](https://x.com/ashen_one))

**Oluşturulan sahnenin kompozisyonunu Blender MCP ile düzenleyicide inceleyin.**

Yazar Game of Thrones'daki Demir Taht salonunun yeniden oluşturulmasını Hydrogen ve Blender MCP'ye atfediyor. Sahnenin kaydını paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-poster-3b5239c01fca.jpg" alt="Case 97 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121165467821936651-1-url-124c83a0a646.mp4)

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-113"></a>
### Örnek 113: [Tarayıcı CAD'inde Beton Mikseri Montajı](https://x.com/johnsanthosh01/status/2121243197901041869) (hazırlayan [@johnsanthosh01](https://x.com/johnsanthosh01))

**Oluşturulan montajı CAD akışında kullanmadan önce parça ağacını ve parçaların uyumunu inceleyin.**

Yazar Hydrogen'ın CadX Studio'da tek istemle 40 dakikada 265 parçalı beton mikseri oluşturduğunu bildiriyor. Parçaları tek tek elle modellemediğini belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-poster-5192b1b49665.jpg" alt="Case 113 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121243197901041869-1-url-c704d069fd36.mp4)

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-114"></a>
### Örnek 114: [Blender'da Prosedürel Balta Modelleme](https://x.com/camperaigg/status/2121252572115951897) (hazırlayan [@camperaigg](https://x.com/camperaigg))

**Prosedürel bir Blender varlığını referans silüeti ve birkaç düzenleyici görünümüyle inceleyin.**

Yazar, Antigravity CLI'da Hydrogen kullanarak Python modülleri ve yinelemeli görünüm kontrolleriyle stilize balta yaptığını söylüyor. Kayıt dahil 51 dakika ve 5,01 USD API maliyeti bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-poster-2d8eecf7e7f6.jpg" alt="Case 114 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-1-url-1ff99f54fe92.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121252572115951897-2-url-4cdc2b18764d.jpg" alt="Case 114 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-118"></a>
### Örnek 118: [28 Modüllü Ember Isle Projesi](https://x.com/IamEmily2050/status/2121258646759952644) (hazırlayan [@IamEmily2050](https://x.com/IamEmily2050))

**Büyük sahneyi modüllere bölüp her üretimin süresini kaydedin.**

Yazar Ember Isle için Gemini uygulamasında Hydrogen High kullandı. 28 modül, modül başına bir istem ve istem başına 82 ile 290 saniye bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-poster-46a68c400032.jpg" alt="Case 118 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121258646759952644-1-url-c100ba7f212f.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-150"></a>
### Örnek 150: [Ayrı Modellerle Planlama, Uygulama ve İnceleme](https://x.com/naufaldi/status/2121499487999013081) (hazırlayan [@naufaldi](https://x.com/naufaldi))

**Planlama, uygulama ve inceleme için ayrı roller tanımlayın ve model başına toplamları karşılaştırın.**

Yazar planlama için Opus 5.5, uygulama için Hydrogen ve yedekte Sol, inceleme için Sol 6.1 kullandığını anlatıyor. Kendi Antigravity kullanım sayılarını ayrı yayımlanmış kıyaslamalarla birlikte sunuyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-1-url-4838b2ba0b61.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-1-url-4838b2ba0b61.jpg" alt="Case 150 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-2-url-e7c778cfcf91.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-2-url-e7c778cfcf91.jpg" alt="Case 150 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-3-url-5d627806345d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121499487999013081-3-url-5d627806345d.jpg" alt="Case 150 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-154"></a>
### Örnek 154: [Kodlama İstemcisinde Hydrogen Kurulumu](https://x.com/k2sbhai/status/2121509825658147041) (hazırlayan [@k2sbhai](https://x.com/k2sbhai))

**Desteklenen bir istemcide Google API anahtarıyla birlikte tam model kimliğini kullanın.**

Yazar Google AI Studio'dan anahtar almayı ve OpenCode ya da Cline'da gemini-4-hydrogen seçmeyi anlatıyor. Erişim ve hız sınırları sağlayıcıya bağlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121509825658147041-1-url-2c02386dd242.jpg" alt="Case 154 source image 1" height="360"></a>

Tür: Tutorial | Tarih: 2026-11-14

---

<a id="case-155"></a>
### Örnek 155: [Hydrogen ile SuperARIS Araştırma Ekibi](https://x.com/NFT_Chen/status/2121520579304206443) (hazırlayan [@NFT_Chen](https://x.com/NFT_Chen))

**Çok modelli ajan ekibinde Hydrogen'a belirli araştırma ve metin görevleri atayın.**

Paylaşım, SuperARIS kurulumu ve ekip seçimini anlatıyor. Tartışma ve yazı için Hydrogen ya da Carbon, koordinasyon ve uygulama için ayrı roller öneriyor. Tarif araştırma kalitesini ölçmüyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-1-url-724d48461bd4.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-1-url-724d48461bd4.jpg" alt="Case 155 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-2-url-dd4a1c6d1650.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-2-url-dd4a1c6d1650.jpg" alt="Case 155 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-3-url-a70f7661d1c1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-3-url-a70f7661d1c1.jpg" alt="Case 155 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-4-url-8cdfdaf95c58.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121520579304206443-4-url-8cdfdaf95c58.jpg" alt="Case 155 source image 4" width="100%"></a>
</td>
</tr>
</table>

Tür: Integration | Tarih: 2026-11-14

---

<a id="case-156"></a>
### Örnek 156: [Dört Modelle Bir Çekirdek Modülü Baştan Yazmak](https://x.com/oasisfeng/status/2121523934831276203) (hazırlayan [@oasisfeng](https://x.com/oasisfeng))

**Yeniden yazım için ajan seçerken kodu anlama, tasarım ve uygulama becerisini karşılaştırın.**

Yazar Hydrogen, Argon, GPT-6 Astra ve Claude Opus 5.5'in çekirdek modül yenilemelerini karşılaştırıyor. Hydrogen'ın uygulamadaki güçlü yanlarını diğer çalıştırmalardaki mimari tasarımdan ayrı ele alıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-1-url-729f1441593f.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-1-url-729f1441593f.png" alt="Case 156 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-2-url-4f4c6848310c.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121523934831276203-2-url-4f4c6848310c.png" alt="Case 156 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-158"></a>
### Örnek 158: [Muse İşleri Antigravity CLI'a Aktarıyor](https://x.com/tetumemo/status/2121528823061852166) (hazırlayan [@tetumemo](https://x.com/tetumemo))

**Uzaktaki asistanı yerel kodlama ortamına bağlayın ve varsayılan yazı modelini seçin.**

Yazar, Muse'un ev bilgisayarındaki Antigravity CLI'a görev gönderip sonuç aldığını anlatıyor. Varsayılanı Hydrogen, Argon da kullanılabiliyor. Örneklerde Japonca metinler ve görseller var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528823061852166-1-url-5d08d484fad0.jpg" alt="Case 158 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-14

---

<a id="case-168"></a>
### Örnek 168: [Antigravity Orchestrator ve Swarm Arasında Seçim](https://x.com/ohayou792/status/2121624258984153452) (hazırlayan [@ohayou792](https://x.com/ohayou792))

**Sıralı görevlerde modeller arasında iş devri, paralel görevlerde bağımsız uygulayıcı ve doğrulayıcı kullanın.**

Yazar, güçlü modelin planlayıp Hydrogen'ın uyguladığı Orchestrator akışını şemalaştırıyor. Bunu /swarm ile karşılaştırıyor ve seçimi görevlerin birbirine bağımlılığına bağlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121624258984153452-1-url-bd7a755272bd.jpg" alt="Case 168 source image 1" height="360"></a>

Tür: Tutorial | Tarih: 2026-11-14

---

<a id="case-171"></a>
### Örnek 171: [Referans Görselden SolidWorks Modeline](https://x.com/GoGoFly23/status/2121636952479080713) (hazırlayan [@GoGoFly23](https://x.com/GoGoFly23))

**Bir ajanın SolidWorks modelleme iş akışını 3B referans görselle sınayın.**

Yazar Antigravity'de Hydrogen'a tek görsel verdiğini bildiriyor ve SolidWorks parçasını gösteriyor. Takip gönderisinde SolidWorks MCP anılıyor. Bu seçkide tolerans ve mühendislik uygunluğu test edilmedi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121636952479080713-1-url-7724363fcc76.jpg" alt="Case 171 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-14

---

<a id="case-188"></a>
### Örnek 188: [Antigravity Swarm'da Tarayıcı Kullanımı](https://x.com/Saboo_Shubham_/status/2121852445756477924) (hazırlayan [@Saboo_Shubham_](https://x.com/Saboo_Shubham_))

**Swarm değerlendirirken ajan görevleriyle birlikte tarayıcı etkinliğini inceleyin.**

Bir Google çalışanı Hydrogen ve Antigravity Swarm ile tarayıcı kullanımının ekran görüntüsünü paylaşıyor. Tam görev günlüğü bulunmuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121852445756477924-1-url-e5b25e72b7f0.jpg" alt="Case 188 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-189"></a>
### Örnek 189: [Google Drive Üzerinden Muse'a İş Devri](https://x.com/nasuvit_z/status/2121857992702525734) (hazırlayan [@nasuvit_z](https://x.com/nasuvit_z))

**Sıradaki adımı ikinci bir ajan yürütecekse araştırmayı izlenen Drive klasörü üzerinden devredin.**

Yazar, Hydrogen'ın bilgiyi toplayıp Drive dosyasında düzenlediğini ve dosya gelince Muse'un işi devraldığını anlatıyor. Şema devir akışını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121857992702525734-1-url-d438bd9f499b.jpg" alt="Case 189 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-15

---

<a id="case-192"></a>
### Örnek 192: [Antigravity Swarm Pelikanı Canlandırıyor](https://x.com/chetaslua/status/2121885449509851415) (hazırlayan [@chetaslua](https://x.com/chetaslua))

**Animasyon ve sesi kodlama ajanlarına atayıp birleşik sahneyi inceleyin.**

Yazar farklı sanat tarzları arasında geçen JavaScript pelikan sahnesini Carbon ve Hydrogen'a atfediyor. Müziğin ve ses efektlerinin kodla üretildiğini söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-poster-62e881524b30.jpg" alt="Case 192 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121885449509851415-1-url-a4bb35da3ee7.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-195"></a>
### Örnek 195: [Google Cloud Projesi Üzerinden Antigravity](https://x.com/loganlu51268/status/2121911409042719023) (hazırlayan [@loganlu51268](https://x.com/loganlu51268))

**Yönetilen kimlik bilgileriyle Hydrogen'ı etkinleştirirken doğrulamayı ve proje faturalamasını denetleyin.**

Yazar kişisel Antigravity planından Application Default Credentials kullanan Google Cloud Agent Platform projesine geçişi anlatıyor. Model listesinde Hydrogen var. Proje ücretlerinin SKU'ya göre izlenmesi de açıklanıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-1-url-c86f9942da03.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-1-url-c86f9942da03.png" alt="Case 195 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-2-url-7695f3eaa9a3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-2-url-7695f3eaa9a3.jpg" alt="Case 195 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-3-url-6bad19f93237.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-3-url-6bad19f93237.jpg" alt="Case 195 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-4-url-99834386815e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121911409042719023-4-url-99834386815e.jpg" alt="Case 195 source image 4" width="100%"></a>
</td>
</tr>
</table>

Tür: Tutorial | Tarih: 2026-11-15

---

<a id="case-198"></a>
### Örnek 198: [Mobil Tasarımı Carbon Planlıyor, Hydrogen Uyguluyor](https://x.com/thebuggeddev/status/2121945961555718334) (hazırlayan [@thebuggeddev](https://x.com/thebuggeddev))

**Etkileşim tasarımını planlama modeline, uygulamayı yürütme modeline verin.**

Yazar mobil uygulamanın planını Carbon'a, Reanimated fiziği dahil uygulamasını Hydrogen'a atfediyor. Akıcı olarak tarif ettiği hareketi kayıtta gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-poster-d60b8722795a.jpg" alt="Case 198 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121945961555718334-1-url-54dd2b9f3dd5.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-202"></a>
### Örnek 202: [T3 Code Kurulumunda Hydrogen](https://x.com/bei351009016/status/2121964293906206916) (hazırlayan [@bei351009016](https://x.com/bei351009016))

**Gerçekçi bir oturumda kodlama istemcisini deneyip kayan ve haftalık kotaları takip edin.**

Yazar T3 Code'da Gemini Pro bağlantısıyla Hydrogen'ı yaklaşık yarım gün kullandığını bildiriyor. Ekran görüntüleri kota deneyimini gösteriyor. Karşılaştırmada hissedilen hız ile doğruluğu ayrı değerlendiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121964293906206916-1-url-e5954fdfc701.jpg" alt="Case 202 source image 1" height="360"></a>

Tür: Integration | Tarih: 2026-11-15

---

<a id="case-204"></a>
### Örnek 204: [On Sanat Tarzında Bisikletli Tavus Kuşu](https://x.com/SahilPanhotra/status/2121995488425849064) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Görsel geçişleri oluşturmak ve sesi eşlemek için çok modelli Swarm kullanın.**

Yazar on tarzı birleştiren bisikletli tavus kuşunu Carbon ve Hydrogen Swarm'a atfediyor. Görsel, müzik ve ses efektlerinin kodla üretildiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-poster-5b8935f59c44.jpg" alt="Case 204 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121995488425849064-1-url-dedf5e21aa8d.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-220"></a>
### Örnek 220: [Almance Vale'i 100 Modüle Çıkarmak](https://x.com/IamEmily2050/status/2122257581175410858) (hazırlayan [@IamEmily2050](https://x.com/IamEmily2050))

**Mevcut uygulamayı bir kodlama ajanına taşıyıp modül eklerken üslubu korumasını isteyin.**

Yazar projeyi Gemini uygulamasından Antigravity'ye taşıdı. Swarm modunda Hydrogen Extra ile kod düzenini koruduğunu ve birkaç saatte Almance Vale'i 100 modüle çıkardığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-poster-76e3b7399077.jpg" alt="Case 220 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122257581175410858-1-url-33ecf3a3a154.mp4)

Tür: Demo | Tarih: 2026-11-16

---

<a id="case-223"></a>
### Örnek 223: [Yedi Hydrogen Alt Ajanıyla Niagara Şelalesi](https://x.com/SahilPanhotra/status/2122311637684424737) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Koordinatöre farklı sahne öğeleri vererek bunları uygulayıcı ajanlara dağıtmasını sağlayın.**

Yazar tek istemle bir saatin altında kurulan Niagara deneyimini Carbon ve yedi Hydrogen alt ajanına atfediyor. Kayıt suyu, tekneleri, farklı bakış açılarını ve değişen ortamları gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-poster-fdd8d9abdaf1.jpg" alt="Case 223 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122311637684424737-1-url-58fe4d9e64ef.mp4)

Tür: Demo | Tarih: 2026-11-16

---


<a id="apps-learning"></a>
## 💻 Uygulamalar ve öğrenme

<a id="case-6"></a>
### Örnek 6: [Lingo City'de dil pratiği](https://x.com/tulseedoshi/status/2121095754844713427) (hazırlayan [@tulseedoshi](https://x.com/tulseedoshi))

**Bağlama dayalı dil pratiği için çalışma kartlarını etkileşimli bir sokak sahnesiyle birleştirin.**

Tulsee Doshi, özelleştirilmiş 2B ve 3B çalışma kartlarını akışla sunan ve sanal bir şehirde esnafla konuşma pratiği sağlayan bir Google örneği paylaşıyor. Bu bir sağlayıcı demosudur, bağımsız bir öğrenme sonuçları araştırması değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001-poster.jpg" alt="Case 6 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U001.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-7"></a>
### Örnek 7: [3B kâğıt tiyatrosu olarak Romeo ve Juliet](https://x.com/techartist_/status/2120957446202253803) (hazırlayan [@techartist_](https://x.com/techartist_))

**Belirli bir dersi, net bir öğrenme hedefi olan etkileşimli bir sahneye dönüştürün.**

Üretici, GCSE İngiliz Edebiyatı için Romeo ve Juliet'in balkon sahnesini konu alan bir 3B kâğıt tiyatrosu dersi oluşturdu. Kaynak arayüzü gösteriyor ancak öğrenme sonuçlarını ölçmüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026-poster.jpg" alt="Case 7 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U026.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-8"></a>
### Örnek 8: [Tasarım görselinden okuma sitesine](https://x.com/thebuggeddev/status/2120952661046689992) (hazırlayan [@thebuggeddev](https://x.com/thebuggeddev))

**Görsel anlayışı ve çalışan ön yüz uygulamasını değerlendirmek için bir referans tasarım kullanın.**

Üretici, Hydrogen'ın bir tasarım görselini 5 dakika 27 saniyede çalışan bir okuma yönetimi sitesine dönüştürdüğünü söylüyor. Süre ve eksiksizlik, kaynağın iddialarıdır; bu derlemede bağımsız bir işlevsel test bulunmuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030-poster.jpg" alt="Case 8 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U030.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-9"></a>
### Örnek 9: [Yirmi modülde oluşturulmuş koi bahçesi](https://x.com/IamEmily2050/status/2120951069874532806) (hazırlayan [@IamEmily2050](https://x.com/IamEmily2050))

**Tek bir istemden eksiksiz sonuç beklemek yerine büyük bir sahneyi küçük modüllerle oluşturun.**

Üretici, Gemini uygulamasında 20 modül için 20 istem kullandığını ve her birinin 90–270 saniye sürdüğünü bildiriyor. Yazar erken erişimi açıkladı; örnek tek seferlik bir sonuç değil, açıkça yinelemeli bir çalışmadır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032-poster.jpg" alt="Case 9 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U032.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-10"></a>
### Örnek 10: [Proton füzyonunu öğreten bir oyun](https://x.com/SidraMiconi/status/2120948703095820743) (hazırlayan [@SidraMiconi](https://x.com/SidraMiconi))

**Bilimsel bir sürecin etkileşimli açıklamasını prototipleyin, ardından temelindeki bilimi kontrol edin.**

Üreticinin oyunu genç bir yıldız içindeki proton–proton zincirini izliyor. Bildirilen tek istem, 78 saniyelik çalışma süresi ve yaklaşık $0.19 maliyet, kaynağın iddialarıdır; bağımsız olarak tekrarlanmış sonuçlar değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034-poster.jpg" alt="Case 10 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U034.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-58"></a>
### Örnek 58: [On Beş Dakikada Minecraft Tarzı Prototip](https://x.com/RezAIT00/status/2120947124418293876) (hazırlayan [@RezAIT00](https://x.com/RezAIT00))

**Bir voksel oyununda kazma ve envanter gibi sistemlerin uyumunu sınayın.**

Yazar, Hydrogen Extra High ile 15 dakikada Minecraft tarzı bir prototip kurduğunu bildiriyor. Blok yerleştirme, kazma ve envanterden söz ediyor. Kayıt bu özellikleri kısmen gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-poster-dd00f590b6bc.jpg" alt="Case 58 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947124418293876-1-url-2b6a22869ba5.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-77"></a>
### Örnek 77: [Haber Özetinden Anlatımlı Klibe](https://x.com/gigabit_million/status/2121011957042163722) (hazırlayan [@gigabit_million](https://x.com/gigabit_million))

**Araştırılmış bir haber özetinden kısa bir anlatımlı video hazırlayıp kullanılan olguları kontrol edin.**

Yazar, mobil Gemini'de Hydrogen'ın güncel haberleri arayıp bir taslak hazırlamasını kaydediyor. Video isteğinden sonra uygulamada on saniyelik oynatım görülüyor. Süre ve anlatım bilgileri yazarın beyanı. Görüntüyü üreten sistem belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-poster-f46a450328ad.jpg" alt="Case 77 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121011957042163722-1-url-a5fe41d90add.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-90"></a>
### Örnek 90: [Web Kamerasıyla Havada Çizim](https://x.com/CodeByPoonam/status/2121121804483969102) (hazırlayan [@CodeByPoonam](https://x.com/CodeByPoonam))

**Havada çizgiler çizin ve arayüzün hareketleri nasıl takip ettiğine bakın.**

Yazar erken Hydrogen erişimiyle web kamerası üzerinden çizim aracı geliştirdiğini bildiriyor ve kullanım kaydını paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-poster-d2740b731919.jpg" alt="Case 90 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121121804483969102-1-url-9f7c08b41d28.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-93"></a>
### Örnek 93: [Tek Çalıştırmada Web Portalı](https://x.com/kimura_0314/status/2121130305532878979) (hazırlayan [@kimura_0314](https://x.com/kimura_0314))

**Tek tek akışları sınamadan önce ilk arayüzü portal düzeni üzerinden değerlendirin.**

Yazar Antigravity'de Hydrogen ile tek üretimde oluşturduğunu bildirdiği portalın ekran görüntüsünü paylaşıyor. Portal etkileşimlerinin çalışıp çalışmadığı belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130305532878979-1-url-d6714b69364f.jpg" alt="Case 93 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-95"></a>
### Örnek 95: [Cities: Skylines Tarzı Bir Şehir Kurma Oyunu](https://x.com/yohakujpn/status/2121146464466604147) (hazırlayan [@yohakujpn](https://x.com/yohakujpn))

**Bir şehir oyunu prototipi hazırlayıp denetimlerin ve simülasyonların uyumunu inceleyin.**

Yazar Hydrogen'a atfettiği Cities: Skylines tarzı prototipi gösteriyor ve üretim oturumunun 30 dakikadan kısa sürdüğünü bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-poster-34aeeb54a6af.jpg" alt="Case 95 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121146464466604147-1-url-298b92e5fe96.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-124"></a>
### Örnek 124: [Kimya Kitabından Etkileşimli Derse](https://x.com/smalkalbani/status/2121282231759155617) (hazırlayan [@smalkalbani](https://x.com/smalkalbani))

**İpuçları, sesli anlatım ve isteğe bağlı metinle kendi kendine öğrenme dersi oluşturun.**

Yazar sesli yönlendirme ve ipuçları içeren dokuzuncu sınıf kimya dersini gösteriyor. Gösterim kullanım akışını belgeliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-poster-46c6c0553638.jpg" alt="Case 124 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121282231759155617-1-url-14aae247e3b7.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-125"></a>
### Örnek 125: [Vocaloid Şarkı Prototipi](https://x.com/peach2k2/status/2121284159565902188) (hazırlayan [@peach2k2](https://x.com/peach2k2))

**Tek seferde oluşturulan bestenin karaktere ve müzik tarzına uygunluğunu inceleyin.**

Yazar şarkı klibini paylaşıp besteyi Hydrogen'a atfediyor. Sesin hangi araçla üretildiği belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-poster-9825f0c25adc.jpg" alt="Case 125 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121284159565902188-1-url-14f6acb88f2c.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-134"></a>
### Örnek 134: [Görselden Karmaşık Bir İntegrali Okuma](https://x.com/HarshithLucky3/status/2121303778548908228) (hazırlayan [@HarshithLucky3](https://x.com/HarshithLucky3))

**Uzun ifadeyi sadeleştirmeden önce modelin eşit integral sınırlarını fark edip etmediğini kontrol edin.**

Yazar, Gemini uygulamasında Hydrogen High'ın integral ekran görüntüsüne verdiği yanıtı kaydediyor. Test dış integralin iki sınırının eşit olduğunun anlaşılmasıyla ilgili.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-poster-bec6c022344c.jpg" alt="Case 134 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121303778548908228-1-url-7faa26a09daa.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-138"></a>
### Örnek 138: [WebGL2 ile İnsan Hücresi Ansiklopedisi](https://x.com/soumyadesign/status/2121354542344466565) (hazırlayan [@soumyadesign](https://x.com/soumyadesign))

**Hücre içindeki uzamsal ilişkileri etkileşimli kesitle anlatın.**

Yazar Hydrogen ve Antigravity ile harici kütüphane kullanmadan WebGL2 tabanlı 3B insan hücresi ansiklopedisi geliştirdiğini bildiriyor. Kesit görünümünü vurguluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-poster-6a06a050f91c.jpg" alt="Case 138 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121354542344466565-1-url-23aab29b9f33.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-140"></a>
### Örnek 140: [Parking Bench'te Yalnızca Görselle Oynayan Rakip](https://x.com/agenticjay/status/2121391300822081713) (hazırlayan [@agenticjay](https://x.com/agenticjay))

**Bulmaca rakibini tek durum girdisi olarak tahta görüntüsüyle sınayın.**

Yazar oyunu Carbon'un kurduğunu ve oyuncuların beş seviyede API üzerinden Hydrogen ya da Gemini Decision 1 ile karşılaştığını söylüyor. İkisine de ızgara durumu olmadan tahta PNG'si gönderiliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-poster-9f9f7b5af31e.jpg" alt="Case 140 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121391300822081713-1-url-27dd30156905.mp4)

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-141"></a>
### Örnek 141: [Google Dokümanlar İçin Videolu Anlatım](https://x.com/nin222/status/2121395008863621390) (hazırlayan [@nin222](https://x.com/nin222))

**Mobil düzenlemeyi ekran görüntüleri ve numaralı işaretlerle anlatın.**

Yazar mobil Google Dokümanlar'da metin seçimi, stil, renk, yazı tipi ve kaydetmeyi gösteren kurguyu Hydrogen'a atfediyor. Örnek kareler işaretlemeleri gösteriyor. Kurgu yöntemi belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-poster-2bd2bc3867a6.jpg" alt="Case 141 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121395008863621390-1-url-6424ac72e0e7.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-146"></a>
### Örnek 146: [MZ-1500 İçin BASIC Ortamı](https://x.com/hiromsa/status/2121465784715338065) (hazırlayan [@hiromsa](https://x.com/hiromsa))

**Retro bir BASIC ortamı prototipleyin ve çevre birimi desteğini ayrı kontrol edin.**

Yazar demoyu Hydrogen'a atfediyor ve yaklaşık 15 dakika bildiriyor. PCG, PSG ve QuickDisk desteği listeleniyor. QuickDisk, LOAD ile sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-poster-514d7eb8e0ec.jpg" alt="Case 146 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-1-url-38fd35d47c21.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121465784715338065-2-url-b1ab2bf1fdbd.jpg" alt="Case 146 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-161"></a>
### Örnek 161: [Bir Dakikada HTML Nişancı Oyunu](https://x.com/SahilPanhotra/status/2121561371951399133) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Tek HTML dosyasıyla bir nişancı oyununun temel denetim ve geri bildirim döngüsünü sınayın.**

Yazar Hydrogen'ın tek istemden bir dakikanın altında oynanabilir oyun oluşturduğunu bildiriyor. Tek HTML dosyası kullanıldı ve çerçeve ya da kurulum adımı gerekmiyordu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-poster-fcaa05cc4504.jpg" alt="Case 161 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121561371951399133-1-url-3ec921912f0c.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-163"></a>
### Örnek 163: [AITuber OnAir'de Hydrogen ile Sohbet](https://x.com/shinshin86/status/2121571590442017094) (hazırlayan [@shinshin86](https://x.com/shinshin86))

**Live2D avatarının arkasındaki sohbet modeli olarak Hydrogen'ı deneyin.**

Projenin geliştiricisi AITuber OnAir'de Hydrogen desteğini duyuruyor ve Live2D dahil örnek sohbet avatarları sunuyor. Kayıt entegrasyonu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-poster-5281e35f0667.jpg" alt="Case 163 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121571590442017094-1-url-69f263303447.mp4)

Tür: Integration | Tarih: 2026-11-14

---

<a id="case-164"></a>
### Örnek 164: [Kodla Oluşturulan Tanıtım Videosu](https://x.com/xiangning0/status/2121594643540480293) (hazırlayan [@xiangning0](https://x.com/xiangning0))

**Kodlama modeline kısa bir tanıtım görevi verip hareketli grafikleri inceleyin.**

Yazar GPT-6.2 Astra temalı tanıtım videosunu gösteriyor ve Hydrogen'ın bunu yalnızca kodla ürettiğini söylüyor. Video kod tabanlı üretim akışını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-poster-66bb65c3f2ab.jpg" alt="Case 164 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121594643540480293-1-url-c768101e1c0d.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-173"></a>
### Örnek 173: [Jung'un Eşzamanlılığı Üzerine Sunum](https://x.com/soumyadesign/status/2121676345835241916) (hazırlayan [@soumyadesign](https://x.com/soumyadesign))

**İlgili kavramların açıkça anlatılması gereken bir konuyla slayt üretimini sınayın.**

Yazar Carl Jung'un eşzamanlılık ve nedensellik dışı düzen konulu sunumunu Hydrogen ve özel slayt aracına atfediyor. Aracı Antigravity'de geliştirdiğini söylüyor ve slaytları paylaşıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-1-url-da309a9b81ad.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-1-url-da309a9b81ad.jpg" alt="Case 173 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-2-url-04e00cd024a5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-2-url-04e00cd024a5.jpg" alt="Case 173 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-3-url-12da69202041.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-3-url-12da69202041.jpg" alt="Case 173 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-4-url-520c28ccff68.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121676345835241916-4-url-520c28ccff68.jpg" alt="Case 173 source image 4" width="100%"></a>
</td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-178"></a>
### Örnek 178: [Etkileşimli Mitokondri Motoru](https://x.com/SidraMiconi/status/2121745863827697687) (hazırlayan [@SidraMiconi](https://x.com/SidraMiconi))

**Etkileşimli bir şemayla moleküler hareketi ATP üretimiyle ilişkilendirin.**

Yazar Hydrogen High'ın tek istemle ATP sentaz uygulaması oluşturduğunu, sonradan kamera düzeltmesi yaptığını söylüyor. Geometri kryo-EM koordinatlarından geliyor ve hareket basitleştirilmiş.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-poster-1d0d387e5eb3.jpg" alt="Case 178 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121745863827697687-1-url-0663725beae5.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-179"></a>
### Örnek 179: [Qix Tarzı Alan Ele Geçirme Oyunu](https://x.com/UWhQC5DHKuVq/status/2121751941965562224) (hazırlayan [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq))

**Kısa bir arcade oyunu tarifiyle ilk çıktının etkileşimli döngü içerip içermediğini sınayın.**

Yazar ücretsiz Gemini arayüzünden Qix tarzı bir alan oyunu istedi ve demoyu paylaştı. Gönderide Hydrogen etiketi ve tek istek bilgisi yer alıyor.

**İstem:**

```
クイックス風の陣取りゲームを作って
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-poster-5f091be1128b.jpg" alt="Case 179 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121751941965562224-1-url-bff69f449366.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-180"></a>
### Örnek 180: [Hydrogen ile HTML Slaytları](https://x.com/yamachan_ai_log/status/2121772023710118043) (hazırlayan [@yamachan_ai_log](https://x.com/yamachan_ai_log))

**HTML üretimini sınarken slaytların görsel hiyerarşisini ve düzenini inceleyin.**

Yazar Hydrogen'ın oluşturduğu HTML slaytlarını gösteriyor ve çıktıyı hızlı ve ayrıntılı olarak nitelendiriyor. Kayıt sunumu gösteriyor. Karşılaştırmalı süre verilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-poster-f343fe9c12f0.jpg" alt="Case 180 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121772023710118043-1-url-f71ccad820be.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-185"></a>
### Örnek 185: [Dersten Kısa Videoya](https://x.com/smalkalbani/status/2121844887033458954) (hazırlayan [@smalkalbani](https://x.com/smalkalbani))

**Dersi videoya dönüştürürken anlatımın doğruluğunu ve temposunu kontrol edin.**

Yazar ders iş akışını Hydrogen'a atfediyor ve iki klip paylaşıyor. Videoyu hangi sistemin oluşturduğu belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-poster-3fbc11842915.jpg" alt="Case 185 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-1-url-0fc2657ea2ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-poster-37ec4aec60de.jpg" alt="Case 185 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121844887033458954-2-url-30af8d8f9be2.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-190"></a>
### Örnek 190: [Gemini Canvas'ta Blok Flüt Rehberi](https://x.com/nin222/status/2121877676042682538) (hazırlayan [@nin222](https://x.com/nin222))

**Notayı enstrüman yönergeleriyle eşleştiren alıştırma aracı için hızlı modu deneyin.**

Video Hydrogen'ın hızlı moduyla oluşturulan Canvas blok flüt rehberini gösteriyor. Yazar, aracın içe aktarılan notalardan da yapılabildiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-poster-d0d34c84341f.jpg" alt="Case 190 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121877676042682538-1-url-0765fe29b656.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-194"></a>
### Örnek 194: [Tek HTML Dosyasında TAJ VICE](https://x.com/SahilPanhotra/status/2121909681514074328) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Tek dosya sınırıyla gezilebilir harita prototipleyip kalan hataları sınayın.**

Yazar 12 saatten kısa oturumda Hydrogen ile kurgusal Agra'da geçen GTA esintili oyun geliştirdi. Saf JavaScript, bir HTML dosyası ve harici varlık kullanılmadığını belirtiyor. Oynanış hataları sürüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-poster-50008d63d16b.jpg" alt="Case 194 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121909681514074328-1-url-43f1bfbb5057.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-203"></a>
### Örnek 203: [Elle Çizilmiş Görünümlü Kamu Spotu](https://x.com/shengtang135754/status/2121965385356612020) (hazırlayan [@shengtang135754](https://x.com/shengtang135754))

**Bir kamu mesajıyla elle çizilmiş görsel üslubu değerlendirin.**

Yazar elle çizilmiş tarzda kısa kamu spotunu Gemini 4 Hydrogen'a atfediyor. Tek seferde üretim yazarın beyanı. Görüntüyü üreten model ve süreç açıklanmıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-poster-3eec12877e2f.jpg" alt="Case 203 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121965385356612020-1-url-d3f8ec0477b4.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-207"></a>
### Örnek 207: [Görselden React.gg Sitesini Yeniden Yapmak](https://x.com/thebuggeddev/status/2122019549117911473) (hazırlayan [@thebuggeddev](https://x.com/thebuggeddev))

**Referans görselden başlayıp hangi ayrıntıların düzenleme gerektirdiğini inceleyin.**

Yazar Hydrogen'a referans görsel verip React.gg'yi birkaç istemde yeniden oluşturduğunu bildiriyor. Demo bağlantısını paylaşıyor ve eşleşmenin kusursuz olmadığını belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-poster-961b1b6ad234.jpg" alt="Case 207 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122019549117911473-1-url-197d543cbceb.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-210"></a>
### Örnek 210: [Koşu Antrenörü Olarak Gemini](https://x.com/ivanleomk/status/2122036783307469199) (hazırlayan [@ivanleomk](https://x.com/ivanleomk))

**Antrenman kaydını önerilerle karşılaştırıp hedefleri başlangıç seviyenize göre ayarlayın.**

Yazar koşu koçluğunu Gemini Hydrogen'a atfediyor ve yaklaşık bir yıldaki en uzun koşusunu yaptığını bildirip antrenman ekran görüntüsünü paylaşıyor. Örnek kişisel deneyime dayanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122036783307469199-1-url-9894b3ee8ad6.jpg" alt="Case 210 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-211"></a>
### Örnek 211: [Zincir Üzerinde Skor Tutan Tarayıcı Oyunu](https://x.com/itshoseyn/status/2122063851143246140) (hazırlayan [@itshoseyn](https://x.com/itshoseyn))

**Masaüstü oyununu deneyin ve skor kaydını oynanıştan ayrı doğrulayın.**

Yazar Base üzerinde skor tutan Sheytonak oyununun yapımında Hydrogen kullandığını söylüyor. Masaüstü optimizasyonunu, mobildeki sorunları ve kalan hataları belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-poster-a37f5264e5a5.jpg" alt="Case 211 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122063851143246140-1-url-95d38e868999.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-213"></a>
### Örnek 213: [Japonca İstemden MIDI Üreten Beste Uygulaması](https://x.com/Awed_Urshy/status/2122161392828727738) (hazırlayan [@Awed_Urshy](https://x.com/Awed_Urshy))

**Japonca girdiyi MIDI, WAV ve piyano rulosuna dönüştüren bir aracı prototipleyin.**

Yazar Hydrogen ile kurulan uygulamanın Japonca girdiyi İngilizce müzik istemine çevirdiğini, MIDI yazdığını, WAV ve piyano rulosu videosu ürettiğini gösteriyor. Bunlar demo uygulamasının işlevleri.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-poster-3a598f17361f.jpg" alt="Case 213 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122161392828727738-1-url-8336bccf148d.mp4)

Tür: Demo | Tarih: 2026-11-16

---

<a id="case-215"></a>
### Örnek 215: [Tek Sayfalık Konser Özeti](https://x.com/fukubaya/status/2122215495474794640) (hazırlayan [@fukubaya](https://x.com/fukubaya))

**Etkinlik bilgisini kolay taranabilen görsel bir sayfaya dönüştürün.**

Yazar Batten Girls konserinin Japonca görsel özetini paylaşıp Hydrogen'a atfediyor. Kaynak malzemelerin ve istemin tamamı gösterilmiyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-1-url-d73e46e74edb.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-1-url-d73e46e74edb.jpg" alt="Case 215 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-2-url-2f2363fb51b2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122215495474794640-2-url-2f2363fb51b2.jpg" alt="Case 215 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-16

---

<a id="case-218"></a>
### Örnek 218: [Avatardan Günlük Yaşam Montajı](https://x.com/antiAIvo/status/2122251181112353276) (hazırlayan [@antiAIvo](https://x.com/antiAIvo))

**Tek avatar ve dört gündelik sahneyle kısa storyboard uyarlamasını değerlendirin.**

Yazar X avatarı ile ders çalışma, yemek, telefona bakma ve spor sahneleri verdi. Yaklaşık on saniyelik sonucu Hydrogen'a atfediyor. Görüntüyü üreten sistem belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-poster-a8276ba9e2e6.jpg" alt="Case 218 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122251181112353276-1-url-985770b40d3a.mp4)

Tür: Demo | Tarih: 2026-11-16

---

<a id="case-219"></a>
### Örnek 219: [Hydrogen ComfyUI Karakter Klibini Planlıyor](https://x.com/nyapan_mohy/status/2122253350808744004) (hazırlayan [@nyapan_mohy](https://x.com/nyapan_mohy))

**Kostümü ve arka planı sabit tutup video boyunca ifadeleri ve hareketleri değiştirin.**

Yazar klibin referans tasarıma göre planlanmasını Hydrogen'a atfediyor. Görüntü üretiminde ayrı bir ComfyUI MiniMax görselden videoya hattı kullanıyor. Yeni açılış karesi ve 30 çekimlik istem hazırlıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-poster-b2add96ffeee.jpg" alt="Case 219 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122253350808744004-1-url-1cb890463796.mp4)

Tür: Integration | Tarih: 2026-11-16

---

<a id="case-222"></a>
### Örnek 222: [Bir Şarkı İçin Geniş Ekran Görselleştirmesi](https://x.com/ivy432hz/status/2122283590180589791) (hazırlayan [@ivy432hz](https://x.com/ivy432hz))

**Şarkı ve çerçeve tarifi verip hareketin müziğin enerjisini nasıl taşıdığını inceleyin.**

Yazar Hydrogen XHigh'a sadece şarkı, 21:9 biçimi ve hız hissi isteği verdiğini söylüyor. Klip yolda hızlı ilerleyen görüntüler içeriyor. Görüntünün nasıl üretildiği açıklanmıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-poster-ede51f908440.jpg" alt="Case 222 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122283590180589791-1-url-21ea26419abd.mp4)

Tür: Demo | Tarih: 2026-11-16

---

<a id="case-224"></a>
### Örnek 224: [İki Tarihî Romantik Klipte Süreklilik](https://x.com/AvaSinclairAi_/status/2122315627113107670) (hazırlayan [@AvaSinclairAi_](https://x.com/AvaSinclairAi_))

**İkinci klipte devam ederken hangi ayrıntıların korunacağını belirtin.**

Yazar okyanus gemisindeki kısa romantik sahneyi Hydrogen kullanılan Gemini iş akışına atfediyor. İki bölümlü tarifte karakter ve kostüm sürekliliği isteniyor. Video modeli belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-poster-36bd5540bb16.jpg" alt="Case 224 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122315627113107670-1-url-fd0eb64a4c18.mp4)

Tür: Demo | Tarih: 2026-11-16

---


<a id="data-search"></a>
## 📊 E-tablolar ve Search

<a id="case-11"></a>
### Örnek 11: [Google Sheets'te hareketli manzara](https://x.com/Google/status/2121004369617485896) (hazırlayan [@Google](https://x.com/Google))

**Üretilen kodu ve hücre düzeyindeki güncellemeleri incelemek için alışılmadık bir e-tablo animasyonu kullanın.**

Google, Antigravity'de yazılan kodla e-tablo hücrelerine çizilmiş kıyı trenleri, bulutlar ve sonbahar yapraklarını gösteriyor. Bu resmî bir yaratıcı demodur, e-tablo performans kıyaslaması değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006-poster.jpg" alt="Case 11 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U006.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-12"></a>
### Örnek 12: [Folio etkileşimli veri sitesi](https://x.com/vamsibatchuk/status/2120996342923436188) (hazırlayan [@vamsibatchuk](https://x.com/vamsibatchuk))

**Küçük bir web prototipinde tanıtım sayfası düzenini etkileşimli veri görselleştirmeleriyle birleştirin.**

Bir Google DeepMind çalışanı, Google AI Studio ile oluşturulmuş Folio tarzı bir siteyi ve etkileşimli animasyonu sunuyor. Gönderi, tam üretim istemini veya bağımsız bir işlevsel testi sağlamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007-poster.jpg" alt="Case 12 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U007.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-13"></a>
### Örnek 13: [Çok parçalı arama sorularına görsel yanıtlar](https://x.com/Google/status/2120960715011883148) (hazırlayan [@Google](https://x.com/Google))

**Çok sayıda koşul içeren ayrıntılı bir arama isteğini test ederken yanıt düzenini ve kaynak bağlantılarını karşılaştırın.**

Google'ın Search örneği; niyet anlama, görsel düzenler, karşılaştırma tabloları ve sorgu dallandırmayı birleştiriyor. Bunlar sağlayıcının anlattığı ürün davranışlarıdır; demo, yayıncıların sıralamalarına veya trafiğine etkisini ortaya koymuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021-poster.jpg" alt="Case 13 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U021.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-14"></a>
### Örnek 14: [Sheets'te etkileşimli finansal tahmin](https://x.com/ChanduThota/status/2120942270627414079) (hazırlayan [@ChanduThota](https://x.com/ChanduThota))

**Varsayımları görünür bir finansal model prototipi oluşturun ve üretilen formülleri ve grafikleri inceleyin.**

Chandu Thota, Google Sheets'te bir tahmin demosu sunuyor. Kaynaktaki %30'dan fazla hızlı canvas üretimi iddiası sağlayıcıya aittir; bu depo için yapılmış kontrollü bir süre ölçümü değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047-poster.jpg" alt="Case 14 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U047.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-60"></a>
### Örnek 60: [Box Agent ile Karmaşık Kurumsal Belgeler](https://x.com/levie/status/2120947988143198302) (hazırlayan [@levie](https://x.com/levie))

**Gerçekçi bir belge iş yükünde doğruluk, çalışma süresi ve token kullanımını kontrol edin.**

Box erken erişim değerlendirmesinde, tipik bir görevde Gemini 3.8 Flash'a göre doğruluğun beş puan arttığını, sürenin yarıdan aza indiğini ve yaklaşık %12 daha az token kullanıldığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120947988143198302-1-url-656beeac65cd.jpg" alt="Case 60 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-74"></a>
### Örnek 74: [Workspace Verilerinden Grafik ve Rapor](https://x.com/nin222/status/2120989168247652674) (hazırlayan [@nin222](https://x.com/nin222))

**Eksik analiz, grafik veya rapor çıktısını bir takip isteminin tamamlayıp tamamlamadığını kontrol edin.**

Yazar, Workspace for Education Fundamentals demosunda Hydrogen ile veri analiz edip grafik ve rapor dosyası oluşturdu. İki tur gerektiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-poster-f746d8b7fb16.jpg" alt="Case 74 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-2-url-f47ce3b229ec.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120989168247652674-1-url-870f082b495e.jpg" alt="Case 74 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-81"></a>
### Örnek 81: [Google E-Tablolar'da Gemini ile Piksel Sanatı](https://x.com/kkitase/status/2121041283640926401) (hazırlayan [@kkitase](https://x.com/kkitase))

**Gemini seçeneklerini aynı Google E-Tablolar çizim göreviyle karşılaştırın.**

Yazar Hydrogen'ın Google E-Tablolar'da piksel sanatı çizmesini gösteriyor ve Antigravity Orchestrator, Carbon ile Argon çalışmalarına bağlantı veriyor. Gösterimde biçimsel puanlama yok.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-poster-4749e9ea9413.jpg" alt="Case 81 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121041283640926401-1-url-2e5af0096256.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-148"></a>
### Örnek 148: [Etkileşimli FAA Yer Durdurma Haritası](https://x.com/SidraMiconi/status/2121486870341370204) (hazırlayan [@SidraMiconi](https://x.com/SidraMiconi))

**Operasyon durdurması bitince kuyruğun neden sürdüğünü zaman çizelgesi ve haritayla gösterin.**

Yazar Hydrogen ile FAA aksaklık haritasını 222 saniyede kurduğunu ve bir etiketi düzelttiğini bildiriyor. Zaman çizelgesi resmi raporları izliyor. Trafik, tipik sefer saatleriyle simüle ediliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-poster-707bfd6135da.jpg" alt="Case 148 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121486870341370204-1-url-75faddf0e5e6.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-184"></a>
### Örnek 184: [Chrome'da Yapılandırılmış YouTube Özeti](https://x.com/studio_yebisu/status/2121835594674561098) (hazırlayan [@studio_yebisu](https://x.com/studio_yebisu))

**Chrome'daki Gemini panelinden zaman damgalı özet ve kaynaklı arka plan isteyin.**

Japonca gönderi, Chrome'da açık YouTube videosunun Gemini ile özetlenmesini gösteriyor. Yayımlanan istem kısa özet, ana noktalar, bölüm akışı, kaynaklı arka plan, olgusal çekinceler ve ek kaynaklar istiyor.

**İstem:**

```
今開いている動画の内容を、初めて見る人にも分かるように要約してください。

# 出力の構成
1. **ひとことで**：この動画が何を伝えているかを1〜2文で。
2. **要点**：重要なポイントを5〜8個の箇条書きで。可能ならタイムスタンプ（例 03:12）を付ける。
3. **詳しい流れ**：話の展開を章ごとに整理。専門用語は初出時にかみ砕いて説明する。
4. **関連情報**：動画内で触れられた人物・製品・研究・出来事について、背景知識や最新の関連情報をWebから補足する。動画内の情報と外部情報ははっきり区別し、外部情報には出典URLを付ける。
5. **注意点**：動画の主張で事実と異なる・古い・議論がある部分があれば指摘する。
6. **さらに知りたい人へ**：次に読む・見るとよいリソースを3つ。

# ルール
- 日本語で、中学生にも伝わる平易な言葉で書く。
- 推測で埋めず、動画で言っていないことは「動画内では言及なし」と書く。
- 数字・固有名詞は正確に残す。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-poster-1c98bb7de426.jpg" alt="Case 184 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121835594674561098-1-url-3df49e47a1b9.mp4)

Tür: Tutorial | Tarih: 2026-11-15

---


<a id="interactive-3d"></a>
## 🎮 Etkileşimli 3B ve arayüzler

<a id="case-15"></a>
### Örnek 15: [Etkileşimli bir yemek odası](https://x.com/notjazii/status/2120979811569222137) (hazırlayan [@notjazii](https://x.com/notjazii))

**Bir sahneyi sabit görselden değerlendirmek yerine nesne etkileşimlerini, aydınlatmayı ve durum değişikliklerini kontrol edin.**

Üretici; ışıkları, lambaları, buzdolabı ve içindeki nesneleri etkileşimli olan bir yemek odası gösteriyor. Bildirilen 30 dakikalık geliştirme süresi bağımsız olarak doğrulanmadı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014-poster.jpg" alt="Case 15 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U014.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-16"></a>
### Örnek 16: [Minyatür dünyalı bir ses kaydırıcısı](https://x.com/vib3coded/status/2120973294090555890) (hazırlayan [@vib3coded](https://x.com/vib3coded))

**Hem etkileşim tasarımını hem de hareketli sahnenin ayrıntılarını test etmek için tanıdık bir kontrol kullanın.**

Kaynak, küçük bir Japon tarzı dünyayı hareketlendiren ses kaydırıcısını gösteriyor. Üretici $0.19 maliyet bildiriyor ancak fatura veya tam üretim iş akışı sunmuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016-poster.jpg" alt="Case 16 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U016.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-17"></a>
### Örnek 17: [Three.js ile bir Japon evi](https://x.com/SPAC89/status/2120972954146140409) (hazırlayan [@SPAC89](https://x.com/SPAC89))

**Ayrıntılı bir 3B gezintiyi değerlendirirken kod üretimini görüntüleme süresinden ayırın.**

Üretici, bu ev ve bahçeyi ajan kullanmadan Three.js ile çalışan Hydrogen'a atfediyor. Gönderideki abonelik kullanımı ve iki saatten kısa süre iddiaları yazarın kurulumuna özgüdür; genel fiyat veya gecikme garantileri değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017-poster.jpg" alt="Case 17 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U017.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-18"></a>
### Örnek 18: [3B bisiklet süren pelikan](https://x.com/nehstrr3/status/2120953932692537722) (hazırlayan [@nehstrr3](https://x.com/nehstrr3))

**Koordinasyonu, hareketi ve sahne tutarlılığını incelemek için hareketli bir karakter kullanın.**

Üretici, bisiklet süren bir 3B pelikan animasyonu sunuyor ve modeli Hydrogen XHigh olarak belirtiyor. Gönderi bir çıktı demosudur; tam, tekrarlanabilir bir istem veya fizik doğrulaması değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029-poster.jpg" alt="Case 18 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U029.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-19"></a>
### Örnek 19: [Önce planlanan bir gezegen simülatörü](https://x.com/The_Alex/status/2120950301318582643) (hazırlayan [@The_Alex](https://x.com/The_Alex))

**Karmaşık bir sahneyi düzenlemesini istemeden önce kodlama modeline somut bir plan verin.**

Erken erişimli üretici bir gezegen simülatörü gösteriyor ve daha ayrıntılı planlar verdikten sonra düzenleme sonuçlarının iyileştiğini bildiriyor. Kaynak, fikri ForwardEditor'a atfediyor ve yinelemeli bir iş akışı anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033-poster.jpg" alt="Case 19 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U033.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-20"></a>
### Örnek 20: [Antigravity Swarm ile liman adası](https://x.com/ai_for_success/status/2120942147780464660) (hazırlayan [@ai_for_success](https://x.com/ai_for_success))

**Çok ajanlı sahne oluşturma davranışını incelemek için gezilebilir küçük bir ortam kullanın.**

Üretici erken erişimi açıkladı ve Antigravity'nin Swarm özelliği içinde Hydrogen ile oluşturulmuş bir liman adası gösteriyor. Herkese açık gönderi, tüm orkestrasyonu veya istem geçmişini belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048-poster.jpg" alt="Case 20 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U048.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-21"></a>
### Örnek 21: [Eyfel Kuleli yüzen ada](https://x.com/RezAIT00/status/2120940988780736973) (hazırlayan [@RezAIT00](https://x.com/RezAIT00))

**Kompakt bir anıt sahnesinde kompozisyonu, kamera hareketini ve modelin ürettiği kodu değerlendirin.**

Kaynak, Eyfel Kuleli minyatür bir ada gösteriyor ve bunu Hydrogen XHigh'a atfediyor. Altı dakikalık oluşturma ve kayıt süresi yazarın bildirimidir, bağımsız bir süre testi değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051-poster.jpg" alt="Case 21 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U051.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-22"></a>
### Örnek 22: [Uçarak gezilebilen fütüristik şehir](https://x.com/kimmonismus/status/2120940617169826037) (hazırlayan [@kimmonismus](https://x.com/kimmonismus))

**İlk çıktının nihai olduğunu varsaymak yerine prosedürel bir dünyada sonraki düzenlemeleri test edin.**

Erken erişimli üretici Antigravity'de Hydrogen High kullandı; prosedürel kuleler, yağmur ve uçan trafik içeren Three.js şehrini bir ek istemle oluşturduğunu bildiriyor. Kayıt, üretilen kodun çalışmasını gösteriyor; yerel video üretimini değil.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054-poster.jpg" alt="Case 22 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U054.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-23"></a>
### Örnek 23: [Gün doğumundan geceye bir deniz uçağı](https://x.com/LuminaBench/status/2120939312564842663) (hazırlayan [@LuminaBench](https://x.com/LuminaBench))

**Etkileşimli bir 3B sahnede ortam kontrollerini ve ışık geçişlerini inceleyin.**

LuminaBench'in daha sonra Google tarafından yeniden paylaşılan özgün demosu, bir deniz uçağını ve günün değişen saatlerini gösteriyor. Gönderi, kayıtlı herkese açık yayın sınırından önceye aittir; erişim yolu ve model çağrısı bağımsız olarak doğrulanmadı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056-poster.jpg" alt="Case 23 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U056.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-41"></a>
### Örnek 41: [Uzay Görsellerinden HTML Sahnesine](https://x.com/Inmerson/status/2120482539907559651) (hazırlayan [@Inmerson](https://x.com/Inmerson))

**Az sayıda referansla, oluşturulan sahnenin ayırt edilebilir bir görsel üslup taşıyıp taşımadığını sınayın.**

Yazar uzay görselleştirmesini Hydrogen'a atfediyor. Kaynak, modele verilen gezegen görsellerini ve bunlardan üretilen halkalı gezegenli HTML sahnesini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-poster-e95d77f11c96.jpg" alt="Case 41 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-1-url-a3d0ecad78f9.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120482539907559651-2-url-ac359bf02698.png" alt="Case 41 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-11

---

<a id="case-42"></a>
### Örnek 42: [Gemini Canvas'ta Formula 1 Prototipi](https://x.com/auricxofficial/status/2120843585914605830) (hazırlayan [@auricxofficial](https://x.com/auricxofficial))

**Üretilen araç modelini farklı açılardan incelemek için birkaç kamera görünümü ekleyin.**

Yazar Formula 1 tarzı araç görüntüleyicisini Gemini Canvas'taki ilk Hydrogen denemesine atfediyor. Kayıt, kamera ön ayarlarını ve süspansiyon görünümlerini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-poster-14ad77bd5166.jpg" alt="Case 42 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120843585914605830-1-url-5efdb224d3f1.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-48"></a>
### Örnek 48: [SVG Olarak BMW Yan Profili](https://x.com/HarshithLucky3/status/2120932649938382894) (hazırlayan [@HarshithLucky3](https://x.com/HarshithLucky3))

**Oranları, silüeti ve küçük ayrıntıları bir aracın SVG yan görünümünden inceleyin.**

Yazar BMW M4 CS'nin SVG yan görünümünü Gemini uygulamasındaki Hydrogen High'a atfediyor ve üretim süresinin 30 saniyenin altında olduğunu bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120932649938382894-1-url-93db64dda108.jpg" alt="Case 48 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-49"></a>
### Örnek 49: [Bir Gökbilimcinin Yüzen Adası](https://x.com/pankajkumar_dev/status/2120933196221333791) (hazırlayan [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Küçük bir sahneye belirgin bir tema verip nesnelerin ve ışığın bunu nasıl desteklediğini inceleyin.**

Yazar yüzen gökbilimci adasını Arena'da Hydrogen olarak etiketlenen bir sürüme atfediyor. Bu çalıştırmanın dört dakika sürdüğünü bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-poster-090959832e16.jpg" alt="Case 49 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120933196221333791-1-url-275f272023e6.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-50"></a>
### Örnek 50: [Referans Görselden Gezilebilir 3B Manzaraya](https://x.com/HarshithLucky3/status/2120935535422374055) (hazırlayan [@HarshithLucky3](https://x.com/HarshithLucky3))

**Görselden oluşturulan sahnenin hem referansa sadakatini hem de hareket olanağını sınayın.**

Yazar Gemini uygulamasında Hydrogen'a atfettiği oynanabilir 3B manzarayı paylaşıyor. GLSL yansımaları, prosedürel geometri ve yüzme fiziğini tarif ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-poster-0a62be25ae44.jpg" alt="Case 50 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120935535422374055-1-url-e1277d4c0c7d.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-51"></a>
### Örnek 51: [3B Bloklardan Minyatür Diorama](https://x.com/abhinavflac/status/2120936501961969990) (hazırlayan [@abhinavflac](https://x.com/abhinavflac))

**Bloklarla kurulan bir minyatürde şekillerin bütünlüklü bir sahne oluşturup oluşturmadığına bakın.**

Yazar 3B bloklardan oluşan minyatür dioramanın kaydını paylaşıp Hydrogen'a atfediyor. Süre ve kurulum ayrıntıları belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-poster-25873d1c834e.jpg" alt="Case 51 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936501961969990-1-url-aa174a0a5ff2.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-52"></a>
### Örnek 52: [Etkileşimli Kiraz Çiçeği Ağacı](https://x.com/hakmgpt/status/2120936640436642231) (hazırlayan [@hakmgpt](https://x.com/hakmgpt))

**Tek bir hareketli nesne ve birkaç denetimle küçük bir sahnedeki anlık değişiklikleri keşfedin.**

Yazar ekran görüntüsündeki kiraz çiçeği ağacı arayüzünü Hydrogen'a atfediyor. Görüntüde sahne ayarları yer alıyor. Uygulama ayrıntıları belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120936640436642231-1-url-9fc060f764a0.jpg" alt="Case 52 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-62"></a>
### Örnek 62: [Küçük Bir Etkileşimli Animasyonda Kırılma](https://x.com/chanelluuh/status/2120951519470399710) (hazırlayan [@chanelluuh](https://x.com/chanelluuh))

**Sahneyi büyütmeden önce optik bir etkiyi kısa önizlemelerle iyileştirin.**

Yazar Small Delights serisindeki küçük bir animasyonu Hydrogen'a atfediyor ve ışık kırılmasına dikkat çekiyor. Kaynak yinelemeli bir tasarım sürecini anlatıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-poster-4641e47771de.jpg" alt="Case 62 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120951519470399710-1-url-3f4fd8b34ad6.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-63"></a>
### Örnek 63: [Yokuş Yukarı Akan Nehir](https://x.com/xKaka1456/status/2120952404225265983) (hazırlayan [@xKaka1456](https://x.com/xKaka1456))

**Alışılmadık bir hareket yönüyle küçük bir sahne kurup görsel etkiyi inceleyin.**

Yazar ters yönde akan nehri web üzerinde Hydrogen ile oluşturduğunu bildiriyor ve kaydı paylaşıyor. Süre ve kota kullanımı yazarın gözlemleri.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-poster-b05f2228bb87.jpg" alt="Case 63 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120952404225265983-1-url-8a4b34fd66b9.mp4)

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-67"></a>
### Örnek 67: [Hydrogen ile 3B Portre](https://x.com/soyamiruku/status/2120959893943251322) (hazırlayan [@soyamiruku](https://x.com/soyamiruku))

**Üç boyutlu bir gösterimde kişinin tanınabilirliğini portreyle sınayın.**

Yazar, gönderide seslendiği kişinin 3B portresini Hydrogen'a atfediyor ve görseli paylaşıyor. Kurulumla ilgili bilgi sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120959893943251322-1-url-80696f60a4dd.jpg" alt="Case 67 source image 1" height="360"></a>

Tür: Demo | Tarih: 2026-11-12

---

<a id="case-82"></a>
### Örnek 82: [Referans Görselden Daire Maketinin Baskısına](https://x.com/bijanbowen/status/2121042010928709932) (hazırlayan [@bijanbowen](https://x.com/bijanbowen))

**Görselden 3B model üretme testini fiziksel baskıya kadar götürün.**

Yazar, Seinfeld dairesinin referans görselini ve Hydrogen'a atfettiği modelin fiziksel baskısını paylaşıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-1-url-c8d62f93f433.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-1-url-c8d62f93f433.jpg" alt="Case 82 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-2-url-e864ca91b00a.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121042010928709932-2-url-e864ca91b00a.png" alt="Case 82 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-86"></a>
### Örnek 86: [Golden Merry Gemi Sahnesi](https://x.com/xKaka1456/status/2121063351136739388) (hazırlayan [@xKaka1456](https://x.com/xKaka1456))

**Tanıdık bir kurmaca gemiyle deniz sahnesinin görsel düzenini sınayın.**

Yazar, mavi sulardaki Golden Merry klibini Hydrogen'a atfediyor. Paylaşım istemi, araç ayarlarını ve yineleme sayısını belirtmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-poster-1f43c24bfc6f.jpg" alt="Case 86 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121063351136739388-1-url-92fbdad95f56.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-88"></a>
### Örnek 88: [Bulutların İçinde Hareket Eden Balina](https://x.com/xKaka1456/status/2121100318150898144) (hazırlayan [@xKaka1456](https://x.com/xKaka1456))

**Kodla üretilen bir hayvan sahnesinde akıcı hareketi ve göz tasarımını ayrı değerlendirin.**

Kaynak, bulutların arasında hareket eden kodla oluşturulmuş balinayı gösteriyor ve yaklaşık iki dakikalık Hydrogen çalıştırması bildiriyor. Süre ve kota yazarın gözlemlerine dayanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-poster-f2a1fabe0691.jpg" alt="Case 88 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121100318150898144-1-url-da7c503b38d6.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-92"></a>
### Örnek 92: [Gemini Canvas'ta Bir Su Altı Şehri](https://x.com/ayyh_18/status/2121128385690693821) (hazırlayan [@ayyh_18](https://x.com/ayyh_18))

**Küçük bir 3B sahneden başlayıp birkaç turda gezilebilir alanlar ve hareketli canlılar ekleyin.**

Yazar, Gemini uygulamasında birden çok istemle balık, denizanası, mercan ve gezilebilir cam kubbeler içeren su altı şehri oluşturuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-poster-1c2dd80e7d93.jpg" alt="Case 92 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121128385690693821-1-url-abbcbd1a1795.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-99"></a>
### Örnek 99: [Three.js ile Gri Tonlu Korsan Gemisi](https://x.com/parves075/status/2121172856889618528) (hazırlayan [@parves075](https://x.com/parves075))

**Three.js sahnesini gri tonla sınırlayıp ışığın geometriyi görünür kılıp kılmadığını sınayın.**

Yazar Antigravity'de Hydrogen kullanarak Three.js ile gri tonlarda bir korsan gemisi oluşturdu. Kayıt, aydınlatma ve 3B ayrıntı testini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-poster-cd20b0b09126.jpg" alt="Case 99 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172856889618528-1-url-f14effc1f3e9.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-101"></a>
### Örnek 101: [CadXStudio'da Parametrik Masa Lambası](https://x.com/CadX_Studio/status/2121175785356853312) (hazırlayan [@CadX_Studio](https://x.com/CadX_Studio))

**Oluşturulan CAD modelinin parça ölçülerini ve düzenlenebilirliğini inceleyin.**

CadXStudio tarayıcıda çalışan bir masa lambası modelini gösteriyor ve 35 düzenlenebilir parça bildiriyor. Örnek araç sağlayıcısından geliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-poster-50c852bb5b0d.jpg" alt="Case 101 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121175785356853312-1-url-50e02ffe9028.mp4)

Tür: Integration | Tarih: 2026-11-13

---

<a id="case-102"></a>
### Örnek 102: [C++ ile Tapınak Yolu Animasyonu](https://x.com/nehstrr3/status/2121184399245128137) (hazırlayan [@nehstrr3](https://x.com/nehstrr3))

**Modelin web altyapısı olmadan çalışan animasyon yazmasını küçük bir yerel sahneyle sınayın.**

Yazar tapınak kapılarının altındaki yol animasyonunu Extra High ayarında Hydrogen'a atfediyor ve uygulama dili olarak C++'ı belirtiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-poster-222bc49a850f.jpg" alt="Case 102 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121184399245128137-1-url-60e96c14023c.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-105"></a>
### Örnek 105: [30 Modülden Kurulan Kasaba Sahnesi](https://x.com/IamEmily2050/status/2121200010574598655) (hazırlayan [@IamEmily2050](https://x.com/IamEmily2050))

**Sahneyi istemlerle ayrı modüller halinde oluşturup birleşik görünümü inceleyin.**

Yazar Gemini uygulamasındaki Hydrogen High'ı kullandığını ve 30 modülün her biri için bir istem verdiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-poster-398726e1e490.jpg" alt="Case 105 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121200010574598655-1-url-361f3f7b6eef.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-108"></a>
### Örnek 108: [Yüzen Adada Postane](https://x.com/pankajkumar_dev/status/2121220537984954448) (hazırlayan [@pankajkumar_dev](https://x.com/pankajkumar_dev))

**Küçük bir bina tarif edip malzeme ve ışığın sahneye katkısını inceleyin.**

Yazar Hydrogen'dan yüzen adada minyatür 3B postane istedi. Paylaştığı kayıtta dokuları, renkleri ve ışığı öne çıkarıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-poster-adfc27d33c10.jpg" alt="Case 108 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121220537984954448-1-url-78a0c86fd68a.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-110"></a>
### Örnek 110: [Koi Courtyard'da Su ve Balıklar](https://x.com/SahilPanhotra/status/2121225566779023432) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Hareketli balıklar içeren sahnede yüzey yansımalarıyla su ışığının tutarlılığını inceleyin.**

Yazar Koi Courtyard testinin Hydrogen sürümünde ışık desenlerini, yansımaları ve balık davranışını vurguluyor. Carbon sürümünü bağlam için iliştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-poster-c0518105ec77.jpg" alt="Case 110 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121225566779023432-1-url-4910808043a6.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-112"></a>
### Örnek 112: [Gemini Uygulamasında Canlı 3B Sahne](https://x.com/YxzRainy/status/2121232725185339869) (hazırlayan [@YxzRainy](https://x.com/YxzRainy))

**Gemini web arayüzünde etkileşimli ışık ve parçacıklar prototipleyin.**

Yazar parçacıklar, hareketli aydınlatma ve gerçek zamanlı denetimler içeren Hydrogen sahnesini gösteriyor. Kayıtta sahne Gemini tarayıcı arayüzünde çalışıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-poster-badf3377669f.jpg" alt="Case 112 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121232725185339869-1-url-806d7c3d3e00.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-115"></a>
### Örnek 115: [Tek HTML Dosyasında Pembe 3B Sahne](https://x.com/SahilPanhotra/status/2121254256288137484) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Harici varlık kullanmadan Three.js sahnesi kurup kompozisyonun anlaşılabilirliğini inceleyin.**

Yazar pembe sahneyi Hydrogen'a atfediyor ve harici varlık olmadan tek HTML dosyasında Three.js kullandığını bildiriyor. Bağlantıdaki Koi Courtyard ayrı bir proje.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-poster-a70fc446f836.jpg" alt="Case 115 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121254256288137484-1-url-ea3fb51baca8.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-119"></a>
### Örnek 119: [Yalnızca Kodla Büyük Patlama Simülasyonu](https://x.com/ash_twtz/status/2121268140630000020) (hazırlayan [@ash_twtz](https://x.com/ash_twtz))

**Kısa bir animasyonla görsel bir açıklama tasarlayıp bilimsel çerçevesini kontrol edin.**

Yazar Gemini uygulamasındaki Hydrogen'a 15 saniyelik Büyük Patlama görselleştirmesini atfediyor. Tamamen kodla üretildiğini ve web, doku, harici varlık ya da 3B model kullanılmadığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-poster-05c7c24a6a02.jpg" alt="Case 119 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121268140630000020-1-url-bca0cbbebd56.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-120"></a>
### Örnek 120: [Patlatılmış Montaj Görünümlü Helikopter](https://x.com/LuminaBench/status/2121273297715277930) (hazırlayan [@LuminaBench](https://x.com/LuminaBench))

**3B prototipte uçuş denetimlerinin faydalı inceleme görünümleriyle bir araya gelip gelmediğini sınayın.**

Yazar uçurulabilir helikopteri, montaj görünümünü ve patlatılmış görünümleri gösteriyor. Prototipi yüksek akıl yürütme ayarındaki Hydrogen'a atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-poster-0dd4c07704e0.jpg" alt="Case 120 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121273297715277930-1-url-2427547981d5.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-121"></a>
### Örnek 121: [Röntgen ve Tel Kafes Görünümlü Hydrogen Express](https://x.com/LuminaBench/status/2121277060983234788) (hazırlayan [@LuminaBench](https://x.com/LuminaBench))

**Denetlenebilir 3B prototipe birden fazla inceleme modu ekleyin.**

Yazar hız denetimleri, patlatılmış görünüm, tel kafes ve röntgen modları olan bir tren gösteriyor. Çalıştırma için yaklaşık beş dakika bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-poster-fa3770c151ce.jpg" alt="Case 121 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121277060983234788-1-url-03df48153635.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-122"></a>
### Örnek 122: [Gökyüzünde Yakıt İstasyonu](https://x.com/doe_naps/status/2121279837512106168) (hazırlayan [@doe_naps](https://x.com/doe_naps))

**Davranışını demoda görünür kılmak için sahneye hareketli nesneler ve değişen ışık ekleyin.**

Yazar Hydrogen ile kurulan gökyüzü istasyonunu, retro uçan arabayı, dönen türbinleri ve gece gündüz geçişini gösteriyor. Tek üretim bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-poster-2720fcb1e865.jpg" alt="Case 122 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121279837512106168-1-url-61cb581d732d.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-129"></a>
### Örnek 129: [Tek HTML Dosyasında Su Değirmeni](https://x.com/NovaXCode/status/2121294356875509851) (hazırlayan [@NovaXCode](https://x.com/NovaXCode))

**Hızlı bir 3B prototipi, hareketi fark edilen nesnelere sahip küçük bir manzarayla sınayın.**

Yazar Hydrogen'ın kayıttaki su değirmeni sahnesini tek HTML dosyasında yaklaşık 30 saniyede oluşturduğunu bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-poster-da35067b1ffb.jpg" alt="Case 129 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121294356875509851-1-url-b31fc6ad9e68.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-132"></a>
### Örnek 132: [Hydrogen Extra ile Blender Sahnesi](https://x.com/SPAC89/status/2121302218347270625) (hazırlayan [@SPAC89](https://x.com/SPAC89))

**Görsel ayrıntıları artırmadan önce Blender'da geometriyi ve malzemeleri denetleyin.**

Yazar Hydrogen Extra'ya atfettiği Blender sahnesini gösteriyor ve bu oturumdaki abonelik kotası kullanımını tahmin ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-poster-f6986f7f3e1a.jpg" alt="Case 132 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302218347270625-1-url-129cfdd60422.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-139"></a>
### Örnek 139: [Hydrogen ile İki Parçacık Animasyonu](https://x.com/gwammyy/status/2121355401392189746) (hazırlayan [@gwammyy](https://x.com/gwammyy))

**Basit görsel efektlerde şekil ve hareketi iki farklı parçacık sahnesiyle inceleyin.**

Yazar iki kısa parçacık efekti kaydını Hydrogen'a atfediyor. Çıktılar gösteriliyor, kurulum ayrıntısı belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-poster-6d5849ed3509.jpg" alt="Case 139 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-1-url-855891f71efa.mp4)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-poster-2088c860ef2d.jpg" alt="Case 139 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121355401392189746-2-url-70df27eea019.mp4)

Tür: Demo | Tarih: 2026-11-13

---

<a id="case-142"></a>
### Örnek 142: [Minyatür Dünyada Gece Gündüz Düğmesi](https://x.com/vib3coded/status/2121398359395283027) (hazırlayan [@vib3coded](https://x.com/vib3coded))

**Arayüz durumları arasındaki geçişin akıcılığını basit bir düğmeyle sınayın.**

Yazar düğmeyle kontrol edilen gece gündüz geçişini gösteriyor ve geliştirme için 0,21 USD harcadığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-poster-b72941c84e2a.jpg" alt="Case 142 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121398359395283027-1-url-f38bd83bdc37.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-143"></a>
### Örnek 143: [65 Modülde Bir Çevre Kurmak](https://x.com/IamEmily2050/status/2121400396002492781) (hazırlayan [@IamEmily2050](https://x.com/IamEmily2050))

**Oluşturulan sahne büyüdükçe yapım süresini ve birleştirme işini izleyin.**

Yazar Gemini uygulamasında her biri bir istemle oluşturulan 65 modül bildiriyor ve sonucun kaydını paylaşıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-poster-2f86aa69648d.jpg" alt="Case 143 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121400396002492781-1-url-216ccb32f42f.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-149"></a>
### Örnek 149: [Minyatür Pagoda Bahçesi](https://x.com/auricxofficial/status/2121498286926540970) (hazırlayan [@auricxofficial](https://x.com/auricxofficial))

**Minyatürde mimari ile çevre düzenlemesinin uyumunu inceleyin.**

Yazar blok tarzı pagoda ve bahçe klibini Hydrogen'a atfediyor. Kayıt çıktıyı gösteriyor, uygulama ayrıntıları belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-poster-fe045f64e09d.jpg" alt="Case 149 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121498286926540970-1-url-2ba69f8c98cf.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-153"></a>
### Örnek 153: [II. Dünya Savaşı Havaalanı Dioraması](https://x.com/doe_naps/status/2121508105947320688) (hazırlayan [@doe_naps](https://x.com/doe_naps))

**Görünüşün yanı sıra işlevi sınamak için 3B demoya görsel referanslar ve mekanik hareket gereksinimleri verin.**

Yazar Hydrogen'a referanslar ve kısa bir tarifle tek HTML dosyasında havaalanı dioraması yaptırdığını bildiriyor. Görev, hareket edebilen uçak ve tank gerektiriyordu.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-poster-b8c274bcb597.jpg" alt="Case 153 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121508105947320688-1-url-61f1174a04fb.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-167"></a>
### Örnek 167: [Prosedürel Kızılgerdan Animasyonu](https://x.com/LuminaBench/status/2121620820791562291) (hazırlayan [@LuminaBench](https://x.com/LuminaBench))

**Oluşturulan uçuş animasyonunda kanat ve gövde hareketlerini inceleyin.**

Yazar kızılgerdan uçuş animasyonunun kodunu Hydrogen'a atfediyor. Bir takip paylaşımı aynı çalışma için ayrı Antigravity Swarm grafiğini gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-poster-2cfd31ca974a.jpg" alt="Case 167 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121620820791562291-1-url-424c6739108a.mp4)

Tür: Demo | Tarih: 2026-11-14

---

<a id="case-182"></a>
### Örnek 182: [Tek HTML Dosyasında İllüstrasyon](https://x.com/vamsibatchuk/status/2121788887823778297) (hazırlayan [@vamsibatchuk](https://x.com/vamsibatchuk))

**Görsel referansın harici varlık olmadan kodla yeniden oluşturulup oluşturulamadığını sınayın.**

DeepMind çalışanı tek dosyalık illüstrasyonu gösteriyor. Kütüphane, görsel üretici, beceri paketi veya gömülü varlık kullanılmadığını söylüyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-1-url-1de77cd76ae3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-1-url-1de77cd76ae3.jpg" alt="Case 182 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-2-url-5e02ddf0aad5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-2-url-5e02ddf0aad5.jpg" alt="Case 182 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-3-url-3da151834158.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-3-url-3da151834158.jpg" alt="Case 182 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-4-url-3c008316ab34.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121788887823778297-4-url-3c008316ab34.jpg" alt="Case 182 source image 4" width="100%"></a>
</td>
</tr>
</table>

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-186"></a>
### Örnek 186: [Durağan Sahneden Deniz Papağanı Animasyonu](https://x.com/vamsibatchuk/status/2121846407950639541) (hazırlayan [@vamsibatchuk](https://x.com/vamsibatchuk))

**Mevcut HTML sahnesini prosedürel animasyonun ilk karesi olarak kullanın.**

Yazar Hydrogen'dan tek HTML dosyasında 50 karelik bir devam animasyonu istedi. Klipte deniz papağanı karakterin şapkasını alıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-poster-4bb36cbf242d.jpg" alt="Case 186 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121846407950639541-1-url-28a319f0aec4.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-200"></a>
### Örnek 200: [Tek İstemden 3B Minyatür Ada](https://x.com/CodeByPoonam/status/2121952483132289270) (hazırlayan [@CodeByPoonam](https://x.com/CodeByPoonam))

**Tek çalıştırmada suyun, arazinin ve önemli noktaların anlaşılır biçimde yerleştirilip yerleştirilmediğini sınayın.**

Yazar adayı tek istemle Hydrogen'ın kurduğunu bildiriyor. Görselde binalar ve başka işaret noktaları var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-poster-aba21df1cc20.jpg" alt="Case 200 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121952483132289270-1-url-c9517769a98e.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-208"></a>
### Örnek 208: [Tekillik Temalı Etkileşimli Panel](https://x.com/Moleh1ll/status/2122032596263776351) (hazırlayan [@Moleh1ll](https://x.com/Moleh1ll))

**Tek bir görsel fikir etrafında kısa etkileşimli akış prototipleyin.**

Yazar Hydrogen'a atfettiği tekillik temalı paneli paylaşıyor. Kayıt sonucu gösteriyor. Uygulama bağlamı sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-poster-659c4681b977.jpg" alt="Case 208 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122032596263776351-1-url-89b2278022aa.mp4)

Tür: Demo | Tarih: 2026-11-15

---

<a id="case-225"></a>
### Örnek 225: [Gemini Uygulamasında Su Küresi](https://x.com/Google/status/2122366286659289502) (hazırlayan [@Google](https://x.com/Google))

**Basit bir optik sahneyle parlak noktaların ve kırılmanın ilişkisini inceleyin.**

Google, Hydrogen yazılı su benzeri küreyi Gemini uygulamasında gösteriyor ve Hydrogen'a atfediyor. Kaynak sonucu gösteriyor, görüntü oluşturma düzeneğini açıklamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-poster-37e4e965f3ec.jpg" alt="Case 225 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122366286659289502-1-url-983330c4af5c.mp4)

Tür: Demo | Tarih: 2026-11-16

---


<a id="comparisons-limits"></a>
## 🧪 Karşılaştırmalar ve sınırlamalar

<a id="case-24"></a>
### Örnek 24: [Neon çöp adam animasyonu: Hydrogen ve Opus](https://x.com/rubenssoto_ai/status/2121068028435791947) (hazırlayan [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Aynı çalıştırma ortamlarını varsaymadan tamamlanmış animasyonu bildirilen süre ve maliyetle birlikte karşılaştırın.**

Yazar, Hydrogen ve Opus 5.5 çıktılarını sunuyor; $1.02 karşısında $7.43 ve 10m 22s karşısında 34m bildiriyor. Bu derleme; faturalamayı, istemleri, yineleme sayılarını veya karşılaştırılabilir çalıştırma ayarlarını doğrulamadı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002-poster.jpg" alt="Case 24 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U002.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-25"></a>
### Örnek 25: [Robotik görevler ve fark edilen hatalar](https://x.com/ArtificialAnlys/status/2120995180891508833) (hazırlayan [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Robotik değerlendirmeye görev tamamlamayı ve küçük hataları fark etmeyi dahil edin.**

Artificial Analysis, sıvı dökme ve blok toplama görevleri gösteriyor; Hydrogen'ın küçük bir dökülmeyi ve kapatılmamış bir kapağı fark ettiğini söylüyor. Video ve AA-Robotics v0.1 sıralaması değerlendiriciden geliyor; burada bağımsız tekrar yapılmadı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008-poster.jpg" alt="Case 25 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U008.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-26"></a>
### Örnek 26: [Doğal dille yönetilen laboratuvar çalışma hücresi](https://x.com/danielmckinn0n/status/2120990834246173125) (hazırlayan [@danielmckinn0n](https://x.com/danielmckinn0n))

**Araç çalıştırmayı ve hata yönetimini, öne çıkan kıyaslama puanlarından ayrı değerlendirin.**

Kaynak, doğal dil isteğiyle yönetilen bir laboratuvar çalışma hücresi gösteriyor ve laboratuvarla ilgili dört kıyaslamada sonuç bildiriyor. Hydrogen'ın bildirilen RareBench puanı Opus 5.5'inkinden düşük, diğer üçü ise yüksek; bu kıyaslamanın sahibinin demosudur, tıbbi doğrulama değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009-poster.jpg" alt="Case 26 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U009.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-27"></a>
### Örnek 27: [Buzdağı ve römorkör: Hydrogen ve Carbon](https://x.com/EnvolDev/status/2120989670582677930) (hazırlayan [@EnvolDev](https://x.com/EnvolDev))

**Uzun bir 3B geliştirmeyi karşılaştırırken akıl yürütme seviyesini ve çalıştırma ortamının kısıtlarını kaydedin.**

Üretici, her iki modelin de OpenRouter üzerinden High seviyesinde çalıştığını; Hydrogen için $4.27 ve 1h 23m 40s, Carbon için $8.83 ve 2h 39m 10s bildiriyor. Bunlar kaynağın bildirdiği kontrolsüz sonuçlardır, evrensel fiyat veya hız oranları değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010-poster.jpg" alt="Case 27 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U010.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-28"></a>
### Örnek 28: [Jöle koi göleti: Hydrogen ve Sonnet](https://x.com/Haleeeemahh/status/2120987701352739314) (hazırlayan [@Haleeeemahh](https://x.com/Haleeeemahh))

**Bir kıyaslama sıralamasını model tercihine dönüştürmeden önce somut bir sahneyi inceleyin.**

Yazar, 3B koi göleti görevinde Hydrogen ile Sonnet 5.5'i karşılaştırıyor. Kaynak, izleyicilerden çıktıları değerlendirmelerini istiyor ancak eşleştirilmiş ayarlar veya nesnel bir kalite puanı ortaya koymuyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011-poster.jpg" alt="Case 28 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U011.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-29"></a>
### Örnek 29: [Ortak istemli yaratıcı kodlama koleksiyonu](https://x.com/kickingkeys/status/2120985358317875222) (hazırlayan [@kickingkeys](https://x.com/kickingkeys))

**Tek bir çekici çıktıdan aşırı genelleme yapmamak için çeşitli görsel görevler kullanın.**

Üretici, Hydrogen, Carbon ve Argon'a aynı istemleri verdiğini bildiriyor ve karşılaştırmaları yanıtlara yerleştiriyor. Ana gönderinin medyası düşük poligonlu hayvanları, neon bir sokağı ve suluboya tarzı bir kabı gösteriyor; tam kontrollü bir kıyaslama değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012-poster.jpg" alt="Case 29 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U012.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-30"></a>
### Örnek 30: [Megamind vokselleri: maliyet ve kalite için bir karşı örnek](https://x.com/thehypedotnews/status/2120980737012670720) (hazırlayan [@thehypedotnews](https://x.com/thehypedotnews))

**Bir modelin sürekli daha ucuz veya görsel açıdan daha güçlü olup olmadığını değerlendirirken başarısız örnekleri koruyun.**

Kaynak, Hydrogen'ın $36.07 maliyetle daha tutarsız bir Titan figürü ürettiğini, Sonnet 5.5'in ise $8.64 tuttuğunu söylüyor. Gönderide ticari tanıtım bulunuyor; maliyetler ve kalite değerlendirmesi yayıncının iddialarıdır.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013-poster.jpg" alt="Case 30 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U013.mp4)

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-31"></a>
### Örnek 31: [Dört mevsimde jonglör aslan](https://x.com/SahilPanhotra/status/2120978349967458704) (hazırlayan [@SahilPanhotra](https://x.com/SahilPanhotra))

**Yalnızca çevredeki arayüzün görsel kalitesini değil, istenen hareketi kontrol edin.**

Yazar, Carbon'ın kesişen jonglör yaylarını gerçekleştirdiğini, Hydrogen'ın ise daha temiz mevsim geçişleri ve kırpmaya rağmen topları havada bıraktığını bildiriyor. Aynı görevin bu SVG karşılaştırması, genel bir model sıralaması değil belirli bir hareket hatasını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015-poster.jpg" alt="Case 31 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U015.mp4)

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-32"></a>
### Örnek 32: [Üç modelli çöp adam dövüşü: daha yavaş, daha pahalı sonuç](https://x.com/DanielZambrini/status/2120963180461769183) (hazırlayan [@DanielZambrini](https://x.com/DanielZambrini))

**Bir modelin tanıtılan verimliliğini gerçek görev raporlarıyla karşılaştırırken karşı örnekleri koruyun.**

Üretici Hydrogen, Carbon ve Argon'ı karşılaştırıyor; bu testte Hydrogen'ın Carbon'dan daha uzun sürdüğünü ve daha pahalı olduğunu bildiriyor. Ayarlar, faturalama ve yineleme sayıları bağımsız olarak doğrulanmadı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019-poster.jpg" alt="Case 32 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U019.mp4)

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-33"></a>
### Örnek 33: [Çiftlikte bisiklet sahnesi: Hydrogen ve Flash](https://x.com/Bhavani_00007/status/2120959112934834412) (hazırlayan [@Bhavani_00007](https://x.com/Bhavani_00007))

**Hareketi ve sahne kalitesini, üreticinin bildirdiği tamamlanma süresiyle birlikte karşılaştırın.**

Kaynak, çiftlikte bisiklet sahnesinde Hydrogen ile Gemini 3.8 Flash'ı karşılaştırıyor ve altı dakikadan fazlaya karşı 56 saniye bildiriyor. Bu, tek bir üreticinin testidir; genel hız kıyaslaması değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023-poster.jpg" alt="Case 33 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U023.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-34"></a>
### Örnek 34: [Tandem bisikletlerde bir kız ve kedi](https://x.com/marcthecreatorr/status/2120956699951628637) (hazırlayan [@marcthecreatorr](https://x.com/marcthecreatorr))

**Farklı kodlama ortamlarını görünür tutarak isteme bağlılığı ve ek ayrıntıları karşılaştırın.**

Üretici aynı belirtilen SVG görevini kullandı ancak Opus 5.5'i Claude Code'da, Hydrogen'ı Cursor'da çalıştırdı. Bildirilen süre ve maliyetler büyük ölçüde farklı olsa da farklı ortamlar ve açıklanmayan yinelemeler, yalnızca modelleri kapsayan kontrollü bir karşılaştırmayı engelliyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027-poster.jpg" alt="Case 34 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U027.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-35"></a>
### Örnek 35: [Dört model Three.js ile Mario oyunu oluşturuyor](https://x.com/StatsWire/status/2120955723396071548) (hazırlayan [@StatsWire](https://x.com/StatsWire))

**Aynı istemle üretilen oyunları karşılaştırmadan önce eşit olmayan akıl yürütme ayarlarını kaydedin.**

Kaynak; dış 3B modeller veya dokular olmadan yalnızca Three.js kullanarak High seviyesindeki Gemini 3.8 Flash, Argon ve Carbon'ı XHigh seviyesindeki Hydrogen ile karşılaştırıyor. Dört çıktı gösteriyor; eşleştirilmiş akıl yürütme seviyeli bir kıyaslama değil.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028-poster.jpg" alt="Case 35 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U028.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-36"></a>
### Örnek 36: [Üç Gemini modeli oyun kumandası çiziyor](https://x.com/notjazii/status/2120952314873987271) (hazırlayan [@notjazii](https://x.com/notjazii))

**Aile içinde bir hiyerarşi varsaymak yerine göreve özgü gerileme ve iyileşmelere bakın.**

Üretici, Carbon, Argon ve Hydrogen'ın SVG kumanda çıktılarını karşılaştırıyor ve testi tekrar çalıştırdığını bildiriyor. Bildirilen süre ve maliyetler kaynak iddialarıdır; genel bir model kalitesi sıralaması oluşturmaz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U031-01.jpg" alt="Case 36 source image 1" height="360"></a>

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-37"></a>
### Örnek 37: [Uygulama ve Studio'da farklı görsel yanıtlar](https://x.com/thegenioo/status/2120946497802174688) (hazırlayan [@thegenioo](https://x.com/thegenioo))

**Bir görsel sonucuna güvenmeden önce aynı görüntüyü kullanmayı planladığınız üründe test edin.**

Kaynak, Gemini uygulaması ve AI Studio'da Hydrogen'a atfedilen çelişkili yiyecek tanıma yanıtları gösteriyor. Karşılaştırma; yönlendirmenin, ayarların veya tam konuşma bağlamının aynı olduğunu bağımsız olarak doğrulamıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-01.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-01.jpg" alt="Case 37 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-02.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U037-02.jpg" alt="Case 37 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-38"></a>
### Örnek 38: [Roket fırlatma sahnesi: Hydrogen ve Flash](https://x.com/Bhavani_00007/status/2120945380850569395) (hazırlayan [@Bhavani_00007](https://x.com/Bhavani_00007))

**Bildirilen geliştirme süresinin yanı sıra gerçek fırlatma animasyonunu da karşılaştırın.**

Üretici, Hydrogen ve Gemini 3.8 Flash çıktılarını sunuyor; yaklaşık üç dakikaya karşı bir dakikadan kısa süre bildiriyor. Görsel karşılaştırma, çalıştırma kurulumu bağımsız olarak kontrol edilmemiş tek bir görevdir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040-poster.jpg" alt="Case 38 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U040.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-39"></a>
### Örnek 39: [Dört SVG animasyon görevi](https://x.com/Angaisb_/status/2120944947193127061) (hazırlayan [@Angaisb_](https://x.com/Angaisb_))

**Görevler arası tutarlılığı incelemek için birden fazla etkileşim ve animasyon motifi kullanın.**

Kaynak; transferler, gündüz/gece değişimleri, kutu açma ve bukalemun için Hydrogen ve Carbon çıktılarını eşleştiriyor. Kısa ana metin, tam istemleri, süre kanıtlarını veya nesnel bir puanlama yöntemini açıklamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041-poster.jpg" alt="Case 39 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U041.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-40"></a>
### Örnek 40: [Üç model savanada bir atı canlandırıyor](https://x.com/AI_Screening/status/2120944276586823689) (hazırlayan [@AI_Screening](https://x.com/AI_Screening))

**Genel maliyet veya kalite iddialarını kabul etmeden önce hareketi ve görsel ayrıntıyı doğrudan inceleyin.**

Üretici Hydrogen, Carbon ve Argon'ı savanada at sahnesinde sunuyor. Daha yüksek hız, daha düşük maliyet ve yüksek kalite iddiaları kaynağın değerlendirmesi olarak kalıyor; burada tekrarlanmış kontrollü bir karşılaştırma değildir.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043-poster.jpg" alt="Case 40 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-3.6-flash-guide-and-use-cases/hydrogen-20261113/media/U043.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-43"></a>
### Örnek 43: [API'de Hydrogen ve Antigravity'de Carbon](https://x.com/huang18825/status/2120876396264444314) (hazırlayan [@huang18825](https://x.com/huang18825))

**Aynı istemden çıkan görselleri karşılaştırırken her çalıştırmanın ortamını kaydedin.**

Yazar Hydrogen'ı doğrudan API üzerinden, Carbon'u Antigravity'de çalıştırıp sonuçları yan yana gösteriyor. Bildirilen 4 dakika 47 saniye bu kurulumdaki Hydrogen çalıştırmasına ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-poster-c7f6251b518c.jpg" alt="Case 43 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120876396264444314-1-url-f9f3550f5578.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-44"></a>
### Örnek 44: [Hydrogen ve Astra Karşılaştırmasında Gölge Ayrıntısı](https://x.com/SPAC89/status/2120911537296515321) (hazırlayan [@SPAC89](https://x.com/SPAC89))

**Küçük görüntü ayrıntılarını iki çalıştırmanın maliyeti ve süresiyle birlikte değerlendirin.**

Yazar gölge içerdiği için Hydrogen çıktısını tercih ediyor ve kendi kurulumunda daha hızlı tamamlandığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-poster-a83da06a7d2c.jpg" alt="Case 44 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120911537296515321-1-url-e962ea72cb4e.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-45"></a>
### Örnek 45: [Prosedürel 3B Hareket Karşılaştırması](https://x.com/SPAC89/status/2120923185981915156) (hazırlayan [@SPAC89](https://x.com/SPAC89))

**Prosedürel bir animasyonda akıcılık ve kompozisyonu karşılaştırırken üretim süresini kaydedin.**

Yazar Hydrogen High'a atfettiği çizgili 3B biçimin beş dakikadan kısa sürdüğünü bildiriyor ve kendi testinde daha pahalı modellerin çıktılarıyla karşılaştırıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-poster-3756cb2f911d.jpg" alt="Case 45 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923185981915156-1-url-f4ac6b3bd334.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-46"></a>
### Örnek 46: [PokéBench'te 89 Dakikalık Görsel Test](https://x.com/StatsWire/status/2120923685296988296) (hazırlayan [@StatsWire](https://x.com/StatsWire))

**Uzun bir görsel ajan testinde görev sonucuyla birlikte hamleleri ve API hatalarını kaydedin.**

Kaynak, duyurudan önce Vertex'te High ayarıyla yapılan bir çalıştırmada Hydrogen'ın Brock'u 365 hamle ve 89 dakikada geçtiğini bildiriyor. Başarısız API çağrısı bildirilmedi. Sonuç bu test ortamına özgü.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120923685296988296-1-url-0cc5fb29b321.jpg" alt="Case 46 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-47"></a>
### Örnek 47: [Hydrogen ve DeepSeek Aynı 3B Sahneyi Kuruyor](https://x.com/AiHubMix/status/2120928687537418581) (hazırlayan [@AiHubMix](https://x.com/AiHubMix))

**Görsel çıktıları karşılaştırırken süreyi ve API ücretini ayrı ayrı kaydedin.**

AIHubMix aynı 3B sahne isteminde Hydrogen ve DeepSeek V4.1 Flash'ı erişilebilir en yüksek akıl yürütme ayarlarında karşılaştırıyor. Sağlayıcı, Hydrogen için 3 dakika ve 1,30 USD, DeepSeek için 100 dakika ve 0,90 USD bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-poster-e4f59f0c0f58.jpg" alt="Case 47 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120928687537418581-1-url-3f100795e2a1.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-53"></a>
### Örnek 53: [Agent Arena'da Görev Başına Süre ve Maliyet](https://x.com/arena/status/2120940869889175840) (hazırlayan [@arena](https://x.com/arena))

**Toplam başarıyla birlikte görev başına gecikmeyi, maliyeti ve çıktı token'larını inceleyin.**

Agent Arena, Hydrogen High için görev başına medyan 5,3 dakika ve 1,60 USD bildiriyor. Çıktı token'ı kullanımı Carbon ve Argon'dan daha yüksek.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120940869889175840-1-url-91c82837b98a.jpg" alt="Case 53 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-54"></a>
### Örnek 54: [Görsel Belge ve Terminal Kıyaslamaları](https://x.com/ArtificialAnlys/status/2120941511223185722) (hazırlayan [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**Akıl yürütme bütçesi seçerken belge ve terminal sonuçlarını ayrı değerlendirin.**

Artificial Analysis görsel belgelerde güçlü sonuçlar ve terminal görevlerinde farklı oranlarda ilerleme bildiriyor. Ek akıl yürütme, bilimsel terminal puanını artırırken genel Terminal-Bench sonucu %54'te kaldı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120941511223185722-1-url-5826160b2eec.jpg" alt="Case 54 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-55"></a>
### Örnek 55: [Vals Index ve Tax Agent Sonuçları](https://x.com/ValsAI/status/2120943893894303808) (hazırlayan [@ValsAI](https://x.com/ValsAI))

**Uzmanlık gerektiren bir görevin puanını genel değerlendirmeyle birlikte inceleyin.**

Vals AI kendi endeksinde %68,5 ve test sırasında Tax Agent'ta birincilik bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120943893894303808-1-url-31f14528e470.jpg" alt="Case 55 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-56"></a>
### Örnek 56: [CursorBench'te Varsayılan Ayarla Hydrogen](https://x.com/cursor_ai/status/2120944639633211619) (hazırlayan [@cursor_ai](https://x.com/cursor_ai))

**Varsayılan ayardaki puanı kendi deponuzda yapacağınız testler için başlangıç noktası olarak kullanın.**

Cursor kendi testinde varsayılan ayarla Hydrogen için %54,3, Gemini 3.8 Flash için %39,6 bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120944639633211619-1-url-1180f341b2c2.jpg" alt="Case 56 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-57"></a>
### Örnek 57: [Dört Modelle Okçu Savaşı Animasyonu](https://x.com/IndependentEco/status/2120945011277590733) (hazırlayan [@IndependentEco](https://x.com/IndependentEco))

**Her animasyonun savaşçıların hareketlerini ne kadar anlaşılır aktardığını karşılaştırın.**

Yazar Hydrogen, Fable 5.2, GPT-6.1 Sol ve Carbon ile üretilen okçu savaşı sonuçlarını aynı klipte yan yana gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-poster-fd4b00e6d0ae.jpg" alt="Case 57 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120945011277590733-1-url-21dbb33791cd.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-61"></a>
### Örnek 61: [Devin FrontierCode'da Hydrogen](https://x.com/cognition/status/2120950876248641588) (hazırlayan [@cognition](https://x.com/cognition))

**Yamaların birleştirmeye uygunluğunu karşılaştırıp ajan test ortamını kaydedin.**

Cognition, FrontierCode 2.0'da %38,2 bildiriyor. Hydrogen için kullanılan kurulum, karşılaştırma modellerinin Devin CLI kurulumundan farklı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120950876248641588-1-url-a70465b6f37a.jpg" alt="Case 61 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-64"></a>
### Örnek 64: [Açık Talimata Rağmen Web Araması](https://x.com/amanunreal/status/2120954045615768054) (hazırlayan [@amanunreal](https://x.com/amanunreal))

**Tarama yapmadan yanıt gerektiren bir iş akışında araçların çağrılıp çağrılmadığını kontrol edin.**

Yazar, Hydrogen'ın arama ve araç kullanımını yasaklayan talimata rağmen web araması yaptığını bildiriyor. Paylaşım gözlemlenen tek bir örneği gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954045615768054-1-url-793a75324887.jpg" alt="Case 64 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-65"></a>
### Örnek 65: [Antigravity Swarm'da Kota Takibi](https://x.com/HarshithLucky3/status/2120954399971487774) (hazırlayan [@HarshithLucky3](https://x.com/HarshithLucky3))

**Çok ajanlı bir çalıştırmada toplam token sayısını ve tüketilen kotayı kaydedin.**

Yazar Swarm kullanırken 17 milyon token ve beş saatlik kotasının %21'ini tükettiğini bildiriyor. Sayılar bu oturuma ve kullandığı plana ait.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-1-url-a6fefd498713.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-1-url-a6fefd498713.png" alt="Case 65 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-2-url-b4f5e4dfa2e9.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120954399971487774-2-url-b4f5e4dfa2e9.png" alt="Case 65 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-66"></a>
### Örnek 66: [Mesleki Görev Testlerinde Araç Çağrıları](https://x.com/mercor/status/2120957582139642095) (hazırlayan [@mercor](https://x.com/mercor))

**Bir ajanın mesleki görevi yerine getirmeden önce bağlamı nasıl topladığını inceleyin.**

Mercor, APEX-Agents'ta %78,0 Pass@1 ve görev başına ortalama 93 araç çağrısı bildiriyor. Rapor hukuk, danışmanlık ve bankacılık görevlerini kapsıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-poster-a73073fdb77f.jpg" alt="Case 66 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120957582139642095-1-url-1fc1c228abc5.mp4)

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-68"></a>
### Örnek 68: [Dört Model Bir Büyücü ve Ejderhayı Canlandırıyor](https://x.com/IndependentEco/status/2120964690906161461) (hazırlayan [@IndependentEco](https://x.com/IndependentEco))

**Aynı fantastik sahnenin farklı sürümlerinde düzeni, hareketlerin anlaşılırlığını ve efektleri karşılaştırın.**

Klip bir büyücü ve ejderha sahnesini Hydrogen ve üç Claude modeliyle karşılaştırıyor. Yazar bu örnekte Claude çıktısını tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-poster-023cc9abbf78.jpg" alt="Case 68 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120964690906161461-1-url-c8a54484ebbb.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-71"></a>
### Örnek 71: [MazeBench'te Düşük Başarı Oranları](https://x.com/patience_cave/status/2120973681937809766) (hazırlayan [@patience_cave](https://x.com/patience_cave))

**Uzamsal akıl yürütmeye güvenmeden önce labirent görevleriyle sınayın.**

Yayımlanan MazeBench karşılaştırması, bu kurulumda Hydrogen için %1, Sonnet 5.5 için %4 ve GPT-6.1 Terra için %8 bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120973681937809766-1-url-bacbb448507b.jpg" alt="Case 71 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-72"></a>
### Örnek 72: [Üç Gemini Modeli Yelkenli Sahnesi Kuruyor](https://x.com/Octoberry/status/2120974412144902376) (hazırlayan [@Octoberry](https://x.com/Octoberry))

**Temalı bir Three.js sahnesinde hareket ve çevre ayrıntılarını karşılaştırın.**

Yazar Hydrogen, Argon ve Carbon'un yelkenli çıktılarını gösteriyor. Carbon'un ayrıntılarını tercih ediyor ve kendi testinde Hydrogen'ın Argon'a yaklaştığını söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-poster-4a108ab6b91c.jpg" alt="Case 72 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120974412144902376-1-url-f12a81cd3f5d.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-75"></a>
### Örnek 75: [Forma Numarası Okurken Tükenen Bütçe](https://x.com/skalskip92/status/2120994631072776235) (hazırlayan [@skalskip92](https://x.com/skalskip92))

**Küçük bir görsel ayrıntıyı okumak için çaba sınırı ve alternatif yöntem belirleyin.**

Testi yapan kişi, Hydrogen XHigh'ın 131.069 düşünme token'ı kullandığını ve 9 dakika 55 saniyenin ardından forma numarası döndürmediğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2120994631072776235-1-url-e85ff16e2dfc.jpg" alt="Case 75 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-12

---

<a id="case-76"></a>
### Örnek 76: [Model Ailelerinin ClutterBench Performansı](https://x.com/AdamHoltererer/status/2121000759118459138) (hazırlayan [@AdamHoltererer](https://x.com/AdamHoltererer))

**Bir model ailesinin genel güçlü yanlarının karmaşık sahnelere yansıyıp yansımadığını test edin.**

Yazarın paylaştığı ClutterBench sonuçlarında Hydrogen, gösterilen Gemini modellerinin önünde ve karşılaştırmadaki OpenAI modellerinin gerisinde.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121000759118459138-1-url-919d78a6e644.jpg" alt="Case 76 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-12

---

<a id="case-78"></a>
### Örnek 78: [Minecraft Tarzı Anatomik Kesit Büstü](https://x.com/jan_volad/status/2121026531472339340) (hazırlayan [@jan_volad](https://x.com/jan_volad))

**Oluşturulan kesitte istenen iç yapıların yer alıp almadığını kontrol edin.**

Yazar Hydrogen ve Argon'a tek istemle aynı anatomik Minecraft büstünü oluşturma görevi verdi. Hydrogen çıktısında kafatası, kaburgalar ve omurgayı tanıdığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-poster-4b012c2bb0b6.jpg" alt="Case 78 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121026531472339340-1-url-ee4414af3cfc.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-79"></a>
### Örnek 79: [Üç Model Aynı Sahne Nesnesini Üretiyor](https://x.com/luckeyfaraday/status/2121030005899825504) (hazırlayan [@luckeyfaraday](https://x.com/luckeyfaraday))

**Bir testte daha ucuz model daha çok token kullanabildiğinde kaliteyi ve token sayısını ayrı izleyin.**

Karşılaştırma, Hydrogen, Carbon ve Fable 5.2'nin tüfek biçimli aynı nesneyi oluşturmasını gösteriyor. Yazar Hydrogen için 3,69 milyon token ve 1,62 USD, Carbon için 398.000 token ve 0,77 USD bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-poster-f6c2617eba0c.jpg" alt="Case 79 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121030005899825504-1-url-89c7dd94e300.mp4)

Tür: Evaluation | Tarih: 2026-11-12

---

<a id="case-80"></a>
### Örnek 80: [Tümevarım Testi ve Token Tüketimi](https://x.com/s_batzoglou/status/2121037853258129811) (hazırlayan [@s_batzoglou](https://x.com/s_batzoglou))

**Zor görevlerde akıl yürütme puanıyla birlikte faturalanan giriş ve çıkış token'larını izleyin.**

Testi yapan kişi, Hydrogen'ın 100 soruluk tümevarım testinde Opus 5.5'e yakın bir sonuçla dördüncü olduğunu bildiriyor. 55 milyon çıktı ve faturalanan 307 milyon girdi token'ı bildiriyor. Hesaplama ayrıntısı belirsiz.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121037853258129811-1-url-882ac9aa912d.jpg" alt="Case 80 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-83"></a>
### Örnek 83: [Üç Modelle 3B Hayvan Animasyonu](https://x.com/leo114119/status/2121054098753785915) (hazırlayan [@leo114119](https://x.com/leo114119))

**Aynı 3B hayvan modelleme görevinde anatomiyi ve hareketi inceleyin.**

Kaynak, tek modelleme görevinde Hydrogen, GPT-6.1 Terra ve Claude Haiku 5.5'i karşılaştırıyor. Yazar Hydrogen çıktısındaki zayıflıkları belirtiyor. Gözlem bu görevle sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-poster-d3f0da035df5.jpg" alt="Case 83 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121054098753785915-1-url-99d2734c6ae5.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-84"></a>
### Örnek 84: [ts-bench'te Hydrogen ve Qwen](https://x.com/gosrum/status/2121058334552060102) (hazırlayan [@gosrum](https://x.com/gosrum))

**Genel kıyaslama sonucuyla birlikte araç çağrısı hatalarını inceleyin.**

Kaynak ts-bench'te Hydrogen ve Qwen4 Max Preview'ı karşılaştırıp araç çağrılarının güvenilirliğini ele alıyor. Ekran görüntüsü değerlendirme sonuçlarını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121058334552060102-1-url-4e02a3fc0603.jpg" alt="Case 84 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-85"></a>
### Örnek 85: [Vending-Bench İşletme Simülasyonu](https://x.com/andonlabs/status/2121061429889642497) (hazırlayan [@andonlabs](https://x.com/andonlabs))

**Simüle edilen geliri ajanın işletim maliyetiyle birlikte karşılaştırın.**

Andon Labs, Hydrogen'ın Vending-Bench 2'de üçüncü olduğunu ve simülasyonda benzer fiyatlı modellerden daha çok gelir elde ettiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121061429889642497-1-url-f46c95a339ee.jpg" alt="Case 85 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-89"></a>
### Örnek 89: [Dört Model Minyatür Ada Kuruyor](https://x.com/xKaka1456/status/2121111495358697924) (hazırlayan [@xKaka1456](https://x.com/xKaka1456))

**Ada tasarımlarını her ortamın çalışma süresi ve maliyetiyle birlikte karşılaştırın.**

Yazar dört ada çıktısını karşılaştırıp Hydrogen için 4, GPT-6.1 Terra için 20, Sol için 40 ve DeepSeek için 60 dakika bildiriyor. Hydrogen için ek ücret çıkmaması yazarın kurulumuna özgü.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-poster-d4cd8fee31b4.jpg" alt="Case 89 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121111495358697924-1-url-3555f6c37deb.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-91"></a>
### Örnek 91: [Kodla Üretilen Kumaş Yırtılmalarının Karşılaştırması](https://x.com/MichaelLee009/status/2121126779276402904) (hazırlayan [@MichaelLee009](https://x.com/MichaelLee009))

**Aynı animasyon görevinde esneme, yırtılma ve kürkle etkileşimi sınayın.**

Yazar Hydrogen ve Claude Fable 5.2'nin kodla üretilen animasyonlarını karşılaştırıp Fable çıktısını görsel olarak üstün buluyor. Eşleşen ayarlar ve bağımsız fizik doğrulaması belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-poster-da7b327492eb.jpg" alt="Case 91 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121126779276402904-1-url-e37a8faf3def.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-94"></a>
### Örnek 94: [İzlenemeyen Kaynakla Doğruluk Kontrolü](https://x.com/cagrimbakirci/status/2121130756684886279) (hazırlayan [@cagrimbakirci](https://x.com/cagrimbakirci))

**Bir ekran görüntüsü hakkındaki yargıya dayanarak hareket etmeden önce incelenebilir kaynak isteyin.**

Yazar, Hydrogen'a bir gönderi görüntüsünün doğru olup olmadığını sordu. Modelin içeriği doğruladığını, doğrulama aracını tekrar tekrar açtığını ve asıl kaynağı paylaşmadığını bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121130756684886279-1-url-6d728c75ea62.jpg" alt="Case 94 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-13

---

<a id="case-96"></a>
### Örnek 96: [Hydrogen ve Sol ile 2B Pelikan](https://x.com/YxzRainy/status/2121148582166491164) (hazırlayan [@YxzRainy](https://x.com/YxzRainy))

**Aynı basit 2B animasyon görevinde süreyi ve hareket kalitesini karşılaştırın.**

Klip, Hydrogen ve GPT-6.1 Sol ile üretilen bisikletli pelikanları gösteriyor. Yazar Hydrogen için 28 saniye, Sol için 6 dakika 51 saniye bildiriyor. Çalıştırma ayarlarının eşitliği doğrulanmıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-poster-6ce9140306f0.jpg" alt="Case 96 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121148582166491164-1-url-2e8c638fd3fa.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-98"></a>
### Örnek 98: [Dört Modelle Ağda Sallanma Oyunu](https://x.com/StatsWire/status/2121172215182065807) (hazırlayan [@StatsWire](https://x.com/StatsWire))

**Aynı tek dosya kısıtıyla oluşturulan oyunlarda hareketi ve denetimleri karşılaştırın.**

Kaynak, dört Gemini modeline harici varlık kullanmadan tek HTML dosyasında aynı 3B oyunu yaptırıyor. Hydrogen Extra High, Gemini 3.8 Flash, Argon ve Carbon High ayarında.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-poster-cae190064f7b.jpg" alt="Case 98 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172215182065807-1-url-87f42a706c86.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-100"></a>
### Örnek 100: [Dört Model Bina Dioraması Oluşturuyor](https://x.com/Jackson77li/status/2121172890838352306) (hazırlayan [@Jackson77li](https://x.com/Jackson77li))

**Aynı mimari görevde farklı modellerin çıktısını ve ışık tercihlerini karşılaştırın.**

Yazar aynı istemi kullandığını belirttiği Hydrogen, GPT-6.2, Claude Fable 5.2 ve DeepSeek dioramalarını gösteriyor. Sıralama ve hız yorumu yazara ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-poster-4afd8d154223.jpg" alt="Case 100 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121172890838352306-1-url-d80b5df6306b.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-103"></a>
### Örnek 103: [Üç Model Tren Sahnesi Oluşturuyor](https://x.com/xKaka1456/status/2121193705810104515) (hazırlayan [@xKaka1456](https://x.com/xKaka1456))

**Bir tren sahnesiyle kullandığınız model ayarlarının sürelerini karşılaştırın.**

Yazar Hydrogen ile yaklaşık 3, GPT-6.1 Terra ile 20 ve Qwen4 Max Preview ile 68 dakika bildiriyor. Klip çıktıları gösteriyor. Ayarlar ve yineleme sayıları belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-poster-7424e47f74d9.jpg" alt="Case 103 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121193705810104515-1-url-7d7f26fa5f3a.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-104"></a>
### Örnek 104: [Extra Ayarında Yağmurlu Chinatown](https://x.com/qingzhoucloud/status/2121198911515967952) (hazırlayan [@qingzhoucloud](https://x.com/qingzhoucloud))

**Yoğun bir animasyonda akıl yürütme ayarını seçmeden önce süreyi ölçüp bitmiş sahneyi inceleyin.**

Yazar başka bir üreticinin istemini Hydrogen Extra ile kullanıp yağmurlu Chinatown MP4'ü için yaklaşık dört saat bildiriyor. Ayrı Claude Fable 5.2 çalıştırmasıyla karşılaştırılabilirlik sınırlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-poster-3988a90efe47.jpg" alt="Case 104 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121198911515967952-1-url-31fdb05cc5eb.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-106"></a>
### Örnek 106: [Üç Model Bir Gezegen Görselleştiricisi Kuruyor](https://x.com/Stargridcompass/status/2121208957276713181) (hazırlayan [@Stargridcompass](https://x.com/Stargridcompass))

**Bilimsel bir görsel arayüz için aynı istemi birkaç modelle deneyin.**

Kayıt Claude Fable 5.2, GPT-6.2 Sol ve Hydrogen'ın gezegen çıktılarını karşılaştırıyor. Sıralama yazarın görsel değerlendirmesi. Ayar eşitliği ve nesnel puanlama açık.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-poster-26d869e61ab5.jpg" alt="Case 106 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121208957276713181-1-url-cf0ef283fad3.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-107"></a>
### Örnek 107: [Dört Model Chrome Dino'yu Yeniden Yapıyor](https://x.com/noclipepe/status/2121219775170761044) (hazırlayan [@noclipepe](https://x.com/noclipepe))

**Tanıdık bir oyunun her sürümünün süresini ölçüp oynanabilir sonuçları karşılaştırın.**

Yazar T-Rex oyunu için AI Studio'da Hydrogen ile 18 dakika 41 saniye ve Fable 5.2 ile 45 dakika 30 saniye bildiriyor. Kayıt Qwen4-Max-Preview, Carbon ve görsel puanları da gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-poster-55ac8e1dd2aa.jpg" alt="Case 107 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121219775170761044-1-url-6374c3ec16f1.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-109"></a>
### Örnek 109: [İki Kodlama Ajanı Farklı Gemiler Yapıyor](https://x.com/marcthecreatorr/status/2121221667619852660) (hazırlayan [@marcthecreatorr](https://x.com/marcthecreatorr))

**Seçtiğiniz ortamda ilk kullanılabilir çıktıyı ve düzeltme maliyetini karşılaştırın.**

Yazar aynı istemi Sonnet için Claude Code, Hydrogen için Cursor'da kullandı. Hydrogen'ın daha kısa sürdüğünü ve ikinci bir sürüm gerektirdiğini bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-poster-188c6c01545d.jpg" alt="Case 109 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121221667619852660-1-url-3be4415ccf75.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-111"></a>
### Örnek 111: [Dört Modelle Mancınık ve Katı Cisim Fiziği](https://x.com/StatsWire/status/2121226579141386285) (hazırlayan [@StatsWire](https://x.com/StatsWire))

**Aynı görevde oynanabilir fizik prototiplerini karşılaştırıp akıl yürütme ayarlarını kaydedin.**

Yazar dört Gemini modelini yüzlerce taş blok içeren mancınık sahnesinde denedi. Hydrogen Extra High için 10 dakika 3 saniye ve Carbon High için 23 dakika 33 saniye bildirdi. Gemini 3.8 Flash High en hızlısıydı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-poster-2bfed95ab2f4.jpg" alt="Case 111 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121226579141386285-1-url-7dde6068eb0e.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-116"></a>
### Örnek 116: [FrontierMemory'de Kalıcı Ajan Belleği](https://x.com/Letta_AI/status/2121255895745351874) (hazırlayan [@Letta_AI](https://x.com/Letta_AI))

**Uzun ömürlü ajan belleği için model seçerken puanı ve çalıştırma başına maliyeti karşılaştırın.**

Letta, Hydrogen için Argon'la aynı olan %64,4 ve bellek çalıştırması başına yaklaşık 100 USD bildiriyor. Kıyaslama ayarlarında Carbon için %71,1 ve yaklaşık 94 USD bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121255895745351874-1-url-94919aa9b162.jpg" alt="Case 116 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-117"></a>
### Örnek 117: [Arızalı LiveKit Sesli Ajanında Hydrogen](https://x.com/livekit/status/2121256982023672076) (hazırlayan [@livekit](https://x.com/livekit))

**Kontrollü bir araç hatasıyla ajanın desteklenmeyen sonuçlar bildirip bildirmediğini sınayın.**

LiveKit Hydrogen'ı kasıtlı olarak arızalandırılmış bir sesli ajanda test edip sıfır yanlış bildirim raporluyor. Sağlayıcı Gemini 3.8 Flash'la kıyaslıyor ve raporuna bağlantı veriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-poster-16e7d2c0613c.jpg" alt="Case 117 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121256982023672076-1-url-19a320ac15b8.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-123"></a>
### Örnek 123: [Üç Gemini Modeli Bisikletliyi Canlandırıyor](https://x.com/AI_Screening/status/2121281026916057443) (hazırlayan [@AI_Screening](https://x.com/AI_Screening))

**Aynı görevde kısa hareketli sahneleri karşılaştırıp süreleri ayrı kaydedin.**

Yazar Carbon, Argon ve Hydrogen ile üretilen bisikletliyi gösteriyor. Hydrogen için yaklaşık 90 saniye ve Argon için beş dakikadan fazla süre bildiriyor. Carbon'un görüntüsünü tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-poster-a6451d0d5c85.jpg" alt="Case 123 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121281026916057443-1-url-67be8b27ef2f.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-126"></a>
### Örnek 126: [İki Model LEGO Dünyası Kuruyor](https://x.com/kepochnik/status/2121286219669836027) (hazırlayan [@kepochnik](https://x.com/kepochnik))

**Her modelin verilen sürede temalı dünyanın ne kadarını oluşturduğunu karşılaştırın.**

Yazar Fable 5.2 ve Hydrogen’ın LEGO dünyalarını gösteriyor. Kendi çalıştırmalarında sırasıyla 44 ve 28 dakika bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-poster-888f8975c88e.jpg" alt="Case 126 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286219669836027-1-url-cf45f9a57ed0.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-127"></a>
### Örnek 127: [İki Depoya Ekilen Hataları Onarma](https://x.com/PawelHuryn/status/2121286545223086302) (hazırlayan [@PawelHuryn](https://x.com/PawelHuryn))

**Kodlama ajanının hangi hataları bulup düzelttiğini ölçmek için bilinen kusurlar ekleyin.**

Testi yapan kişi iki depoya 105 hata yerleştirdi. Bu kurulumda en yüksek çaba ayarındaki Hydrogen, aynı çaba ayarındaki Sonnet 5.5'in hemen arkasında yer aldı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121286545223086302-1-url-64861f4183a1.jpg" alt="Case 127 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-128"></a>
### Örnek 128: [İki Modelle Çöp Adam ve İmleç](https://x.com/DanielZambrini/status/2121289822677483740) (hazırlayan [@DanielZambrini](https://x.com/DanielZambrini))

**İki etkileşimli animasyonun işaretçiye tepkisini karşılaştırın.**

Yazar Fable'ın çöp adam ve imleç animasyonunu tercih ediyor. Hydrogen'ı daha düşük maliyetli bir deneme için yeterli buluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-poster-6248a9566f69.jpg" alt="Case 128 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121289822677483740-1-url-59226a4a6ae5.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-130"></a>
### Örnek 130: [İki Model Dağ Manzarası Oluşturuyor](https://x.com/ZryMiller/status/2121295750122594440) (hazırlayan [@ZryMiller](https://x.com/ZryMiller))

**Manzara animasyonunda kompozisyonu, üretim süresini ve maliyeti ayrı karşılaştırın.**

Yazar Hydrogen ve Opus 5.5 ile hazırladığı dağ animasyonlarını paylaşıyor. Hydrogen için 20 dakika 30 saniye ile 0,50 USD, Opus için 11 dakika 23 saniye ile 2,50 USD bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-poster-dae58d930d63.jpg" alt="Case 130 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121295750122594440-1-url-6397fee0ceb6.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-131"></a>
### Örnek 131: [Özel Test Ortamında İngilizceden Farsçaya Çeviri](https://x.com/MatinSenPai/status/2121296733258887365) (hazırlayan [@MatinSenPai](https://x.com/MatinSenPai))

**Zor bir çeviriyi insan çevirisiyle karşılaştırıp değerlendirin.**

Yazar kendi test ortamında bir çeviri görevinde Hydrogen'a 100 üzerinden 94 verdi. Öznel değerlendirme bu düzene bağlı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121296733258887365-1-url-7b26fc7de3a0.png" alt="Case 131 source image 1" height="360"></a>

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-133"></a>
### Örnek 133: [Dört Model Batan Gemi Sahnesi Kuruyor](https://x.com/remoteugur/status/2121302956741902451) (hazırlayan [@remoteugur](https://x.com/remoteugur))

**Aynı sahne testinde görsel sadakati, süreyi ve maliyeti ayrı kaydedin.**

Yazar Hydrogen için 8,6 dakika ve 1,16 USD, Gemini 3.8 Flash için 10,8 dakika ve 1,06 USD bildiriyor. Carbon ve Opus 5.5'i de deniyor ve gerçekçilikte Opus'u tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-poster-e9f2d93705d1.jpg" alt="Case 133 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121302956741902451-1-url-d495352c55cb.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-135"></a>
### Örnek 135: [Dört Modelle Kör Reklam Metni Karşılaştırması](https://x.com/quintanilha/status/2121315967447757299) (hazırlayan [@quintanilha](https://x.com/quintanilha))

**Yazı iş akışında kullanacağınız çıktıyı seçmeden önce model adlarını gizleyin.**

Yazar dört modelle kör metin karşılaştırması yaptığını ve Hydrogen çıktısını tercih ettiğini bildiriyor. Kendi testinde Hydrogen'ın Carbon'dan daha hızlı ve daha düşük maliyetli olduğunu söylüyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121315967447757299-1-url-714e452b34ae.png" alt="Case 135 source image 1" height="360"></a>

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-136"></a>
### Örnek 136: [Akıl Yürütme Ayarına Göre Görsel Algılama ve Okuma](https://x.com/skalskip92/status/2121322414453694489) (hazırlayan [@skalskip92](https://x.com/skalskip92))

**Her akıl yürütme düzeyinde algılama, metin doğruluğu, maliyet ve gecikmeyi ayrı ölçün.**

Testi yapan kişi Hydrogen, Argon ve Carbon'un algılama ile metin puanlarını ayrı bildiriyor. Hydrogen High'ın görsel başına ortalaması 29,3 saniye, puanları 64,6 ve 87,2. Carbon High daha maliyetli ve yavaş olmasına rağmen iki alanda da daha yüksek puan aldı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121322414453694489-1-url-cc166d526205.jpg" alt="Case 136 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-13

---

<a id="case-137"></a>
### Örnek 137: [Dört Model Yukarı Bak'taki Evi Yeniden Yapıyor](https://x.com/noclipepe/status/2121326233044537688) (hazırlayan [@noclipepe](https://x.com/noclipepe))

**3B modeller arasındaki farkları aynı referans görseli ve görevle karşılaştırın.**

Yazar dört çalıştırmada Hydrogen'ın en hızlı ve en düşük maliyetli olduğunu bildiriyor, görsel olarak Fable'ı tercih ediyor. Ayarlar ve fiyatlandırma kaynağın beyanına dayanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-poster-15020a29bd9d.jpg" alt="Case 137 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121326233044537688-1-url-acad8447a045.mp4)

Tür: Evaluation | Tarih: 2026-11-13

---

<a id="case-144"></a>
### Örnek 144: [Sabit Kamerayla Dans Klibi](https://x.com/notoro_ai/status/2121427503952834562) (hazırlayan [@notoro_ai](https://x.com/notoro_ai))

**Referanslı animasyonun karakter tasarımını, kompozisyonu ve kamera konumunu koruyup korumadığını sınayın.**

Yazar Japonca bir istemi ve Google Gemini'de Hydrogen'la ilişkilendirdiği dans klibini paylaşıyor. İstem sabit kamera ve referans üslubunu korumayı şart koşuyor. Kullanılan video modeli belirtilmiyor.

**İstem:**

```
無地背景の前でキレのあるダンスをする20代女性。元画像の画風・キャラクターデザイン・構図を完全に維持。カメラは完全に固定（パン・ズームなし）、アングル維持。口は閉じたまま無言で踊る。縦長9:16。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-poster-4610ae50dd6d.jpg" alt="Case 144 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121427503952834562-1-url-35cc552b7d25.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-145"></a>
### Örnek 145: [Başlangıç Testinde Takılan Kodlama Ajanı](https://x.com/Its_lakshya_ai/status/2121431788266659919) (hazırlayan [@Its_lakshya_ai](https://x.com/Its_lakshya_ai))

**Düzeltmeyi beklemeden önce başlangıç testinin süresini sınırlayın ve ilerlemeyi kontrol edin.**

Yazar, Hydrogen'ın uzun bekleyişten sonra hâlâ başlangıç testini çalıştırdığı Antigravity oturumunu gösteriyor. Ekran görüntüsünde durdurup sorunu araştırma isteği var.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121431788266659919-1-url-62f0fa7efc12.jpg" alt="Case 145 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-14

---

<a id="case-147"></a>
### Örnek 147: [İki Model Etkileşimli Robot Kolu Yapıyor](https://x.com/gmi_cloud/status/2121467337119588834) (hazırlayan [@gmi_cloud](https://x.com/gmi_cloud))

**Three.js robot kolunun eklemlerinin kullanıcı girdisine tutarlı tepki verip vermediğini sınayın.**

GMI Cloud aynı Three.js robot kolu görevinde Hydrogen ve Sonnet 5.5 çıktılarını gösteriyor. Sağlayıcı bu karşılaştırmada Sonnet'i tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-poster-944436dd9b66.jpg" alt="Case 147 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121467337119588834-1-url-ac879502d507.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-151"></a>
### Örnek 151: [Hydrogen ve Sol ile Kış Köyü](https://x.com/badboyfoxy/status/2121501015442669866) (hazırlayan [@badboyfoxy](https://x.com/badboyfoxy))

**Kodlama karşılaştırmasında süre, harcama ve sahne kalitesini ayrı değerlendirin.**

Yazar Hydrogen High için 3 dakika ve 1,37 USD, Sol High için 15 dakika ve 4,03 USD bildiriyor. Kış köyünde Sol'un tasarımını tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-poster-a6eccb2b1a8b.jpg" alt="Case 151 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121501015442669866-1-url-4f1e738b9635.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-152"></a>
### Örnek 152: [High ve Ultra Ayarlarında Three.js Adası](https://x.com/laopai1990/status/2121502334866096160) (hazırlayan [@laopai1990](https://x.com/laopai1990))

**Ürünlerin kotalarını ayrı ele alarak görselleri, süreyi ve akıl yürütme düzeyini karşılaştırın.**

Yazar Three.js adası için Hydrogen High ile yaklaşık 90 saniye, GPT-6.1 Sol Ultra ile yaklaşık 30 dakika bildiriyor. Maliyetler tahmini, akıl yürütme düzeyleri farklı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-poster-ce39ea42d2a0.jpg" alt="Case 152 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121502334866096160-1-url-ca5d0d686811.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-157"></a>
### Örnek 157: [3B PS5 Kumandasında Ayrıntı Karşılaştırması](https://x.com/Stargridcompass/status/2121528563254043015) (hazırlayan [@Stargridcompass](https://x.com/Stargridcompass))

**Kumanda modellerinde düğme gölgelerini ve arka donanım ayrıntılarını inceleyin.**

Yazar Hydrogen High ve GPT-6.2 Sol'u 3B kumandada karşılaştırıyor. Yaklaşık 3 ve 11 dakika bildiriyor. Sol çıktısında arka ve yan denetimleri daha eksiksiz buluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-poster-af0dc5a722b4.jpg" alt="Case 157 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121528563254043015-1-url-f3bfbfcac4a4.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-159"></a>
### Örnek 159: [Farklı Akıl Yürütme Bütçeleriyle CursorBench](https://x.com/Beamsters1/status/2121538515909628111) (hazırlayan [@Beamsters1](https://x.com/Beamsters1))

**Hızlı bir varsayılan ayar seçmeden önce farklı akıl yürütme düzeylerinin başarısını karşılaştırın.**

Yazar Hydrogen'a ayrılan akıl yürütme bütçesi artınca CursorBench 4.0 başarısının hızla yükseldiğini bildiriyor. Sonuç test edilen ayarlara özgü.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121538515909628111-1-url-43e96144411e.jpg" alt="Case 159 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-14

---

<a id="case-160"></a>
### Örnek 160: [Üç Model Yıldız Temalı Tapınak Oluşturuyor](https://x.com/YxzRainy/status/2121551796766376081) (hazırlayan [@YxzRainy](https://x.com/YxzRainy))

**3B görevde görüntü kararlılığını görsel ayrıntıdan ayrı değerlendirin.**

Yazar Hydrogen, DeepSeek V4.1 1017 ve Qwen4 Max Preview'ı karşılaştırıyor. Hydrogen'ın daha hızlı çalıştığını, siyah ekran veya titreme olmadığını ve görüntünün daha az ayrıntılı olduğunu bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-poster-1263b041a256.jpg" alt="Case 160 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121551796766376081-1-url-884003aa822f.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-162"></a>
### Örnek 162: [Mevcut Geçiş Tasarımını Sorgulamak](https://x.com/is_llll/status/2121565725072490559) (hazırlayan [@is_llll](https://x.com/is_llll))

**Kodlama ajanlarından geçiş sırasında mevcut mimarinin değiştirilip değiştirilmemesini değerlendirmelerini isteyin.**

Yazar, Hydrogen ve Argon'un mevcut yaklaşımı desteklediği, Claude Opus'un ise mimariyi değiştirip geçişi öne çekmeyi önerdiği incelemeyi gösteriyor. Sonuç tek bir projeye ait.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-1-url-56675d463c82.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-1-url-56675d463c82.jpg" alt="Case 162 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-2-url-beda96ffecef.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121565725072490559-2-url-beda96ffecef.jpg" alt="Case 162 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Limit | Tarih: 2026-11-14

---

<a id="case-165"></a>
### Örnek 165: [İki Model Tapınaktan Kaçış Oyununu Yorumluyor](https://x.com/runable_hq/status/2121596515474964556) (hazırlayan [@runable_hq](https://x.com/runable_hq))

**Aynı oyun fikrinde ışık ve atmosferin sahneyi ne kadar anlaşılır kıldığını karşılaştırın.**

Runable, tapınaktan kaçış oyununun Hydrogen ve Argon uygulamalarını gösteriyor. Sağlayıcı Hydrogen'ın ışığını daha atmosferik, Argon sahnesini daha aydınlık buluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-poster-b0d664885bbd.jpg" alt="Case 165 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121596515474964556-1-url-a831fe608f92.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-166"></a>
### Örnek 166: [Üç Gemini Modeli Ralli Aracı Canlandırıyor](https://x.com/teddyaisi/status/2121604816380010719) (hazırlayan [@teddyaisi](https://x.com/teddyaisi))

**Eğimli virajda süspansiyon davranışının ve lastik tutuşunun inandırıcılığını değerlendirin.**

Yazar taş ocağı sahnesinde Carbon, Argon ve Hydrogen'ın Three.js arazi aracı animasyonlarını karşılaştırıyor. Görev, eğimli toprak yolda süspansiyon sıkışması ve kayma içeriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-poster-43e4dce8c386.jpg" alt="Case 166 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121604816380010719-1-url-1ff8adb8dbf8.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-169"></a>
### Örnek 169: [İki Modelle Chasing Views Animasyonu](https://x.com/VulKan42069/status/2121625271493382166) (hazırlayan [@VulKan42069](https://x.com/VulKan42069))

**Çıktıyı ve süreyi modellerin akıl yürütme ayarlarıyla birlikte karşılaştırın.**

Yazar Hydrogen Extra High ve Opus 5.5 High ile Chasing Views animasyonlarını gösteriyor. Sırasıyla 22 ve 18 dakika bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-poster-417076bec162.jpg" alt="Case 169 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121625271493382166-1-url-99037a7f383c.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-170"></a>
### Örnek 170: [Design Creativity Bench'te Hız ve Maliyet](https://x.com/Kombaico/status/2121635837180031129) (hazırlayan [@Kombaico](https://x.com/Kombaico))

**Yaratıcılık puanıyla birlikte tasarım başına üretim süresini ve maliyeti karşılaştırın.**

Testi yürüten ekip Hydrogen için 49,4 yaratıcılık puanı ve tasarım başına medyan 3,4 dakika ile 0,39 USD bildiriyor. Bu değerlendirmede Argon daha yavaş ve ucuz, Carbon daha yavaş ve pahalı.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121635837180031129-1-url-57c79a2b40a8.png" alt="Case 170 source image 1" height="360"></a>

Tür: Benchmark | Tarih: 2026-11-14

---

<a id="case-172"></a>
### Örnek 172: [Dört Model Çölde Dörtnala Koşan Atı Canlandırıyor](https://x.com/Marlenuii/status/2121664345818235177) (hazırlayan [@Marlenuii](https://x.com/Marlenuii))

**Işığa veya modelleme ayrıntısına geçmeden önce toynağın zemine temasını ve ağırlık aktarımını karşılaştırın.**

Yazar çölde koşan at için Astra, Carbon, Fable 5.2 ve Hydrogen'ı karşılaştırıyor. Astra'nın yürüyüşünü tercih ediyor ve Hydrogen'ın at modelinin yapısını eleştiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-poster-f9ece0d2ee8e.jpg" alt="Case 172 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121664345818235177-1-url-a75b11b13589.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-174"></a>
### Örnek 174: [FrontierCS 2'de Bilgisayar Bilimi Araştırması](https://x.com/wenhaocha1/status/2121679887400403308) (hazırlayan [@wenhaocha1](https://x.com/wenhaocha1))

**Standart kodlama testlerine bir araştırma kıyaslaması ekleyip çalışma ortamını kaydedin.**

Kaynak, Antigravity'deki Hydrogen'ın FrontierCS 2 başarı oranında yedinci olduğunu bildiriyor. Kıyaslama bilgisayar bilimi araştırmalarından teknik problemleri kullanıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-poster-07cfc41ea145.jpg" alt="Case 174 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121679887400403308-1-url-00a50e730fe3.mp4)

Tür: Benchmark | Tarih: 2026-11-14

---

<a id="case-175"></a>
### Örnek 175: [Dört Modelle Bulutların Üzerinde Rio](https://x.com/EnvolDev/status/2121701704139956250) (hazırlayan [@EnvolDev](https://x.com/EnvolDev))

**Aynı yaratıcı görevde maliyet, süre ve algılanan kaliteyi karşılaştırın.**

Testi yapan kişi Hydrogen Extra High için 6,21 USD bildiriyor ve en az bu sonucu beğeniyor. Astra bu çalıştırmada daha kısa sürdü. Rapor yerleşik video üretimini doğrulamıyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-poster-80a0c17165fb.jpg" alt="Case 175 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121701704139956250-1-url-a0883aeab316.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-176"></a>
### Örnek 176: [GBENCH Teknik Görevlerinde Hydrogen](https://x.com/leo_linsky/status/2121710421891780864) (hazırlayan [@leo_linsky](https://x.com/leo_linsky))

**Teknik işi değerlendirirken fiyat ve süreyle birlikte doğrulanabilir kodlu ve kodsuz sonuçlara bakın.**

Testi yürüten ekip, devre tasarımı ve soyut akıl yürütme gibi görevler içeren GBENCH'te Hydrogen sonuçlarını bildiriyor. Benzer fiyat ve hızda Sol'u daha rekabetçi buluyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-1-url-eb704fc94009.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-1-url-eb704fc94009.jpg" alt="Case 176 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-2-url-36e5f1c98a86.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-2-url-36e5f1c98a86.png" alt="Case 176 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-3-url-8ab372b95cb1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121710421891780864-3-url-8ab372b95cb1.jpg" alt="Case 176 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

Tür: Benchmark | Tarih: 2026-11-14

---

<a id="case-177"></a>
### Örnek 177: [Arabalara Paralel Park Öğretmek](https://x.com/noclipepe/status/2121734795738652934) (hazırlayan [@noclipepe](https://x.com/noclipepe))

**Oluşturulan simülasyonlarda öğrenme ilerlemesini ve son başarı oranlarını karşılaştırın.**

Yazar aynı görevde Hydrogen ile 44 aracın 5'inin, Fable 5.2 ile 40 aracın 26'sının park ettiğini bildiriyor. Bu çalıştırmalarda yapım süresi 5,6 ve 24 dakika.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-poster-2fe3fabb8c41.jpg" alt="Case 177 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121734795738652934-1-url-486598aaf9f0.mp4)

Tür: Evaluation | Tarih: 2026-11-14

---

<a id="case-181"></a>
### Örnek 181: [Terminal-Bench 4.0'da Hydrogen](https://x.com/gosrum/status/2121785156273160558) (hazırlayan [@gosrum](https://x.com/gosrum))

**Komut satırı kodlama modeli seçerken tamamlama oranını ve görev maliyetini birlikte değerlendirin.**

Bağımsız Terminal-Bench 4.0 çalıştırması Hydrogen'ı Claude Opus 5.5 ve GPT-6.1 Sol ile karşılaştırıyor. Testi yapan kişi yakın puanlar ve iki model arasında maliyet bildiriyor. Test ortamının olgunluğunun gerçek kullanımı etkilediğini belirtiyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-1-url-cd8ea8d294e1.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-1-url-cd8ea8d294e1.jpg" alt="Case 181 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-2-url-485667e4cf89.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121785156273160558-2-url-485667e4cf89.jpg" alt="Case 181 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Benchmark | Tarih: 2026-11-15

---

<a id="case-183"></a>
### Örnek 183: [Üç Gemini Modeli Ahtapotu Canlandırıyor](https://x.com/teddyaisi/status/2121800606406885880) (hazırlayan [@teddyaisi](https://x.com/teddyaisi))

**Kayanın kavranmasının gövdeyi ileri taşıyıp taşımadığına bakın.**

Yazar Carbon, Argon ve Hydrogen'ın Three.js sahnesinde kayaya tutunup ilerleyen ahtapot animasyonlarını gösteriyor. Kolun kavrama hareketiyle gövdenin ilerlemesi arasındaki bağlantıyı karşılaştırmayı öneriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-poster-ffc45ecb4ab3.jpg" alt="Case 183 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121800606406885880-1-url-1aa060bd3f42.mp4)

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-187"></a>
### Örnek 187: [Bir Kale Modelleme Testi](https://x.com/nemumusitocha/status/2121848375998063012) (hazırlayan [@nemumusitocha](https://x.com/nemumusitocha))

**Farklı model çalıştırmalarında kale çıktılarını ve kaynak kullanımını karşılaştırın.**

Yazar Hydrogen'ın 3B kalesini gösteriyor ve önceki model karşılaştırmalarına bağlantı veriyor. Bildirilen haftalık Google AI Pro kotasının %3'ü bu çalıştırmaya ait.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-poster-d0eac8402c7a.jpg" alt="Case 187 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-1-url-bed405f9a915.mp4)

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-2-url-7651a5296a9f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-2-url-7651a5296a9f.jpg" alt="Case 187 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-3-url-1d59eac2a5b7.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-3-url-1d59eac2a5b7.jpg" alt="Case 187 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-4-url-00e8a6b2fc60.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121848375998063012-4-url-00e8a6b2fc60.jpg" alt="Case 187 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-191"></a>
### Örnek 191: [Kapsam Büyüyünce Değişen Proje Tahmini](https://x.com/KrishnaBuildsAI/status/2121883172036309500) (hazırlayan [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**Teslim tahmini belirgin şekilde değiştiğinde modelden kapsamı ve varsayımları açıklamasını isteyin.**

Yazar, gerekli özellikleri içeren daha gerçekçi takvim isteyince bir aylık tahminin bir yıla çıktığı konuşmayı paylaşıyor. Gerçek proje süresi bilinmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121883172036309500-1-url-02946013d2d9.jpg" alt="Case 191 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-15

---

<a id="case-193"></a>
### Örnek 193: [Artık Yılı da İçeren Takvim Sorusu](https://x.com/itsvishaltwt/status/2121891117050589249) (hazırlayan [@itsvishaltwt](https://x.com/itsvishaltwt))

**Basit bir dönüşüm sorusunda takvime özgü durumların hesaba katılıp katılmadığını kontrol edin.**

Yazar Hydrogen High ve GPT'ye bir yılın kaç saniye olduğunu sordu. İki ekran görüntüsü de normal yıl ile artık yılı ayırıyor. Hydrogen ayrıca ortalama Gregoryen yılı hesaplıyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-1-url-b2270fbaacb0.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-1-url-b2270fbaacb0.jpg" alt="Case 193 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-2-url-cf9b4c45a1e3.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121891117050589249-2-url-cf9b4c45a1e3.jpg" alt="Case 193 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-196"></a>
### Örnek 196: [Yanıtta Güncelliğini Yitirmiş Abonelik Sınırları](https://x.com/take14262/status/2121934737539514533) (hazırlayan [@take14262](https://x.com/take14262))

**Araştırma asistanını değerlendirirken güncel plan şartlarını ve model adlarını birincil kaynaklardan doğrulayın.**

Yazar, Hydrogen'ın benzer bir model adını karıştırdığı ve Qwen planı için eski zaman pencereleri verdiği yanıtları gösteriyor. Bunlar kayıttaki belirli referans hataları.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-1-url-c51825192acc.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-1-url-c51825192acc.png" alt="Case 196 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-2-url-ae838791b312.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121934737539514533-2-url-ae838791b312.png" alt="Case 196 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Limit | Tarih: 2026-11-15

---

<a id="case-197"></a>
### Örnek 197: [WebGL Animasyonunun Hikâyesini İyileştirmek](https://x.com/snakajima/status/2121939899242996058) (hazırlayan [@snakajima](https://x.com/snakajima))

**Teknik açıdan karmaşık ilk sürümde akış belirsizse daha güçlü bir hikâye isteyin.**

Yazar ilk WebGL sürümünü iliştiriyor ve görsel karmaşa ile hikâye eksikliğine dair geri bildirimden sonra ikinci sürümü gösteriyor. İyileştirmeyi beğeniyor ama Claude Code çıktısını tercih ediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-poster-c8328f56b503.jpg" alt="Case 197 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121939899242996058-1-url-0b308ee4f3c7.mp4)

Tür: Limit | Tarih: 2026-11-15

---

<a id="case-199"></a>
### Örnek 199: [İki Model Dağda Ejderha Dövüşünü Kodluyor](https://x.com/DrstaOne/status/2121947540509831302) (hazırlayan [@DrstaOne](https://x.com/DrstaOne))

**Aynı sahnede iki karakterin etkileşiminin nasıl canlandırıldığını karşılaştırın.**

Yazar dağ tapınağının üzerindeki ejderha dövüşü için Qwen-4 Max ve Hydrogen ile kodla oluşturulan animasyonları paylaşıyor. İstemi başka bir üreticiye atfediyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-poster-a3224c417316.jpg" alt="Case 199 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121947540509831302-1-url-a943b660cd56.mp4)

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-201"></a>
### Örnek 201: [Yeniden Kullanılabilir Three.js Pelikan İstemi](https://x.com/Aki_LIG/status/2121960943361896596) (hazırlayan [@Aki_LIG](https://x.com/Aki_LIG))

**Bisiklet animasyonunda bacak, tekerlek ve yön hareketlerinin uyumunu sınayın.**

Yazar eksiksiz Japonca Three.js istemini ve Hydrogen'ın sahil yolundaki çıktısını yayımlıyor. Aynı istemi daha önce GPT-6.1 Terra'ya verdiğini bildiriyor. Bu kayıt Hydrogen'a ait.

**İstem:**

```
Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-poster-f90f56ce994c.jpg" alt="Case 201 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121960943361896596-1-url-172b40fda30a.mp4)

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-205"></a>
### Örnek 205: [Üç Ortamda Aynı Kır Evi İstemi](https://x.com/doe_naps/status/2121999317628330476) (hazırlayan [@doe_naps](https://x.com/doe_naps))

**Görsel bir görevi başka model ayarı veya platforma taşırken çıktı biçimini kontrol edin.**

Yazar Antigravity'de Hydrogen High ve Carbon High, AI Studio'da Hydrogen Extra High ile durağan çıktı bildiriyor. Arena'da Hydrogen etiketli çalıştırma animasyonlu SVG üretti. Model sürümü bağımsız olarak belirlenmedi.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-poster-3ac93b436953.jpg" alt="Case 205 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-1-url-80af2e3cffcd.mp4)

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-2-url-61c8ea9c30fc.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-2-url-61c8ea9c30fc.jpg" alt="Case 205 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-3-url-e52b66f1cf3f.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-3-url-e52b66f1cf3f.jpg" alt="Case 205 source image 2" width="100%"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-4-url-c4376faa6be5.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2121999317628330476-4-url-c4376faa6be5.jpg" alt="Case 205 source image 3" width="100%"></a>
</td>
<td width="50%" valign="top"></td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-206"></a>
### Örnek 206: [Tek İstemle Pano Karşılaştırması](https://x.com/fiapp_pro/status/2122014257667846338) (hazırlayan [@fiapp_pro](https://x.com/fiapp_pro))

**Ortak bir arayüz istemiyle düzeni ve bilgi hiyerarşisini karşılaştırın.**

Yazar GPT-6.1 Sol ve Hydrogen'a atfettiği web arayüzlerini yan yana paylaşıyor. Görseller karşılaştırmaya elverişli. Uygulama, ayarlar ve işlevler belirtilmiyor.

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-1-url-a5bc19cd8b96.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-1-url-a5bc19cd8b96.jpg" alt="Case 206 source image 1" width="100%"></a>
</td>
<td width="50%" valign="top" align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-2-url-41c8d506d533.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122014257667846338-2-url-41c8d506d533.jpg" alt="Case 206 source image 2" width="100%"></a>
</td>
</tr>
</table>

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-209"></a>
### Örnek 209: [İki Model Yandan Kaydırmalı Animasyon Kodluyor](https://x.com/rubenssoto_ai/status/2122035198728814753) (hazırlayan [@rubenssoto_ai](https://x.com/rubenssoto_ai))

**Oluşturulan aksiyon sahnelerinde hareket sürekliliğine ve yapım maliyetine bakın.**

Yazar Hydrogen ve GPT-6 Astra'nın yandan kaydırmalı sahnelerini karşılaştırıyor. Bu iki çalıştırmada Hydrogen'ın hareketini doğal buluyor ve daha düşük maliyet bildiriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-poster-5b1ecdfb8a0a.jpg" alt="Case 209 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122035198728814753-1-url-aa0d380f9f85.mp4)

Tür: Evaluation | Tarih: 2026-11-15

---

<a id="case-212"></a>
### Örnek 212: [Japonca Yanıtta Görüntülenmeyen Formüller](https://x.com/ToraMutton/status/2122131489718759930) (hazırlayan [@ToraMutton](https://x.com/ToraMutton))

**TeX komutlu yanıtlarda doğrulukla birlikte matematiğin ekranda nasıl göründüğünü sınayın.**

Yazar Hydrogen'a geçtikten sonra Japonca Gemini yanıtında dizilmiş denklemler yerine ham matematik işaretleri görüyor. Ekran görüntüsü arayüzdeki tek bir biçim hatasını gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122131489718759930-1-url-5d7e834e9209.jpg" alt="Case 212 source image 1" height="360"></a>

Tür: Limit | Tarih: 2026-11-16

---

<a id="case-214"></a>
### Örnek 214: [Sessiz Kalma Talimatını Sınamak](https://x.com/KrishnaBuildsAI/status/2122169915759345998) (hazırlayan [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI))

**İş akışı gerektiriyorsa modelin hiç yanıt üretmemesini sınayın.**

Yazar cevapsız kalma testinin ekran görüntüsünü paylaşıyor ve Carbon ile Argon'da farklı davranış bildiriyor. Paylaşım bir deneme grubunu gösteriyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122169915759345998-1-url-fbeac4a7fd19.jpg" alt="Case 214 source image 1" height="360"></a>

Tür: Evaluation | Tarih: 2026-11-16

---

<a id="case-216"></a>
### Örnek 216: [Üç Model Elektrik Motorunu Açıklıyor](https://x.com/analogalok/status/2122221106304352257) (hazırlayan [@analogalok](https://x.com/analogalok))

**Aynı simülasyon istemiyle görsel netliği ve öğretici denetimleri karşılaştırın.**

Yazar Hydrogen'ı iki Qwen modeliyle karşılaştırdı. Hydrogen'ın 3B motorunu ve fizik açıklamalarını tercih etti. Değerlendirme tek karşılaştırmaya ait.

**İstem:**

```
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-poster-2fb335efd829.jpg" alt="Case 216 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122221106304352257-1-url-50eef72421a8.mp4)

Tür: Evaluation | Tarih: 2026-11-16

---

<a id="case-217"></a>
### Örnek 217: [İki Model Akışıyla Masa Sahnesi Animasyonu](https://x.com/GeroXBT/status/2122234332102435128) (hazırlayan [@GeroXBT](https://x.com/GeroXBT))

**Sahne ayrıntılarını, ses düzeyini ve sondaki sabit kareyi asıl istemle karşılaştırın.**

Yazar API üzerinden aynı istemle Hydrogen ve Astra destekli masa animasyonları üretti. Gemini sonucunu daha akıcı buluyor ama son karede hareketin sürdüğünü ve sesin daha kısık olduğunu söylüyor. İşleme hattı belirtilmiyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-poster-ca038d8fd7f5.jpg" alt="Case 217 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122234332102435128-1-url-a5be55c770d6.mp4)

Tür: Evaluation | Tarih: 2026-11-16

---

<a id="case-221"></a>
### Örnek 221: [Prosedürel Sesli 2B Köy](https://x.com/marcthecreatorr/status/2122266495216459841) (hazırlayan [@marcthecreatorr](https://x.com/marcthecreatorr))

**Yapım süresinin yanında seslerin ekrandaki olaylara uyup uymadığını kontrol edin.**

Yazar 2B köyde Qwen 4 Max ve Extra High ayarındaki Hydrogen'ı karşılaştırıyor. Qwen için yaklaşık 75 dakika ve 0,90 USD, Hydrogen için 12 dakika ve 1,70 USD bildiriyor. Hydrogen'ın müziğini olaylara daha uyumlu buluyor.

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-poster-3da6df64a1f3.jpg" alt="Case 221 source video poster" height="360"></a>

[Kaynak videoyu oynat](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-gemini-4-hydrogen-use-cases/hydrogen-20261117/media/2122266495216459841-1-url-1c3e66535104.mp4)

Tür: Evaluation | Tarih: 2026-11-16

---

<a id="related-repositories"></a>
## İlgili depolar

- [Gemini 4 Carbon Guide and Use Cases](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases): Gemini 4 Carbon örnekleri ve karşılaştırmaları

<a id="acknowledge"></a>
## 🙏 Teşekkürler

Hydrogen çalışmalarını herkese açık olarak paylaşan üreticilere, geliştiricilere ve değerlendiricilere teşekkürler.

**Kaynak üreticileri:**

[@antigravity](https://x.com/antigravity), [@shengzheyao](https://x.com/shengzheyao), [@thtbee_](https://x.com/thtbee_), [@GoogleAI](https://x.com/GoogleAI), [@Da7_Tech](https://x.com/Da7_Tech), [@tulseedoshi](https://x.com/tulseedoshi), [@techartist_](https://x.com/techartist_), [@thebuggeddev](https://x.com/thebuggeddev), [@IamEmily2050](https://x.com/IamEmily2050), [@SidraMiconi](https://x.com/SidraMiconi), [@Google](https://x.com/Google), [@vamsibatchuk](https://x.com/vamsibatchuk), [@ChanduThota](https://x.com/ChanduThota), [@notjazii](https://x.com/notjazii), [@vib3coded](https://x.com/vib3coded), [@SPAC89](https://x.com/SPAC89), [@nehstrr3](https://x.com/nehstrr3), [@The_Alex](https://x.com/The_Alex), [@ai_for_success](https://x.com/ai_for_success), [@RezAIT00](https://x.com/RezAIT00), [@kimmonismus](https://x.com/kimmonismus), [@LuminaBench](https://x.com/LuminaBench), [@rubenssoto_ai](https://x.com/rubenssoto_ai), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@danielmckinn0n](https://x.com/danielmckinn0n), [@EnvolDev](https://x.com/EnvolDev), [@Haleeeemahh](https://x.com/Haleeeemahh), [@kickingkeys](https://x.com/kickingkeys), [@thehypedotnews](https://x.com/thehypedotnews), [@SahilPanhotra](https://x.com/SahilPanhotra), [@DanielZambrini](https://x.com/DanielZambrini), [@Bhavani_00007](https://x.com/Bhavani_00007), [@marcthecreatorr](https://x.com/marcthecreatorr), [@StatsWire](https://x.com/StatsWire), [@thegenioo](https://x.com/thegenioo), [@Angaisb_](https://x.com/Angaisb_), [@AI_Screening](https://x.com/AI_Screening), [@Inmerson](https://x.com/Inmerson), [@auricxofficial](https://x.com/auricxofficial), [@huang18825](https://x.com/huang18825), [@AiHubMix](https://x.com/AiHubMix), [@HarshithLucky3](https://x.com/HarshithLucky3), [@pankajkumar_dev](https://x.com/pankajkumar_dev), [@abhinavflac](https://x.com/abhinavflac), [@hakmgpt](https://x.com/hakmgpt), [@arena](https://x.com/arena), [@ValsAI](https://x.com/ValsAI), [@cursor_ai](https://x.com/cursor_ai), [@IndependentEco](https://x.com/IndependentEco), [@n8n_io](https://x.com/n8n_io), [@levie](https://x.com/levie), [@cognition](https://x.com/cognition), [@chanelluuh](https://x.com/chanelluuh), [@xKaka1456](https://x.com/xKaka1456), [@amanunreal](https://x.com/amanunreal), [@mercor](https://x.com/mercor), [@soyamiruku](https://x.com/soyamiruku), [@studio_yebisu](https://x.com/studio_yebisu), [@patience_cave](https://x.com/patience_cave), [@Octoberry](https://x.com/Octoberry), [@nin222](https://x.com/nin222), [@skalskip92](https://x.com/skalskip92), [@AdamHoltererer](https://x.com/AdamHoltererer), [@gigabit_million](https://x.com/gigabit_million), [@jan_volad](https://x.com/jan_volad), [@luckeyfaraday](https://x.com/luckeyfaraday), [@s_batzoglou](https://x.com/s_batzoglou), [@kkitase](https://x.com/kkitase), [@bijanbowen](https://x.com/bijanbowen), [@leo114119](https://x.com/leo114119), [@gosrum](https://x.com/gosrum), [@andonlabs](https://x.com/andonlabs), [@openclaw](https://x.com/openclaw), [@CodeByPoonam](https://x.com/CodeByPoonam), [@MichaelLee009](https://x.com/MichaelLee009), [@ayyh_18](https://x.com/ayyh_18), [@kimura_0314](https://x.com/kimura_0314), [@cagrimbakirci](https://x.com/cagrimbakirci), [@yohakujpn](https://x.com/yohakujpn), [@YxzRainy](https://x.com/YxzRainy), [@ashen_one](https://x.com/ashen_one), [@parves075](https://x.com/parves075), [@Jackson77li](https://x.com/Jackson77li), [@CadX_Studio](https://x.com/CadX_Studio), [@qingzhoucloud](https://x.com/qingzhoucloud), [@Stargridcompass](https://x.com/Stargridcompass), [@noclipepe](https://x.com/noclipepe), [@johnsanthosh01](https://x.com/johnsanthosh01), [@camperaigg](https://x.com/camperaigg), [@Letta_AI](https://x.com/Letta_AI), [@livekit](https://x.com/livekit), [@ash_twtz](https://x.com/ash_twtz), [@doe_naps](https://x.com/doe_naps), [@smalkalbani](https://x.com/smalkalbani), [@peach2k2](https://x.com/peach2k2), [@kepochnik](https://x.com/kepochnik), [@PawelHuryn](https://x.com/PawelHuryn), [@NovaXCode](https://x.com/NovaXCode), [@ZryMiller](https://x.com/ZryMiller), [@MatinSenPai](https://x.com/MatinSenPai), [@remoteugur](https://x.com/remoteugur), [@quintanilha](https://x.com/quintanilha), [@soumyadesign](https://x.com/soumyadesign), [@gwammyy](https://x.com/gwammyy), [@agenticjay](https://x.com/agenticjay), [@notoro_ai](https://x.com/notoro_ai), [@Its_lakshya_ai](https://x.com/Its_lakshya_ai), [@hiromsa](https://x.com/hiromsa), [@gmi_cloud](https://x.com/gmi_cloud), [@naufaldi](https://x.com/naufaldi), [@badboyfoxy](https://x.com/badboyfoxy), [@laopai1990](https://x.com/laopai1990), [@k2sbhai](https://x.com/k2sbhai), [@NFT_Chen](https://x.com/NFT_Chen), [@oasisfeng](https://x.com/oasisfeng), [@tetumemo](https://x.com/tetumemo), [@Beamsters1](https://x.com/Beamsters1), [@is_llll](https://x.com/is_llll), [@shinshin86](https://x.com/shinshin86), [@xiangning0](https://x.com/xiangning0), [@runable_hq](https://x.com/runable_hq), [@teddyaisi](https://x.com/teddyaisi), [@ohayou792](https://x.com/ohayou792), [@VulKan42069](https://x.com/VulKan42069), [@Kombaico](https://x.com/Kombaico), [@GoGoFly23](https://x.com/GoGoFly23), [@Marlenuii](https://x.com/Marlenuii), [@wenhaocha1](https://x.com/wenhaocha1), [@leo_linsky](https://x.com/leo_linsky), [@UWhQC5DHKuVq](https://x.com/UWhQC5DHKuVq), [@yamachan_ai_log](https://x.com/yamachan_ai_log), [@nemumusitocha](https://x.com/nemumusitocha), [@Saboo_Shubham_](https://x.com/Saboo_Shubham_), [@nasuvit_z](https://x.com/nasuvit_z), [@KrishnaBuildsAI](https://x.com/KrishnaBuildsAI), [@chetaslua](https://x.com/chetaslua), [@itsvishaltwt](https://x.com/itsvishaltwt), [@loganlu51268](https://x.com/loganlu51268), [@take14262](https://x.com/take14262), [@snakajima](https://x.com/snakajima), [@DrstaOne](https://x.com/DrstaOne), [@Aki_LIG](https://x.com/Aki_LIG), [@bei351009016](https://x.com/bei351009016), [@shengtang135754](https://x.com/shengtang135754), [@fiapp_pro](https://x.com/fiapp_pro), [@Moleh1ll](https://x.com/Moleh1ll), [@ivanleomk](https://x.com/ivanleomk), [@itshoseyn](https://x.com/itshoseyn), [@ToraMutton](https://x.com/ToraMutton), [@Awed_Urshy](https://x.com/Awed_Urshy), [@fukubaya](https://x.com/fukubaya), [@analogalok](https://x.com/analogalok), [@GeroXBT](https://x.com/GeroXBT), [@antiAIvo](https://x.com/antiAIvo), [@nyapan_mohy](https://x.com/nyapan_mohy), [@ivy432hz](https://x.com/ivy432hz), [@AvaSinclairAi_](https://x.com/AvaSinclairAi_)

*Atıflar belirtilen herkese açık kaynakları izler ve ilk üreticiyi belirlemeyebilir. Düzeltme veya kaldırma talepleri için herkese açık bir kaynak ekleyerek sorun kaydı açın.*

Katkı kontrol listesini izleyerek bir sorun kaydı veya değişiklik isteği üzerinden kaynaklarla desteklenen bir örnek önerin.
