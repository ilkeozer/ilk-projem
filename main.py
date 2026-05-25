from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis
from models.odeme import Odeme
from services.siparis_yonetimi import SiparisYonetimi
from database.veri_tabani import VeriTabani


try:
    musteri1 = Musteri("İlke", "ilke@gmail.com", 1001)

    urun1 = Urun("Telefon", 77000, 2)
    urun2 = Urun("Kulaklık", 2000, 5)

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

    yonetim = SiparisYonetimi()
    yonetim.siparis_ekle(siparis1)

    print("Toplam Ciro:", yonetim.toplam_ciro(), "TL")

    veri_tabani = VeriTabani()
    veri_tabani.siparis_kaydet(siparis1)

    print("Veritabanındaki Sipariş Sayısı:", veri_tabani.siparis_sayisi())

except ValueError as hata:
    print("Değer hatası:", hata)

except TypeError as hata:
    print("Tip hatası:", hata)

except Exception as hata:
    print("Beklenmeyen hata:", hata)

finally:
    print("Program tamamlandı.")
