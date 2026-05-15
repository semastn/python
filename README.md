# 🧛‍♂️ Vampir-Köylü Konsol Oyunu

Python ve SQLite kullanılarak geliştirilmiş, terminal tabanlı interaktif bir rol yapma (Vampir-Köylü) oyunudur.

## 📌 Proje Hakkında
Bu proje, popüler parti oyunu "Vampir-Köylü"nün Python ile dijitalleştirilmiş bir versiyonudur. Oyunun akışı, oyuncu durumları ve rastgele rol atamaları **SQLite** veritabanı kullanılarak anlık olarak işlenir ve kaydedilir. Temel CRUD operasyonları ve döngüsel oyun mantığı içeren bu proje, algoritmik düşünme ve veri yönetimi pratikleri barındırmaktadır.

## 🚀 Özellikler
* **Dinamik Oyuncu Yönetimi:** En az 6 kişiyle oynanabilir yapı ve dinamik isim doğrulama sistemi.
* **Adil Rol Dağıtımı:** Algoritmik olarak 1 Vampir, 1 Doktor ve geri kalanlar için Köylü rollerinin otomatik, benzersiz şekilde atanması.
* **Şifreli Admin Paneli:** Rollerin gizliliğini korumak için şifre korumalı (`admin123`) yönetici görüntüleme ekranı.
* **Gece/Gündüz Döngüsü Modülü:** * **Gece Fazı:** Vampir bir hedef seçer, Doktor birini korur. Eğer hedefler eşleşirse ölüm engellenir.
  * **Gündüz Fazı:** Hayatta kalan oyuncular kendi aralarında demokratik bir oylama yapar. Çoğunluk oyu alan kişi oyundan elenir, oyların eşitliği durumunda kimse elenmez.
* **Anlık Durum Takibi:** Tüm yaşama/ölme durumları anlık olarak `oyun.db` içerisindeki `oyuncular` tablosunda güncellenir.

## 🛠️ Kullanılan Teknolojiler
* **Python 3**
* **SQLite3** (Veri Tabanı Yönetimi)
* **Random Kütüphanesi** (Olasılık ve Dağıtım)

## 💻 Nasıl Çalıştırılır?
1. Projeyi bilgisayarınıza indirin.
2. Terminal veya Komut İstemcisi'ni (Command Prompt) açın.
3. Projenin bulunduğu dizine gidin ve dosyayı çalıştırın:
   ```bash
   python semaproje2.py
