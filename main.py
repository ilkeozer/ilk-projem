from models.odeme import Odeme
odeme1 = Odeme("Kredi Kartı", 13500)

print(odeme1.bilgileri_goster())

odeme1.odeme_tamamla()

print("Yeni Ödeme Durumu:", odeme1.durum())
