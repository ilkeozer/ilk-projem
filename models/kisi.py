class Kisi:
    def __init__(self, ad, email):
        self.__ad = ad
        self.__email = email

    def ad(self):
        return self.__ad

    def email(self):
        return self.__email

    def ad_guncelle(self, yeni_ad):
        self.__ad = yeni_ad

    def email_guncelle(self, yeni_email):
        self.__email = yeni_email

    def bilgileri_goster(self):
        return f"Ad: {self.__ad}, Email: {self.__email}"
