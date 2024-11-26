#Mencetak Menu
def menu():
    print ("Pilih Bentuk 2D")
    print ("1. Persegi Panjang")
    print ("2. Lingkaran")
    print ("3. Segitiga")
    print ("4. Keluar")
    
    pilih_menu = int(input("Pilih menu diatas : "))
    if pilih_menu == 1:
        persegi()
    elif pilih_menu == 2:
        lingkaran()
    elif pilih_menu == 3:
        segitiga()
    elif pilih_menu == 4:
        exit()
    else:
        print("Pilihan anda tidak valid")
        menu()

def persegi():
        print ("Menghitung Luas Persegi Panjang")
        p = int(input("Masukkan Panjang : "))
        l = int(input("Masukkan Lebar : "))
        luas = p*l
        print ("Luas Persegi Panjang adalah ",luas)
        print() 
        print ("Coba lagi [Y/N]? ")
        back = input().upper()
        if back == "Y":
            menu()
        else:
            exit()


def lingkaran():
        print("Menghitung Luas Lingkaran")
        r = int(input("Masukkan Jari-Jari : "))
        luas = 3.14*(r**2)
        print ("Luas Lingkaran adalah ",luas)
        print ("Coba lagi [Y/N]? ")
        back = input().upper()
        if back == "Y":
            menu()
        else:
             exit()


def segitiga():
    print ("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas : "))
    t = int(input("Masukkan Tinggi : "))
    luas = (a*t)/2
    print ("Luas Segitiga adalah ",luas)
    print ()
    print ("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

menu()
