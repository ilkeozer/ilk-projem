class SiparisYonetimi:
    def __init__(self):

        self.__siparisler = []

    def siparis_ekle(self, siparis):

        self.__siparisler.append(siparis)

    def siparisleri_listele(self):

        return self.__siparisler

    def toplam_ciro(self):

        toplam = 0

        for siparis in self.__siparisler:
            toplam += siparis.toplam_tutar()

        return toplam
