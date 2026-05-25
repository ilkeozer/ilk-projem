import pytest
from models.urun import Urun
from models.musteri import Musteri


def test_urun_adi():

    urun = Urun("Kulaklık", 1500, 10)

    assert urun.urun_adi() == "Kulaklık"


def test_urun_fiyati():

    urun = Urun("Mouse", 800, 5)

    assert urun.fiyat() == 800


def test_musteri_adi():

    musteri = Musteri("İlke", "ilke@gmail.com", 1001)

    assert musteri.ad() == "İlke"


def test_stok_bilgisi():

    urun = Urun("Klavye", 1200, 7)

    assert urun.stok() == 7


def test_stok_guncelleme():

    urun = Urun("Tablet", 5000, 3)

    urun.stok_guncelle(10)

    assert urun.stok() == 10


def test_negatif_fiyat():

    with pytest.raises(ValueError):

        Urun("Telefon", -1000, 5)


def test_negatif_stok():

    with pytest.raises(ValueError):

        Urun("Telefon", 1000, -5)


def test_email_bilgisi():

    musteri = Musteri("Ayşe", "ayse@gmail.com", 1002)

    assert musteri.email() == "ayse@gmail.com"


def test_musteri_numarasi():

    musteri = Musteri("Mehmet", "mehmet@gmail.com", 2001)

    assert musteri.musteri_no() == 2001


def test_ad_guncelleme():

    kisi = Musteri("Ali", "ali@gmail.com", 3001)

    kisi.ad_guncelle("Veli")

    assert kisi.ad() == "Veli"
