""" 

Not Defteri (Notebook): 

Proje Tanımı: 
Bir not defteri uygulaması oluşturun. Kullanıcı not ekleyebilir, silebilir ve notlarını tarih sırasına göre listeleyebilir.

İstenilen Özellikler:
Not ekleme (not içeriği ve tarih).
Notları listeleme.
Notları silme.
Tüm notları bir .txt dosyasına kaydetme ve yeniden yükleme.

Yönerge:
Bir Not sınıfı oluşturun. Not içeriği ve tarih bilgisi tutulsun.
Bir NotDefteri sınıfı oluşturun. Not ekleme, listeleme ve silme işlemlerini yönetin.

"""


from datetime import datetime
import os

class Not:
    def __init__(self, icerik, tarih=None):
        self.icerik = icerik
        self.tarih = tarih if tarih else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"{self.tarih} - {self.icerik}"

class NotDefteri:
    def __init__(self):
        self.notlar = []

    def not_ekle(self, icerik):
        yeni_not = Not(icerik)
        self.notlar.append(yeni_not)
        print("Not başarıyla eklendi!")

    def notlari_listele(self):
        if not self.notlar:
            print("Not defteri boş.")
        else:
            print("Notlar:")
            for not_obj in sorted(self.notlar, key=lambda x: x.tarih):
                print(not_obj)

    def not_sil(self, index):
        try:
            silinen_not = self.notlar.pop(index)
            print(f"Silinen not: {silinen_not}")
        except IndexError:
            print("Geçersiz indeks. Lütfen doğru bir indeks girin.")

    def notlari_kaydet(self, dosya_adi):
        try:
            with open(dosya_adi, 'w', encoding='utf-8') as dosya:
                for not_obj in self.notlar:
                    dosya.write(f"{not_obj.tarih}\t{not_obj.icerik}\n")
            print(f"Notlar {dosya_adi} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Dosya kaydedilirken bir hata oluştu: {e}")

    def notlari_yukle(self, dosya_adi):
        if not os.path.exists(dosya_adi):
            print(f"{dosya_adi} bulunamadı.")
            return

        try:
            with open(dosya_adi, 'r', encoding='utf-8') as dosya:
                self.notlar.clear()
                for satir in dosya:
                    tarih, icerik = satir.strip().split('\t', 1)
                    self.notlar.append(Not(icerik, tarih))
            print(f"Notlar {dosya_adi} dosyasından yüklendi.")
        except Exception as e:
            print(f"Dosya yüklenirken bir hata oluştu: {e}")

# Örnek kullanım
if __name__ == "__main__":
    defter = NotDefteri()

    while True:
        print("\n1. Not Ekle")
        print("2. Notları Listele")
        print("3. Not Sil")
        print("4. Notları Kaydet")
        print("5. Notları Yükle")
        print("6. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            icerik = input("Not içeriğini girin: ")
            defter.not_ekle(icerik)
        elif secim == "2":
            defter.notlari_listele()
        elif secim == "3":
            try:
                indeks = int(input("Silmek istediğiniz notun indeksini girin: "))
                defter.not_sil(indeks)
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "4":
            dosya_adi = input("Dosya adını girin: ")
            defter.notlari_kaydet(dosya_adi)
        elif secim == "5":
            dosya_adi = input("Dosya adını girin: ")
            defter.notlari_yukle(dosya_adi)
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
