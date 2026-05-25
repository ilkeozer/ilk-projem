class Kargo:
    def __init__(self):

        self.__durum = "Hazırlanıyor"

    def durum(self):
        return self.__durum

    def durum_guncelle(self, yeni_durum):

        gecerli_durumlar = [
            "Hazırlanıyor",
            "Kargoda",
            "Teslim Edildi",
            "İptal Edildi"
        ]

        if yeni_durum not in gecerli_durumlar:
            raise ValueError("Geçersiz kargo durumu!")

        self.__durum = yeni_durum
