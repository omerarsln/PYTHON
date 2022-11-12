zincir1 = ["A", "T", "G", "A", "T", "G", "A", "T", "G", "C"]
zincir2 = ["T", "C", "G", "C", "G", "C", "T", "A", "G", "C"]
zincir3 = ["C", "G", "T", "C", "G", "T", "A", "A", "A", "C"]
zincir4 = ["T", "A", "T", "T", "T", "A", "C", "G", "A", "A"]
zincir5 = ["T", "A", "C", "T", "A", "C", "T", "A", "C", "G"]

tumZincirler = [zincir1, zincir2, zincir3, zincir4, zincir5]
uyumlular = []

i = 0
while i < 5:
    j = i + 1
    while j < 5:
        t = 0
        while t < 10:
            if(tumZincirler[i][t] == "A"):
                if(tumZincirler[j][t] != "T"):
                    break
            elif(tumZincirler[i][t] == "T"):
                if(tumZincirler[j][t] != "A"):
                    break
            elif(tumZincirler[i][t] == "G"):
                if(tumZincirler[j][t] != "C"):
                    break
            else:
                if(tumZincirler[j][t] != "G"):
                    break
            t += 1
            if(t == 10):
                uyumlular.append([i + 1, j + 1])
        j += 1
    i += 1

for eleman in uyumlular:
    print(eleman)
