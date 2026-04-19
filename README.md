🚚 Akıllı Lojistik ve Gerçek Zamanlı Araç Takip Sistemi
Bu proje, Bulut Bilişim Dersi - Proje 2 kapsamında; IoT cihazlarından gelen verilerin gerçek zamanlı olarak bulut ortamında işlenmesi ve depolanması amacıyla geliştirilmiştir.

🚀 Proje Hakkında
Sistem, bir lojistik firmasının araçlarından gelen anlık hız ve konum verilerini simüle eder. Veriler bulut üzerinde analiz edilerek güvenli sürüş takibi yapılmasına olanak sağlar.

🛠️ Teknik Mimari
Projede dökümana uygun olarak aşağıdaki servisler ve protokoller kullanılmıştır:

Veri Kaynağı: Python tabanlı IoT simülatörü.

Protokol: HTTP/POST (Real-time stream simulation).

Hesaplama (Compute): AWS Lambda (Serverless).

Veritabanı: AWS DynamoDB (NoSQL).

📝 Uygulama Adımları (Commit Geçmişi)
Aşama 1: Proje senaryosu belirlendi ve GitHub reposu oluşturuldu.

Aşama 2: AWS üzerinde KamyonVerileri tablosu (DynamoDB) yapılandırıldı.

Aşama 3: Veritabanı ve bulut fonksiyonu arasındaki bağlantı için IAM politikaları (Permission) düzenlendi.

Aşama 4: AWS Lambda üzerinde Python 3.11 kullanılarak veri işleme ve analiz fonksiyonu yazıldı.

Aşama 5: Yerel cihaz simülatörü kodlandı ve sistem uçtan uca test edildi.

📊 Veri Analizi ve İşleme
Sistem sadece veriyi depolamakla kalmaz, aynı zamanda gelen her paket üzerinde şu analizi yapar:

Eğer gelen hiz değeri 90 km/s üzerindeyse, veri otomatik olarak TEHLIKELI olarak etiketlenir.

Analiz sonuçları DynamoDB üzerinde her satıra bir öznitelik (attribute) olarak eklenir.