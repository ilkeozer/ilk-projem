class VeriTabani:
    def __init__(self):
        self.__siparisler = []

    def siparis_kaydet(self, siparis):
        if siparis is None:
            raise ValueError("Kaydedilecek sipariş boş olamaz!")

        self.__siparisler.append(siparis)
        return True

    def tum_siparisleri_getir(self):
        return self.__siparisler

    def siparis_sayisi(self):
        return len(self.__siparisler)
