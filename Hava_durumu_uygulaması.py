"""

 Hava Durumu Uygulaması:
 
Proje Tanımı: 
Bir şehir için hava durumunu tahmin eden bir uygulama yazın. Şehir ve sıcaklık bilgisi girdi olarak alınacak ve önerilerde bulunulacak.

İstenilen Özellikler:
Şehir ekleme ve sıcaklık tahmini ekleme.
Şehir adına göre hava durumunu sorgulama.
Sıcaklığa göre tavsiye verme:
0°C altı: "Soğuk, sıkı giyinin."
0°C-15°C arası: "Serin, mont almayı unutmayın."
15°C üzeri: "Hava güzel, rahat giyin."

Yönerge:
Bir Sehir sınıfı oluşturun. Bu sınıf, şehir adını ve sıcaklık bilgisini saklasın.
Bir HavaDurumu sınıfı oluşturun. Şehir ekleme, sıcaklık güncelleme ve tavsiye verme gibi işlemleri yönetin.


"""

class Sehir:
    def __init__(self, ad, sicaklik):
        self.ad = ad
        self.sicaklik = sicaklik

    def __str__(self):
        return f"{self.ad} şehrinin sıcaklığı: {self.sicaklik}°C"
    
class HavaDurumu:
    def __init__(self):
        self.sehirler = {}

    def sehir_ekle(self, sehir):
        self.sehirler[sehir.ad] = sehir

    def sicaklik_guncelle(self, sehir_adı, yeni_sicaklik):
        if sehir_adı in self.sehirler:
            self.sehirler[sehir_adı].sicaklik = yeni_sicaklik
        else:
            print("Böyle bir şehir bulunamadı.")

    def hava_durumu_sorgula(self, sehir_adı):
        if sehir_adı in self.sehirler:
            sehir = self.sehirler[sehir_adı]
            if sehir.sicaklik < 0:
                print("Soğuk, sıkı giyinin.")
            elif 0 <= sehir.sicaklik < 15:
                print("Serin, mont almayı unutmayın.")
            else:
                print("Hava güzel, rahat giyin.")
        else:
            print("Böyle bir şehir bulunamadı.")

hava_durumu = HavaDurumu()

while True:
    print("\n1. Şehir Ekle\n2. Sıcaklık Güncelle\n3. Hava Durumu Sorgula\n4. Çıkış")
    secim = input("Seçenek: ")

    if secim == '1':
        sehir_adı = input("Şehir adı: ")
        sicaklik = float(input("Sıcaklık: "))
        hava_durumu.sehir_ekle(Sehir(sehir_adı, sicaklik))
    elif secim == '2':
        sehir_adı = input("Hangi şehrin sıcaklığını güncelleyeceksiniz? ")
        yeni_sicaklik = float(input("Yeni sıcaklık: "))
        hava_durumu.sicaklik_guncelle(sehir_adı, yeni_sicaklik)
    elif secim == '3':
        sehir_adı = input("Hangi şehrin hava durumunu öğrenmek istiyorsunuz? ")
        hava_durumu.hava_durumu_sorgula(sehir_adı)
    elif secim == '4':
        break
    else:
        print("Geçersiz seçenek.")

