from models.kisi import Kisi
from models.musteri import Musteri

kisi1 = Kisi("İlke", "ilke@gmail.com")

print(kisi1.ad())
print(kisi1.email())

print("------------------")

musteri1 = Musteri("Ahmet", "ahmet@gmail.com", 1001)

print(musteri1.bilgileri_goster())
