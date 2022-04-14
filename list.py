# Diziler

urunler = ["laptop", "mause", "keyboard"]
print(urunler)
print(type(urunler))
urunler.append("Telefon")
print(urunler)

ogrenciler1 = ["faruk", "mahmut", "kerem"]
ogrenciler2 = ["faruk2", "mahmut2", "kerem2"]
ogrenciler1 = ogrenciler2
ogrenciler2[0] = "hamza"

print(ogrenciler1)
print(ogrenciler2)


sayi1 = 10
sayi2 = 20
sayi1 = sayi2
sayi2 = 60
print(sayi1)
print(sayi2)
