N = int(input("masukkan input"))
A = 60*60*24
Hari = N//A
B = A*Hari
C = N-B
Jam = C//(60*60)
D = Jam *(60*60)
E = C-D
Menit = E // 60
Detik = N%60
print ("%d Hari %d Jam %d Menit %d Detik"%(Hari,Jam,Menit,Detik))