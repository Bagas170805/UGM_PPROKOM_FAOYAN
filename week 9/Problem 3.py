array = [4, 5, 11, 12, 14, 16, 16, 19]
bilangan_prima = []
for num in array:
    if num >= 2:
        is_prime = True

        for i in range (2, int(num ** 0.5) + 1):
            if num % i ==0:
                is_prime = False
                break

        
        if is_prime:
            bilangan_prima.append(num)

banyak_prima= len(bilangan_prima)
print("data pada array :",array)
print(f"Bilangan prima yang ada dalam array :{bilangan_prima} ")
print(f"banyaknya bilangan prima: {len(bilangan_prima)}")