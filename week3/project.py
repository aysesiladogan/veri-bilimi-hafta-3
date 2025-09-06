import random
import statistics

kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda x: x["satis"])

def yazar_satislari(kitaplar):
    sonuc = {}
    for k in kitaplar:
        sonuc[k["yazar"]] = sonuc.get(k["yazar"], 0) + k["satis"]
    return sonuc

turler = {k["tur"] for k in kitaplar}
bin_ustu = [k["isim"] for k in kitaplar if k["satis"] > 1000]

sonra_2020 = list(filter(lambda x: x["yil"] > 2020, kitaplar))
yuzde_artis = list(map(lambda x: {**x, "satis": int(x["satis"] * 1.1)}, kitaplar))
sirali = sorted(kitaplar, key=lambda x: x["satis"], reverse=True)

ortalama_satis = statistics.mean([k["satis"] for k in kitaplar])
standart_sapma = statistics.stdev([k["satis"] for k in kitaplar])

tur_satis = {}
for k in kitaplar:
    tur_satis[k["tur"]] = tur_satis.get(k["tur"], 0) + k["satis"]
en_cok_satan_tur = max(tur_satis, key=tur_satis.get)

random.shuffle(kitaplar)
train_size = int(0.7 * len(kitaplar))
train, test = kitaplar[:train_size], kitaplar[train_size:]

train_yazar_satis = yazar_satislari(train)
train_ortalama = statistics.mean([k["satis"] for k in train])

test_ustunde = [k["isim"] for k in test if k["satis"] > train_ortalama]

print("En çok satan kitap:", en_cok_satan(kitaplar)["isim"])
print("Yazar satışları:", yazar_satislari(kitaplar))
print("Türler:", turler)
print("1000’den fazla satan kitaplar:", bin_ustu)
print("Ortalama satış:", round(ortalama_satis, 2))
print("Standart sapma:", round(standart_sapma, 2))
print("En çok satan tür:", en_cok_satan_tur)
print("\nEğitim/Test Analizi:")
print("Eğitim ortalama satış:", round(train_ortalama, 2))
print("Testte ortalama üstü kitaplar:", test_ustunde)
