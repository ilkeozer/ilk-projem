from models.kargo import Kargo

kargo1 = Kargo()

print("Kargo Durumu:", kargo1.durum())

kargo1.durum_guncelle("Kargoda")

print("Yeni Durum:", kargo1.durum())
