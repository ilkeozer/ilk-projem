from models.urun import Urun


class Siparis:
    def __init__(self, musteri):
        self.__musteri = musteri
        self.__urunler = []

    def urun_ekle(self, urun):
        if not isinstance(urun, Urun):
            raise TypeError("Siparişe sadece Urun nesnesi eklenebilir.")

        self.__urunler.append(urun)

    def urunleri_listele(self):
        return self.__urunler

    def toplam_tutar(self):
        return sum(urun.fiyat() for urun in self.__urunler)

    def siparis_bilgisi(self):
        if not self.__urunler:
            return f"{self.__musteri.ad()} isimli müşterinin siparişi boştur."

        urun_listesi = ""

        for urun in self.__urunler:
            urun_listesi += f"- {urun.urun_adi()} : {urun.fiyat()} TL\n"

        return f"""
Müşteri: {self.__musteri.ad()}

Ürünler:
{urun_listesi}
Toplam Tutar: {self.toplam_tutar()} TL
"""
