nilai=set({3,6,9,2,5,7})
print("nilai = set","(",nilai,")")
#menambahkan anggota dengan update
nilai.update([1,4,8,10])
print("nilai = set","(",nilai,")")

nilai.difference_update([1,3,4,5,7,8,10])
print("nilai = set","(", nilai,")")