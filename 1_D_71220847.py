print("========== MAKANAN ==========")
print("1. Telur Bakar : Rp 7.000")
print("2. Lele Terbang Mas Bhe : Rp 10.000")
print("3. Es Coklat Lempu : Rp 5.000")
print("4. Es Doger Langensari : Rp 13.000")

hargaTelorBakarMasBro = int(7000)
hargaLeleSelokan = int(10000)
hargaCoklatCoklatToilet = int(5000)
hargaDogerKau = int(13000)

print("========== PESANAN ==========")
telorrr = int(input("Telur Bakar : "))
lelll = int(input("Lele Terbang : "))
cokkk = int(input("Es Coklat : "))
doggg = int(input("Es Doger : "))

hargatelorrr = hargaTelorBakarMasBro*telorrr
hargalelll = hargaLeleSelokan*lelll
hargacokkk = hargaCoklatCoklatToilet*cokkk
hargadoggg = hargaDogerKau*doggg
totalDuitHilang = hargatelorrr+hargalelll+hargacokkk+hargadoggg

print("========== TOTAL ==========")
print(f"TOTAL TELUR BAKAR X {telorrr} : RP {hargatelorrr}")
print(f"TOTAL LELE TERBANG X {lelll} : RP {hargalelll}")
print(f"TOTAL ES COKLAT X {cokkk} : RP {hargacokkk}")
print(f"TOTAL ES DOGER X {doggg} : RP {hargadoggg}")
print(f"Jumlah total biaya yang harus dibayar adalah Rp {totalDuitHilang}")