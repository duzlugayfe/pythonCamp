# Şart Blokları
istenenKredi = 100000
hesap = 9505
minimumOlmasiGerekenHesap = 10000

if hesap >= minimumOlmasiGerekenHesap:
    print("Kredi verilebilir")
    print("Ödemeler hesaplandı")
elif hesap >= 9000 and hesap <= 9500:
    print("Müdüre sorulacak")
elif hesap >= 9501 and hesap <= 9999:
    print("Şefe sorulacak")
else:
    print("Kredi için bakkiye yetersiz")
print("İşlem Sonu")
