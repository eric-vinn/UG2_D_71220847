barangApaSaja = input("Masukkan brand apa saja yang hendak dibeli (pisahkan denga koma): ")
barangApaSaja1, barangApaSaja2, barangApaSaja3, barangApaSaja4 = barangApaSaja.split(",")


hargaBarang1 = int(input(f"Berapa harga barang {barangApaSaja1} ? : "))

def diskonBarang1():
    if hargaBarang1 >= 25000000:
        hargaBarang1/(100*25)
    elif hargaBarang1 >= 10000000:
        hargaBarang1/(100*10)
    else:
        hargaBarang1/(100*0)

def hargadiskonBarang1():
    if hargaBarang1 >= 25000000:
        hargaBarang1/(100*75)
    elif hargaBarang1 >= 10000000:
        hargaBarang1/(100*90)
    else:
        hargaBarang1

print(f"harga {hargaBarang1} Rp. {hargadiskonBarang1()} Diskon Rp. {diskonBarang1()}")
hargaBarang2 = int(input(f"Berapa harga barang {barangApaSaja2} ? : "))
hargaBarang3 = int(input(f"Berapa harga barang {barangApaSaja3} ? : "))
hargaBarang4 = int(input(f"Berapa harga barang {barangApaSaja4} ? : "))


