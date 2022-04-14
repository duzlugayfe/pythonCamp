# Sqlite Veritabanı İşlemleri
import sqlite3


def listele():
    baglanti = sqlite3.connect("chinook/chinook.db")
    cursor = baglanti.execute("select * from customers")

    for satir in cursor:
        print(satir[1], satir[2])

    baglanti.close()


listele()
