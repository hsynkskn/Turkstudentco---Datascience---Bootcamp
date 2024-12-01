"""

 Basit Banka Sistemi:
 
Proje Tanımı: 
Bir banka sistemi tasarlayın. Kullanıcı hesap açabilir, para yatırabilir, çekebilir ve bakiye kontrolü yapabilir.

İstenilen Özellikler:
Kullanıcıların hesap açması (ad, hesap numarası, başlangıç bakiyesi ile).
Para yatırma ve çekme işlemleri.
Hesap bakiyesi sorgulama.
Birden fazla kullanıcıyı yönetebilme.

Yönerge:
Kullanici adında bir sınıf oluşturun. Bu sınıf, hesap numarasını ve bakiyeyi tutar.
Banka adında bir sınıf oluşturun. Bu sınıf, kullanıcıların oluşturulmasını ve işlemlerinin yapılmasını sağlar.
Giriş kontrolü (hesap numarasına göre) ve para çekme işleminde bakiye kontrolü ekleyin.


"""

class Kullanici:
    def __init__(self, ad, hesap_no, bakiye):
        self.ad = ad
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")

    def bakiye_sorgula(self):
        print(f"Bakiyeniz: {self.bakiye} TL")

class Banka:
    def __init__(self):
        self.musteriler = {}

    def hesap_ac(self, ad, bakiye):
        hesap_no = len(self.musteriler) + 1
        yeni_musteri = Kullanici(ad, hesap_no, bakiye)
        self.musteriler[hesap_no] = yeni_musteri
        print(f"Hesabınız açıldı. Hesap numaranız: {hesap_no}")

    def giris_yap(self, hesap_no):
        if hesap_no in self.musteriler:
            return self.musteriler[hesap_no]
        else:
            print("Geçersiz hesap numarası.")
            return None
        
banka = Banka()

while True:
    print("\n1. Hesap Aç\n2. Giriş Yap\n3. Çıkış")
    secim = input("Seçiminiz: ")

    if secim == '1':
        ad = input("Adınız: ")
        bakiye = float(input("Başlangıç bakiyeniz: "))
        banka.hesap_ac(ad, bakiye)
    elif secim == '2':
        hesap_no = int(input("Hesap numaranız: "))
        musteri = banka.giris_yap(hesap_no)
        if musteri:
            while True:
                print("\n1. Para Yatır\n2. Para Çek\n3. Bakiye Sorgula\n4. Çıkış")
                islem = input("İşleminiz: ")
                if islem == '1':
                    miktar = float(input("Yatırmak istediğiniz miktar: "))
                    musteri.para_yatir(miktar)
                elif islem == '2':
                    miktar = float(input("Çekmek istediğiniz miktar: "))
                    musteri.para_cek(miktar)
                elif islem == '3':
                    musteri.bakiye_sorgula()
                elif islem == '4':
                    break
                else:
                    print("Geçersiz işlem.")
    elif secim == '3':
        break
    else:
        print("Geçersiz seçim.")

