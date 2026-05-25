class Odeme:
    def __init__(self, odeme_turu, tutar):

        if tutar <= 0:
            raise ValueError("Ödeme tutarı sıfır veya negatif olamaz!")

        self.__odeme_turu = odeme_turu
        self.__tutar = tutar
        self.__durum = "Bekliyor"

    def odeme_turu(self):
        return self.__odeme_turu

    def tutar(self):
        return self.__tutar

    def durum(self):
        return self.__durum

    def odeme_tamamla(self):
        self.__durum = "Ödendi"

    def bilgileri_goster(self):
        return f"""
Ödeme Türü: {self.__odeme_turu}
Tutar: {self.__tutar} TL
Durum: {self.__durum}
"""
