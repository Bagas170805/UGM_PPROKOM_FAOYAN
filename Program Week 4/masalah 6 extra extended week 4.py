# program Rock Paper Scissor
print("Main Batu Gunting Kertas Yuk !!!")

player1 = input("Hey player 1. kamu pilih Batu Gunting atau Kertas? isi disini = ")
player2 = input("Halo player 2. Sekarang giliranmu memilih nih. pilih Batu Gunting atau Kertas ? isi disini = ")
# supaya mudah menggunakan dan tidak ketergantungan bentuk huruf kapital, maka dibuat lower
player1 = player1.lower()
player2 = player2.lower()
seri = "Wah kamu seri nih!"
play1win = "player 1 kamu hebat, kamu memenangkan game ini"
play2win = "player 2 kamu hebat, kamu memenangkan game ini"
Anomali = "sepertinya kamu salah penulisan nih"

#membuat program batu gunting kertas
if player1 == "batu":
    if player2 == "batu":
        print(seri)
    elif player2 == "kertas":
        print (play2win)
    elif player2 == "gunting":
        print(play1win)
elif player1 == "gunting":
    if player2 == "gunting":
        print(seri)
    elif player2 =="batu":
        print(play2win)
    elif player2 == "kertas":
        print(play1win)
elif player1 == "kertas":
    if player2 == "kertas":
        print(seri)
    elif player2 == "batu":
        print(play1win)
    elif player2 == "gunting":
        print(play2win)
else :
    print(Anomali) 