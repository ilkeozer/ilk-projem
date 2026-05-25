from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis

musteri1 = Musteri("İlke", "ilke@gmail.com", 1001)

urun1 = Urun("Kulaklık", 1500, 10)
urun2 = Urun("Mouse", 800, 5)

siparis1 = Siparis(musteri1)

siparis1.urun_ekle(urun1)
siparis1.urun_ekle(urun2)

print(siparis1.siparis_bilgisi())
