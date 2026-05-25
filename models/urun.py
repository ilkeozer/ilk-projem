class Urun:
    def __init__(self, urun_adi, fiyat, stok):

        if fiyat < 0:
            raise ValueError("Fiyat negatif olamaz!")

        if stok < 0:
            raise ValueError("Stok negatif olamaz!")

        self.__urun_adi = urun_adi
        self.__fiyat = fiyat
        self.__stok = stok

    def urun_adi(self):
        return self.__urun_adi

    def fiyat(self):
        return self.__fiyat

    def stok(self):
        return self.__stok

    def stok_guncelle(self, yeni_stok):

        if yeni_stok < 0:
            raise ValueError("Stok negatif olamaz!")

        self.__stok = yeni_stok

    def bilgileri_goster(self):
        return f"""
Ürün Adı: {self.__urun_adi}
Fiyat: {self.__fiyat} TL
Stok: {self.__stok}
"""
