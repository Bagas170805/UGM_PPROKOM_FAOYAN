angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
print(angka)
angka_genap = []
angka_ganjil = []
for num in angka:
    if num %2 == 0:
        angka_genap.append(num)
        
    else:
        angka_ganjil.append(num)
        
print("angka genap dari data yang ada: ",angka_genap)
print("jumlah angka genap yang ada pada data: ",len(angka_genap))
print("angka ganjil dari data yang ada: ",angka_ganjil)
print("jumlah angka ganjil yang ada pada data: ", len(angka_ganjil))