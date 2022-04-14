# Kullanıcıdan alınan sayının faktöriyelini hesaplama
sayi = int(input("Faktöryel hesaplanacak sayı : "))
faktöryel = 0

if sayi < 0:
    print("Negatif sayı yazamazsınız!")
elif sayi == 0:
    print("0 Rakamının Faktöryeli : 1")
else:
    for i in range(1, sayi+1):
        faktöryel += sayi*i
    #print(str(sayi)+" Rakamının faktöryeli : "+str(faktöryel))
    print(sayi, " Rakamının faktöryeli : ", faktöryel)
