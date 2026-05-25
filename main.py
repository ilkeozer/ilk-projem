from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis
from models.odeme import Odeme
from services.siparis_yonetimi import SiparisYonetimi

musteri1 = Musteri("İlke", "ilke@gmail.com", 1001)

urun1 = Urun("Telefon", 12000, 2)
urun2 = Urun("Kulaklık", 1500, 5)

siparis1 = Siparis(musteri1)
siparis1.urun_ekle(urun1)
siparis1.urun_ekle(urun2)

print(siparis1.siparis_bilgisi())

odeme1 = Odeme("Kredi Kartı", siparis1.toplam_tutar())

print("Ödeme oluşturuldu.")
print("Ödeme Durumu:", odeme1.durum())

odeme1.odeme_tamamla()

print("Ödeme işlemi tamamlandı.")
print("Güncel Ödeme Durumu:", odeme1.durum())
