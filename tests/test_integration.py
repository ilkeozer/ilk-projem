from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis


def test_siparis_toplam_hesaplama():

    musteri = Musteri("İlke", "ilke@gmail.com", 1001)

    urun1 = Urun("Kulaklık", 1500, 5)
    urun2 = Urun("Mouse", 500, 3)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun1)
    siparis.urun_ekle(urun2)

    assert siparis.toplam_tutar() == 2000


def test_siparis_urun_ekleme():

    musteri = Musteri("Ayşe", "ayse@gmail.com", 1002)

    urun = Urun("Tablet", 7000, 2)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun)

    assert siparis.toplam_tutar() == 7000


def test_birden_fazla_urun():

    musteri = Musteri("Mehmet", "mehmet@gmail.com", 2001)

    urun1 = Urun("Telefon", 10000, 1)
    urun2 = Urun("Şarj Aleti", 750, 4)
    urun3 = Urun("Kulaklık", 1200, 2)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun1)
    siparis.urun_ekle(urun2)
    siparis.urun_ekle(urun3)

    assert siparis.toplam_tutar() == 11950
