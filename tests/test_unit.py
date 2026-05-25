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
