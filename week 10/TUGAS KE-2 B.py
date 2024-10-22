daftar = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]


elemen_genap= []
elemen_ganjil = []

for row in daftar:
    for elemen in row:
     if elemen % 2 == 0:
        elemen_genap.append(elemen)
     else :
        elemen_ganjil.append(elemen)

print("jumlah angka genap yang ada pada data: ",len(elemen_genap))
print("jumlah angka ganjil yang ada pada data: ", len(elemen_ganjil))