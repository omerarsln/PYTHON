from random import randint

x = randint(0, 4)
y = randint(0, 4)
can = 16
matris = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

tahmin_x = ""
tahmin_y = ""
isim = input("İsim: ")
print(f"Mayın Tarlası Oyununa Hoşgeldin {isim}")

while can > 0:
    for i in list(range(0, 4)):
        for j in list(range(0, 4)):
            if matris[i][j] == 1:
                print("x", end=" ")
            else:
                print("-", end=" ")

        print()

    tahmin_x = input("Satırı Tahmin Et: ")
    tahmin_y = input("Sütunu Tahmin Et: ")
    if int(tahmin_x) - 1 == x and int(tahmin_y) - 1 == y:
        print("Bombayı Buldun Oyun Bitti!")
        break
    else:
        matris[int(tahmin_x) - 1][int(tahmin_y) - 1] = 1

    can = can - 1

if can == 0:
    print("Kazandın!")
else:
    print("Kaybettin!")
