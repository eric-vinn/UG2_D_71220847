barangApaSaja = input("Masukkan brand apa saja yang hendak dibeli (pisahkan denga koma): ")
barangApaSaja1, barangApaSaja2, barangApaSaja3, barangApaSaja4 = barangApaSaja.split(",")


hargaBarang1 = int(input(f"Berapa harga barang {barangApaSaja1} ? : "))

def diskonBarang1():
    if hargaBarang1 >= 25000000:
        return hargaBarang1/(100*25)
    elif hargaBarang1 >= 10000000:
        return hargaBarang1/(100*10)
    else:
        return hargaBarang1/(100*0)

def hargadiskonBarang1():
    if hargaBarang1 >= 25000000:
        return hargaBarang1/(100*75)
    elif hargaBarang1 >= 10000000:
        return hargaBarang1/(100*90)
    else:
        return hargaBarang1

print(f"harga {hargaBarang1} Rp. {hargaBarang1} Diskon Rp. {diskonBarang1()}")


hargaBarang2 = int(input(f"Berapa harga barang {barangApaSaja2} ? : "))

def diskonBarang2():
    if hargaBarang2 >= 25000000:
        return hargaBarang2/(100*25)
    elif hargaBarang2 >= 10000000:
        return hargaBarang2/(100*10)
    else:
        return hargaBarang2/(100*0)

def hargadiskonBarang2():
    if hargaBarang2 >= 25000000:
        return hargaBarang2/(100*75)
    elif hargaBarang2 >= 10000000:
        return hargaBarang2/(100*90)
    else:
        return hargaBarang2

print(f"harga {hargaBarang2} Rp. {hargaBarang2} Diskon Rp. {diskonBarang2()}")

hargaBarang3 = int(input(f"Berapa harga barang {barangApaSaja3} ? : "))

def diskonBarang3():
    if hargaBarang3 >= 25000000:
        return hargaBarang3/(100*25)
    elif hargaBarang3 >= 10000000:
        return hargaBarang3/(100*10)
    else:
        return hargaBarang3/(100*0)

def hargadiskonBarang3():
    if hargaBarang3 >= 25000000:
        return hargaBarang3/(100*75)
    elif hargaBarang3 >= 10000000:
        return hargaBarang3/(100*90)
    else:
        return hargaBarang3

print(f"harga {hargaBarang3} Rp. {hargaBarang3} Diskon Rp. {diskonBarang3()}")


hargaBarang4 = int(input(f"Berapa harga barang {barangApaSaja4} ? : "))

def diskonBarang4():
    if hargaBarang4 >= 25000000:
        return hargaBarang4/(100*25)
    elif hargaBarang4 >= 10000000:
        return hargaBarang4/(100*10)
    else:
        return hargaBarang4/(100*0)

def hargadiskonBarang4():
    if hargaBarang4 >= 25000000:
        return hargaBarang4/(100*75)
    elif hargaBarang4 >= 10000000:
        return hargaBarang4/(100*90)
    else:
        return hargaBarang4

print(f"harga {hargaBarang4} Rp. {hargaBarang4} Diskon Rp. {diskonBarang4()}")

diskonBarang = diskonBarang1+diskonBarang2+diskonBarang3+diskonBarang4
hargadiskonBarang = hargadiskonBarang1+hargadiskonBarang2+hargadiskonBarang3+hargadiskonBarang4
print("Total diskon yang and dapatkan adalah sebesar: Rp. ", diskonBarang)
print("Total uang yang harus anda bayarkan adalah : Rp. ", hargadiskonBarang)