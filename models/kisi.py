from utils.dogrulama import bos_mu, email_kontrol


class Kisi:
    def __init__(self, ad, email):
        if bos_mu(ad):
            raise ValueError("Ad boş olamaz!")

        if not email_kontrol(email):
            raise ValueError("Geçersiz email adresi!")

        self.__ad = ad
        self.__email = email

    def ad(self):
        return self.__ad

    def email(self):
        return self.__email

    def ad_guncelle(self, yeni_ad):
        if bos_mu(yeni_ad):
            raise ValueError("Ad boş olamaz!")

        self.__ad = yeni_ad

    def email_guncelle(self, yeni_email):
        if not email_kontrol(yeni_email):
            raise ValueError("Geçersiz email adresi!")

        self.__email = yeni_email

    def bilgileri_goster(self):
        return f"Ad: {self.__ad}, Email: {self.__email}"
