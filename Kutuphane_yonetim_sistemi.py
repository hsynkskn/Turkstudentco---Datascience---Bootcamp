"""

Kütüphane Yönetim Sistemi:

Proje Tanımı:
 Bir kütüphane sistemini modelleyin. Kitap ekleme, kitap ödünç verme ve mevcut kitapları listeleme özellikleri sunan bir program yazın.

İstenilen Özellikler:
Kitap ekleme ve listeleme.
Kitapları ödünç verme ve geri alma.
Ödünç alınan kitapların listesini ayrı tutma.

Yönerge:
Kitap sınıfı oluşturun. Kitap adı, yazar adı ve ödünç alınma durumu (True/False) gibi bilgileri saklayın.
Kutuphane sınıfı oluşturun. Kitap ekleme, ödünç verme ve geri alma gibi metotları barındırın.


"""


class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi_mi = False

    def __str__(self):
        return f"{self.ad} - {self.yazar} (Ödünç Alındı: {'Evet' if self.odunc_alindi_mi else 'Hayır'})"
    
class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunc_alinanlar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitap_listesi(self):
        for kitap in self.kitaplar:
            print(kitap)

    def kitap_odunc_al(self, kitap_adı):
        for kitap in self.kitaplar:
            if kitap.ad == kitap_adı and not kitap.odunc_alindi_mi:
                kitap.odunc_alindi_mi = True
                self.odunc_alinanlar.append(kitap)
                print(f"{kitap_adı} kitabı ödünç alındı.")
                return
        print(f"{kitap_adı} kitabı bulunamadı veya zaten ödünç alınmış.")

    def kitap_geri_getir(self, kitap_adı):
        for kitap in self.odunc_alinanlar:
            if kitap.ad == kitap_adı:
                kitap.odunc_alindi_mi = False
                self.odunc_alinanlar.remove(kitap)
                print(f"{kitap_adı} kitabı geri getirildi.")
                return
        print(f"{kitap_adı} kitabı ödünç verilmemiş.")

    def odunc_alinan_kitaplar_listesi(self):
        for kitap in self.odunc_alinanlar:
            print(kitap)

kutuphane = Kutuphane()

# Örnek kitaplar ekleme
kutuphane.kitap_ekle(Kitap("Vatan Yahut Silistre", "Namık Kemal"))
kutuphane.kitap_ekle(Kitap("Çalı Kuşu", "Reşat Nuri Güntekin"))

while True:
    print("\n1. Kitap Ekle\n2. Kitap Listesi\n3. Kitap Ödünç Al\n4. Kitap Geri Getir\n5. Ödünç Alınan Kitaplar\n6. Çıkış")
    secim = input("Seçenek: ")

    if secim == '1':
        ad = input("Kitap adı: ")
        yazar = input("Yazar adı: ")
        kutuphane.kitap_ekle(Kitap(ad, yazar))
    elif secim == '2':
        kutuphane.kitap_listesi()
    elif secim == '3':
        kitap_adı = input("Ödünç almak istediğiniz kitap adı: ")
        kutuphane.kitap_odunc_al(kitap_adı)
    elif secim == '4':
        kitap_adı = input("Geri getirmek istediğiniz kitap adı: ")
        kutuphane.kitap_geri_getir(kitap_adı)
    elif secim == '5':
        kutuphane.odunc_alinan_kitaplar_listesi()
    elif secim == '6':
        break
    else:
        print("Geçersiz seçenek.")

