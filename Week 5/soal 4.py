jumlah_data = int(input("masukkan banyak data yang akan diolah :"))
print()
data=[]
for i in range(0, jumlah_data):
    masukkan=int(input(f"masukkan data ke-{i+1}:"))
    data.append(masukkan)
rata_rata= sum(data) / jumlah_data
print(f"rata-rata = {rata_rata}")