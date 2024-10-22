total_elemen = int(input("Masukkan jumlah elemen dalam array: "))

isi_array = list(range(1, total_elemen + 1))

print("Array yang dihasilkan:", isi_array)

bilangan_bulat = int(input("Masukkan bilangan bulat untuk mencari kelipatan: "))

kelipatan = [num for num in isi_array if num % bilangan_bulat == 0]

if kelipatan:
     print(f"Bilangan yang merupakan kelipatan dari {bilangan_bulat}:", kelipatan)
else:
    print(f"Tidak ada bilangan dalam array yang merupakan kelipatan dari {bilangan_bulat}.")