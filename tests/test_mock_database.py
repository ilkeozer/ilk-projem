from models.musteri import Musteri
from models.urun import Urun
from models.siparis import Siparis


class MockVeriTabani:
    def __init__(self):
        self.siparisler = []

    def siparis_kaydet(self, siparis):
        self.siparisler.append(siparis)

    def siparis_sayisi(self):
        return len(self.siparisler)


def test_mock_veri_tabani():

    musteri = Musteri("İlke", "ilke@gmail.com", 1001)

    urun = Urun("Telefon", 12000, 2)

    siparis = Siparis(musteri)

    siparis.urun_ekle(urun)

    mock_db = MockVeriTabani()

    mock_db.siparis_kaydet(siparis)

    assert mock_db.siparis_sayisi() == 1
