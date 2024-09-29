# login dengan memasukan nama dan nim
nama = input("Masukan Nama: ")
nim = input("Masukan NIM: ")
kelas = input("Masukan kelas: ")
print("---------------------------------------")
print("Hai " + str(nama))
print("Dengan NIM " + str(nim))
print("Kelas ")
print("---------------------------------------")    
print()
# menghitung harga barang dan perulangannya
ulang = "y" 
while(ulang == "y"):
# Menghitung total harga barang
        print("============menghitung harga barang============")
        harga_barang = float(input("Harga barang: Rp. "))
        jumlah_barang = int(input("Jumlah barang: "))

# Harga sebelum diskon
        Harga = harga_barang * jumlah_barang

# Harga setelah diskon
        if Harga > 250.000:
            persen_diskon = Harga * 0.25
            Diskon = Harga - persen_diskon
            print("Anda mendapatkan diskon 25%. jadi harga barang anda: Rp. " + str(Diskon))
            print("=================== Selesai ===================")
        else:
            print("anda tidak mendapatkan diskon. jadi harga barang: Rp. " + str(Harga))
            print("=================== Selesai ===================")
# Perulangan
        ulang = input("lanjut menghitung atau tidak(y/t): ")
        if (ulang == "t"):
            print("terima kasih")
            break