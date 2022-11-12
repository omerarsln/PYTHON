# 31.05.2021
# File Organization Project
# 1306160073
# Ömer Arslan

import random
import os

tahtaRenk = ["S", "", "", "", "", "B", "", "B", "", "", "",
             "S", "B", "", "", "", "S", "", "S", "", "", "", "", "B"]
tahtaSayi = [2, 0, 0, 0, 0, 5, 0, 3, 0, 0,
             0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2]
zar1 = 1
zar2 = 1
siraKimde = "S"
kirikSiyah = 0
kirikBeyaz = 0
toplananSiyah = 0
toplananBeyaz = 0

if os.path.isfile("./Table.txt") == False:
    tableFile = open("Table.txt", mode="w+")
    diceFile = open("Dice.txt", mode="w+")
    variableFile = open("Variables.txt", mode="w+")
else:
    tableFile = open("Table.txt", mode="r+")
    diceFile = open("Dice.txt", mode="r+")
    variableFile = open("Variables.txt", mode="r+")


variableList = variableFile.readlines()
listLenght = len(variableList)


def tahtaCiz():
    for x in range(0, 40):
        print("&", end="")
        tableFile.write("&")
        if(x == 39):
            print()
            tableFile.write("\n")
    for x in range(0, 12):
        if(tahtaSayi[x] == 0):
            print(" - ", end="")
            tableFile.write(" - ")
        else:
            print(str(tahtaSayi[x]) + tahtaRenk[x] + " ", end="")
            tableFile.write(str(tahtaSayi[x]) + tahtaRenk[x] + " ")
        if(x == 5):
            print("** ", end="")
            tableFile.write("** ")
    print()
    tableFile.write("\n")
    print()
    tableFile.write("\n")
    print()
    tableFile.write("\n")
    x = 23
    while x > 11:
        if(tahtaSayi[x] == 0):
            print(" - ", end="")
            tableFile.write(" - ")
        else:
            print(str(tahtaSayi[x]) + tahtaRenk[x] + " ", end="")
            tableFile.write(str(tahtaSayi[x]) + tahtaRenk[x] + " ")
        if(x == 18):
            print("** ", end="")
            tableFile.write("** ")
        x -= 1
    print()
    tableFile.write("\n")
    for x in range(0, 40):
        print("&", end="")
        tableFile.write("&")
    print()
    tableFile.write("\n")
    print("Kırık Siyah:" + str(kirikSiyah) +
          " // " + "Kırık Beyaz:" + str(kirikBeyaz))
    tableFile.write("Kirik Siyah:" + str(kirikSiyah) +
                    " // " + "Kirik Beyaz:" + str(kirikBeyaz) + "\n")
    print("Toplanan Siyah:" + str(toplananSiyah) +
          " // " + "Toplanan Beyaz:" + str(toplananBeyaz))
    tableFile.write("Toplanan Siyah:" + str(toplananSiyah) +
                    " // " + "Toplanan Beyaz:" + str(toplananBeyaz) + "\n")
    print()
    tableFile.write("\n")
    tableFile.write("\n")
    tableFile.write("\n")


def siraDevret():
    global siraKimde
    if(siraKimde == "S"):
        siraKimde = "B"
    else:
        siraKimde = "S"
    kaydet()


def kirikGir(zar):
    global siraKimde
    global kirikBeyaz
    global kirikSiyah
    if(siraKimde == "S"):
        if(tahtaSayi[zar - 1] > 1 and tahtaRenk[zar - 1] == "B"):
            print("Oraya Giremezsiniz")
            return False
        elif(tahtaSayi[zar - 1] == 1 and tahtaRenk[zar - 1] == "B"):
            kirikBeyaz += 1
            kirikSiyah -= 1
            tahtaRenk[zar - 1] = "S"
            return True
        else:
            kirikSiyah -= 1
            tahtaSayi[zar - 1] += 1
            tahtaRenk[zar - 1] = "S"
            return True
    else:
        if(tahtaSayi[24 - zar] > 1 and tahtaRenk[24 - zar] == "S"):
            print("Oraya Giremezsiniz")
            return False
        elif(tahtaSayi[24 - zar] == 1 and tahtaRenk[24 - zar] == "S"):
            kirikBeyaz -= 1
            kirikSiyah += 1
            tahtaRenk[24 - zar] = "B"
            return True
        else:
            kirikBeyaz -= 1
            tahtaSayi[24 - zar] += 1
            tahtaRenk[24 - zar] = "B"
            return True


def pulOyna(index, zar):
    global kirikBeyaz
    global kirikSiyah
    global toplananSiyah
    global toplananBeyaz
    if(siraKimde == "S"):
        if (tahtaRenk[index] == siraKimde):
            if(index + zar > 23):
                # taş topla
                if(toplanabilirMi() == False):
                    print("Taşları Toplamaya Başlayamazsın")
                    return False
                tahtaSayi[index] -= 1
                toplananSiyah += 1
                return True
            elif(tahtaRenk[index + zar] == "B" and tahtaSayi[index + zar] > 1):
                # oynanamaz
                print("O Pulu Oynayamazsınız")
                return False
            elif(tahtaRenk[index + zar] == "B" and tahtaSayi[index + zar] == 1):
                # taş kır
                tahtaSayi[index] -= 1
                tahtaRenk[index + zar] = "S"
                kirikBeyaz += 1
                return True
            else:
                tahtaSayi[index] -= 1
                if(tahtaSayi[index] == 0):
                    tahtaRenk[index] = ""
                tahtaSayi[index + zar] += 1
                tahtaRenk[index + zar] = "S"
                return True
        else:
            print("Orada Siyah Taş Yok")
            return False
    else:
        if (tahtaRenk[index] == siraKimde):
            if(index - zar < 0):
                # taş topla
                if(toplanabilirMi() == False):
                    print("Taşları Toplamaya Başlayamazsın")
                    return False
                tahtaSayi[index] -= 1
                toplananBeyaz += 1
                return True
            elif(tahtaRenk[index - zar] == "S" and tahtaSayi[index - zar] > 1):
                # oynanamaz
                print("O Pulu Oynayamazsınız")
                return False
            elif(tahtaRenk[index - zar] == "S" and tahtaSayi[index - zar] == 1):
                # taş kır
                tahtaSayi[index] -= 1
                tahtaRenk[index - zar] = "B"
                kirikSiyah += 1
                return True
            else:
                tahtaSayi[index] -= 1
                if(tahtaSayi[index] == 0):
                    tahtaRenk[index] = ""
                tahtaSayi[index - zar] += 1
                tahtaRenk[index - zar] = "B"
                return True
        else:
            print("Orada Beyaz Taş Yok")
            return False


def oynanabilirMi(zar):
    global siraKimde
    global kirikSiyah
    global kirikBeyaz
    if(siraKimde == "S"):
        if(kirikSiyah > 0):
            if(tahtaSayi[zar - 1] > 1 and tahtaRenk[zar - 1] == "B"):
                return False
            elif(tahtaSayi[zar - 1] == 1 and tahtaRenk[zar - 1] == "B"):
                return True
            else:
                return True
        else:
            i = 0
            while i < 24:
                if(tahtaRenk[i] == "S"):
                    if(i + zar > 23):
                        # taş toplayabilirsin
                        if(toplanabilirMi()):
                            return True
                        else:
                            return False
                    elif(tahtaRenk[i + zar] == "B" and tahtaSayi[i + zar] == 1):
                        # taş kırabilirsin
                        return True
                    elif(tahtaRenk[i + zar] == "S" or tahtaRenk[i + zar] == ""):
                        return True
                i += 1
    else:
        if(kirikBeyaz > 0):
            if(tahtaSayi[24 - zar] > 1 and tahtaRenk[24 - zar] == "S"):
                return False
            elif(tahtaSayi[24 - zar] == 1 and tahtaRenk[24 - zar] == "S"):
                return True
            else:
                return True
        else:
            i = 23
            while i > -1:
                if(tahtaRenk[i] == "B"):
                    if(i - zar < 0):
                        # taş topla
                        if(toplanabilirMi()):
                            return True
                        else:
                            return False
                    elif(tahtaRenk[i - zar] == "S" and tahtaSayi[i - zar] == 1):
                        # taş kır
                        return True
                    elif(tahtaRenk[i - zar] == "B" or tahtaRenk[i - zar] == ""):
                        return True
                i -= 1

    return False


def kayitsizOyun():
    global siraKimde
    while True:
        input("Siyah için zar atın")
        zar1 = random.randint(1, 6)
        print("Atılan zar : " + str(zar1))

        input("Beyaz için zar atın")
        zar2 = random.randint(1, 6)
        print("Atılan zar : " + str(zar2))
        if (zar1 != zar2):
            break

    if (zar1 > zar2):
        print("Oyuna Siyah başlayacak")
        print()
        siraKimde = "S"
    else:
        print("Oyuna Beyaz başlayacak")
        print()
        siraKimde = "B"


def kaydet():
    i = 0
    while i < 24:
        if(tahtaRenk[i] == ""):
            variableFile.write("*")
            i += 1
        else:
            variableFile.write(tahtaRenk[i])
            i += 1
        if(i == 24):
            variableFile.write("\n")
    i = 0
    while i < 24:
        variableFile.write(str(tahtaSayi[i]))
        i += 1
        if(i == 24):
            variableFile.write("\n")

    variableFile.write(siraKimde + "\n" + str(kirikSiyah) + "\n" + str(kirikBeyaz) +
                       "\n" + str(toplananSiyah) + "\n" + str(toplananBeyaz) + "\n")


def toplanabilirMi():
    if(siraKimde == "S"):
        i = 0
        while i < 18:
            if(tahtaRenk[i] == "S"):
                return False
            i += 1
    else:
        i = 23
        while i > 5:
            if(tahtaRenk[i] == "B"):
                return False
            i -= 1
    return True


def oyun():
    global tableFile
    while True:
        tahtaCiz()
        tableFile.flush()
        os.fsync(tableFile.fileno())
        temp = input(siraKimde + " için zar atın (Kaydedip Çıkmak İçin exit)")
        if(temp == "exit"):
            break
        zar1 = random.randint(1, 6)
        zar2 = random.randint(1, 6)
        diceFile.write(str(zar1) + " " + str(zar2) + "\n")
        diceFile.flush()
        os.fsync(diceFile.fileno())
        print("Gelen Zarlar : " + str(zar1) + "," + str(zar2))
        i = 4 if zar1 == zar2 else 2
        cift = True if zar1 == zar2 else False
        zar1Oynandi = False
        zar2Oynandi = False

        if(cift == True):
            y = 1
            while i > 0:
                if(oynanabilirMi(zar1)):
                    while True:
                        if(siraKimde == "S" and kirikSiyah > 0):
                            oynanacakPul = int(
                                input("Kırık Taşın Girileceği İndex Giriniz: "))
                            if(kirikGir(zar1)):
                                print(str(zar1) + " " +
                                      str(y) + ". Kez Oynandı")
                                i -= 1
                                y += 1
                                break
                        elif(siraKimde == "B" and kirikBeyaz > 0):
                            oynanacakPul = int(
                                input("Kırık Taşın Girileceği İndex Giriniz: "))
                            if(kirikGir(zar1)):
                                print(str(zar1) + " " +
                                      str(y) + ". Kez Oynandı")
                                i -= 1
                                y += 1
                                break
                        else:
                            oynanacakPul = int(
                                input("Oynanacak İndex Giriniz: "))
                            if(pulOyna(oynanacakPul, zar1)):
                                print(str(zar1) + " " +
                                      str(y) + ". Kez Oynandı")
                                i -= 1
                                y += 1
                                break
                else:
                    print(str(zar1) + "Oynanılamıyor , Sıra Devrediliyor")
                    i = 0
            siraDevret()

        else:
            if(oynanabilirMi(zar1) == False and oynanabilirMi(zar2) == False):
                print("İki zarı da oynayamıyorsunuz sira devrediliyor")
                siraDevret()
            else:
                while i > 0:
                    oynanacakZar = int(input("Oynanacak Zar giriniz: "))
                    if(oynanacakZar != zar1 and oynanacakZar != zar2):
                        print("Yanlış Giriş")
                    elif(oynanacakZar == zar1 and zar1Oynandi == True):
                        print(str(zar1) + " Zaten Oynandı")
                    elif(oynanacakZar == zar2 and zar2Oynandi == True):
                        print(str(zar2) + " Zaten Oynandı")
                    elif(oynanacakZar == zar1):
                        if(oynanabilirMi(zar1)):
                            if(siraKimde == "S" and kirikSiyah > 0):
                                if(kirikGir(zar1)):
                                    print(str(zar1) + " Oynandı")
                                    zar1Oynandi = True
                                    i -= 1
                            elif(siraKimde == "B" and kirikBeyaz > 0):
                                if(kirikGir(zar1)):
                                    print(str(zar1) + " Oynandı")
                                    zar1Oynandi = True
                                    i -= 1
                            else:
                                oynanacakPul = int(
                                    input("Oynanacak İndex Giriniz: "))
                                if(pulOyna(oynanacakPul, zar1)):
                                    print(str(zar1) + " Oynandı")
                                    zar1Oynandi = True
                                    i -= 1
                        else:
                            print(str(zar1) + "Oynanılamıyor")
                            zar1Oynandi = True
                            i -= 1
                    elif(oynanacakZar == zar2):
                        if(oynanabilirMi(zar2)):
                            if(siraKimde == "S" and kirikSiyah > 0):
                                if(kirikGir(zar2)):
                                    print(str(zar2) + " Oynandı")
                                    zar2Oynandi = True
                                    i -= 1
                            elif(siraKimde == "B" and kirikBeyaz > 0):
                                if(kirikGir(zar2)):
                                    print(str(zar2) + " Oynandı")
                                    zar2Oynandi = True
                                    i -= 1
                            else:
                                oynanacakPul = int(
                                    input("Oynanacak İndex Giriniz: "))
                                if(pulOyna(oynanacakPul, zar2)):
                                    print(str(zar2) + " Oynandı")
                                    zar2Oynandi = True
                                    i -= 1
                        else:
                            print(str(zar2) + "Oynanılamıyor")
                            zar2Oynandi = True
                            i -= 1
                siraDevret()
        if(toplananSiyah >= 15 or toplananBeyaz >= 15):
            print("Oyun Bitti")
            variableFile.write("Oyun Bitti\n")
            break


def kayitlariGetir():
    global tahtaRenk, tahtaSayi, siraKimde, kirikSiyah, kirikBeyaz, toplananSiyah, toplananBeyaz, variableList, listLenght
    toplananBeyaz = int(variableList[listLenght - 1].rstrip())
    toplananBeyaz = int(variableList[listLenght - 2].rstrip())
    kirikBeyaz = int(variableList[listLenght - 3].rstrip())
    kirikSiyah = int(variableList[listLenght - 4].rstrip())
    siraKimde = variableList[listLenght - 5].rstrip()
    tahtaSayiF = list(variableList[listLenght - 6].rstrip())
    tahtaRenkF = list(variableList[listLenght - 7].rstrip())
    i = 0
    while i < 24:
        tahtaSayi[i] = int(tahtaSayiF[i])
        i += 1
    i = 0
    while i < 24:
        if(tahtaRenkF[i] == "*"):
            tahtaRenk[i] = ""
            i += 1
        else:
            tahtaRenk[i] = tahtaRenkF[i]
            i += 1


if(listLenght == 0):
    kayitsizOyun()
    oyun()
elif(variableList[listLenght - 1] == "Oyun Bitti\n"):
    kayitsizOyun()
    oyun()
else:
    secim = input("Kayıtlı oyunu Yüklemek İster Misiniz ? (y)")
    if(secim == "y"):
        kayitlariGetir()
        oyun()
    else:
        kayitsizOyun()
        oyun()

tableFile.close()
diceFile.close()
variableFile.close()
