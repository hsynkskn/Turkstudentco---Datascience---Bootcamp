"""

Alışveriş Sepeti Uygulaması: 

Proje Tanımı:
 Bir e-ticaret sitesi için alışveriş sepeti uygulaması geliştirin. Kullanıcı ürün ekleyebilir, çıkarabilir ve toplam tutarı görebilir.

İstenilen Özellikler:
Ürün ekleme (ürün adı, fiyat ve miktar bilgisiyle).
Sepeti listeleme (ürün adı, miktarı ve fiyatı).
Sepetten ürün çıkarma.
Toplam tutarı hesaplama.

Yönerge:
Bir Urun sınıfı oluşturun. Ürün adı, fiyatı ve miktarı saklasın.
Bir Sepet sınıfı oluşturun. Ürün ekleme, çıkarma ve toplam hesaplama gibi işlemleri gerçekleştirin.



"""


class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

    def __str__(self):
        return f"{self.miktar} adet {self.ad} ({self.fiyat} TL)"
    
class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)

    def urun_cikar(self, urun_adı):
        for urun in self.urunler:
            if urun.ad == urun_adı:
                self.urunler.remove(urun)
                return
        print(f"{urun_adı} ürünü sepette bulunamadı.")

    def sepeti_listele(self):
        for urun in self.urunler:
            print(urun)

    def toplam_tutar(self):
        toplam = 0
        for urun in self.urunler:
            toplam += urun.fiyat * urun.miktar
        return toplam
    
# Bir sepet oluşturma
sepet = Sepet()

# Ürünler ekleme
sepet.urun_ekle(Urun("Elma", 2, 2))
sepet.urun_ekle(Urun("Armut", 3, 1))
sepet.urun_ekle(Urun("Muz", 4, 1))
sepet.urun_ekle(Urun("Çilek", 4, 10))

# Sepetteki ürünleri listeleme
sepet.sepeti_listele()

# Toplam tutarı hesaplama
print("Toplam Tutar:", sepet.toplam_tutar())

