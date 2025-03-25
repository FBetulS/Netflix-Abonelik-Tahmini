# Netflix Abonelik Tahmini

## 📖 Proje Hakkında
Bu proje, Netflix'in abonelik verilerini analiz ederek gelecekteki abonelik sayısını tahmin etmeyi amaçlamaktadır. Zaman serisi analizi kullanılarak, geçmiş verilerden yola çıkarak gelecekteki abonelik rakamları tahmin edilmektedir. Bu sayede, Netflix'in büyüme trendleri ve abonelik değişimleri hakkında bilgi edinmek mümkün olmaktadır.

## 🔗 Kaynaklar
- Hugging Face Uygulaması: [Netflix Abonelik Tahmini](https://huggingface.co/spaces/btulftma/netflix_abonelik_tahmini)

### Amaç
Projenin ana hedefi, Netflix'in abonelik verilerini kullanarak gelecekteki abonelik sayısını tahmin etmek ve bununla birlikte abonelik büyüme oranlarını analiz etmektir. Bu, Netflix gibi içerik sağlayıcıları için stratejik planlamada faydalı veriler sunabilir.

### Kullanılan Veriler
Proje, `Netflix-Subscriptions.csv` adlı bir veri seti kullanmaktadır. Bu veri seti, Netflix'in zaman içindeki abonelik sayılarını içermektedir. Aşağıdaki sütunlar bulunmaktadır:
- **Time Period**: Zaman dilimi (tarih)
- **Subscribers**: Abone sayısı

### Analiz Yöntemleri
Proje, çeşitli zaman serisi analiz yöntemleri kullanarak aşağıdaki adımları içermektedir:
1. **Veri Yükleme ve Görselleştirme**: Abonelik verilerinin zaman içinde nasıl değiştiğini gösteren grafikler.
2. **Çeyreklik ve Yıllık Büyüme Oranı Hesaplama**: Aboneliklerin çeyreklik ve yıllık büyüme oranlarının hesaplanması ve görselleştirilmesi.
3. **Zaman Serisi Ayrıştırması**: Abonelik verilerinin trend, mevsimsellik ve artık bileşenlere ayrıştırılması.
4. **ARIMA ve SARIMA Modelleri**: Abonelik verilerinin tahmin edilmesi için ARIMA ve SARIMA modellerinin uygulanması.
5. **Güven Aralıkları ile Tahminler**: Tahmin sonuçlarına güven aralıklarının eklenmesi.
6. **Veri Analizi ve Görselleştirme**: Abonelik büyüme oranlarının histogramları, scatter plot'lar ve kümülatif büyüme grafikleri.

### Sonuçlar
Proje, Netflix'in abonelik verilerinin analiz edilmesi ve gelecekteki abonelik sayısının tahmin edilmesi ile sonuçlanmaktadır. Kullanılan modellerin performansı karşılaştırılarak en iyi tahmin yöntemleri belirlenmiştir. Ayrıca, abonelik büyüme oranları ve zaman içindeki değişimlerin analizi ile stratejik içgörüler elde edilmiştir.

### Eklemeler
- Zaman serisi ayrıştırması ile trend ve mevsimsellik analizi.
- SARIMA modelinin mevsimsel etkileri içeren tahminleri.
- İnteraktif grafiklerle görsel iyileştirmeler.
