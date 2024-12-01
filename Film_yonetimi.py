"""
 Film Yönetim Sistemi: 
 
Proje Tanımı: 
Bir film yönetim uygulaması oluşturun. Filmleri ekleyebilir, silebilir ve listeleyebilirsiniz.


İstenilen Özellikler:
Film ekleme (film adı, yönetmen, yıl, tür bilgisiyle).
Filmleri listeleme (türe veya yıla göre filtreleme).
Filmleri silme.

Yönerge:
Film sınıfı oluşturun. Film adı, yönetmen, yıl ve tür bilgilerini saklayın.
FilmYoneticisi sınıfı oluşturun. Film ekleme, silme ve listeleme işlemleri yapılabilsin.


"""

class Film:
    def __init__(self, ad, yonetmen, yil, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self):
        return f"{self.ad} ({self.yil}) - {self.tur}, Yönetmen: {self.yonetmen}"

class FilmYoneticisi:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, ad, yonetmen, yil, tur):
        yeni_film = Film(ad, yonetmen, yil, tur)
        self.filmler.append(yeni_film)
        print("Film başarıyla eklendi!")

    def filmleri_listele(self, filtre_tur=None, filtre_yil=None):
        filtreli_filmler = self.filmler

        if filtre_tur:
            filtreli_filmler = [film for film in filtreli_filmler if film.tur.lower() == filtre_tur.lower()]
        if filtre_yil:
            filtreli_filmler = [film for film in filtreli_filmler if film.yil == filtre_yil]

        if not filtreli_filmler:
            print("Listelenecek film bulunamadı.")
        else:
            print("Filmler:")
            for film in filtreli_filmler:
                print(film)

    def film_sil(self, index):
        try:
            silinen_film = self.filmler.pop(index)
            print(f"Silinen film: {silinen_film}")
        except IndexError:
            print("Geçersiz indeks. Lütfen doğru bir indeks girin.")

# Örnek kullanım
if __name__ == "__main__":
    yonetici = FilmYoneticisi()

    while True:
        print("\n1. Film Ekle")
        print("2. Filmleri Listele")
        print("3. Film Sil")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Film adı: ")
            yonetmen = input("Yönetmen: ")
            yil = int(input("Yıl: "))
            tur = input("Tür: ")
            yonetici.film_ekle(ad, yonetmen, yil, tur)
        elif secim == "2":
            print("Filtreleme seçenekleri:")
            filtre_tur = input("Tür (boş bırakabilirsiniz): ") or None
            try:
                filtre_yil = int(input("Yıl (boş bırakabilirsiniz): ") or 0)
                filtre_yil = filtre_yil if filtre_yil != 0 else None
            except ValueError:
                filtre_yil = None

            yonetici.filmleri_listele(filtre_tur, filtre_yil)
        elif secim == "3":
            try:
                indeks = int(input("Silmek istediğiniz filmin indeksini girin: "))
                yonetici.film_sil(indeks)
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
