from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis
from models.kargo import Kargo


def test_tam_siparis_sistemi():

    musteri = Musteri("İlke", "ilke@gmail.com", 1001)

    urun1 = Urun("Telefon", 12000, 2)
    urun2 = Urun("Kulaklık", 1500, 5)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun1)
    siparis.urun_ekle(urun2)

    kargo = Kargo()

    kargo.durum_guncelle("Kargoda")

    assert siparis.toplam_tutar() == 13500
    assert kargo.durum() == "Kargoda"


def test_siparis_iptal_senaryosu():

    musteri = Musteri("Ayşe", "ayse@gmail.com", 1002)

    urun = Urun("Tablet", 7000, 1)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun)

    kargo = Kargo()

    kargo.durum_guncelle("İptal Edildi")

    assert kargo.durum() == "İptal Edildi"
