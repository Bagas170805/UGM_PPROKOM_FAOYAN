# Program untuk menampilkan siswa yang lulus dan tidak lulus
Nama = input("Nama Siswa = ")
Nilai = int(input("Nilai Siswa = "))
Lulus = "Selamat anda lulus "
Gagal = "Maaf anda tidak lulus :"
# mengecek menggunakan fungsi if apakah nilai yang diinputkan lebih dari atau sama dengan 70
if(Nilai >= 70):
    print (Lulus)
# mengecek apabila nilai kurang dari 70
else :
    print (Gagal)