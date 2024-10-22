angka_tersimpan = []
for i in range(5):
    angka_dimasukkan= float(input(f"Masukan data yang akan dioperasikan: "))
    angka_tersimpan.append(angka_dimasukkan)
    print(angka_tersimpan)


permintaan = input("Apakah anda akan menentukan jumlah atau rata-rata:  ")
permintaan = permintaan.lower()
if permintaan == "jumlah":
    print("Jumlah dari semua data yang diinputkan : ", sum(angka_tersimpan))
elif permintaan == "rata-rata":
    print("Rata-rata dari semua data yang diinputkan : ", (sum(angka_tersimpan)/5)) 

else:
    print("Permintaan tidak dapat diketahui")