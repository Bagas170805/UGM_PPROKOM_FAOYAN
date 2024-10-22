matriks = []

for i in range (0,2):
    matriks.append([])
    for j in range (0,3):
        matriks[i].append(int(input(f"Masukkan nilai ke-[{i}][{j}]: ")))

for i in range (0,2):
    for j in range (0,3):
     print(matriks[i][j], end =' ')
    print()
