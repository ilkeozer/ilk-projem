from models.kisi import Kisi


class Musteri(Kisi):
    def __init__(self, ad, email, musteri_no):
        super().__init__(ad, email)
        self.__musteri_no = musteri_no

    def musteri_no(self):
        return self.__musteri_no

    def bilgileri_goster(self):
        return f"""
Müşteri Adı: {self.ad()}
Email: {self.email()}
Müşteri No: {self.__musteri_no}
"""
