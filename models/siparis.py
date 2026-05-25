class Siparis:
    def __init__(self, musteri):

        self.__musteri = musteri
        self.__urunler = []

    def urun_ekle(self, urun):

        self.__urunler.append(urun)

    def toplam_tutar(self):

        toplam = 0

        for urun in self.__urunler:
            toplam += urun.fiyat()

        return toplam

    def siparis_bilgisi(self):

        urun_listesi = ""

        for urun in self.__urunler:
            urun_listesi += f"- {urun.urun_adi()} : {urun.fiyat()} TL\n"

        return f"""
Müşteri: {self.__musteri.ad()}

Ürünler:
{urun_listesi}

Toplam Tutar: {self.toplam_tutar()} TL
"""
