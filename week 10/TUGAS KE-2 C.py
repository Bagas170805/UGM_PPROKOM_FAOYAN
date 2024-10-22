# Mendefinisikan dua array multidimensi
array1 = [[4, 6],
           [1, 7]]

array2 = [[2, 3],
           [5, 6]]

# Inisialisasi array hasil untuk penjumlahan dan pengurangan
hasil_penjumlahan = []
hasil_pengurangan = []

# Menghitung penjumlahan dan pengurangan
for i in range(len(array1)):
    baris_penjumlahan = []
    baris_pengurangan = []
    for j in range(len(array1[i])):
        # Menghitung penjumlahan
        baris_penjumlahan.append(array1[i][j] + array2[i][j])
        # Menghitung pengurangan
        baris_pengurangan.append(array1[i][j] - array2[i][j])
    hasil_penjumlahan.append(baris_penjumlahan)
    hasil_pengurangan.append(baris_pengurangan)

# Menampilkan hasil
print("Hasil Penjumlahan:")
print(hasil_penjumlahan)

print("Hasil Pengurangan:")
print(hasil_pengurangan)