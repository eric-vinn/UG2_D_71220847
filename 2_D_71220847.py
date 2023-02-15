telll = input("Masukkan Nomor Telepon : ")
depanBro = telll[:4]
belakangBro = telll[-1]
if depanBro == "0816":
    print("Anda menggunakan operator Indosat")
elif depanBro == "0814":
    print("Anda menggunakan operator Telkomsel")
else:
    print("Operator anda tidak diketahui")


if belakangBro == "0":
    print ("genap")
elif belakangBro == "2":
    print ("genap")
elif belakangBro == "4":
    print ("genap")
elif belakangBro == "6":
    print ("genap")
elif belakangBro == "8":
    print ("genap")
else:
    print ("ganjil")