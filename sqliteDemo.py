# Sqlite Veritabanı İşlemleri
import sqlite3
baglanti = sqlite3.connect("chinook/chinook.db")


def listele():
    cursor = baglanti.execute("select * from customers")
    for satir in cursor:
        print(satir[1], satir[2])
    baglanti.close()


def listeleKosul():
    #"select * from customers where Country='Brazil'"
    sqlQuery = "select * from artists where ArtistId=279"
    cursor = baglanti.execute(sqlQuery)
    for satir in cursor:
        print(satir[0], satir[1])
    baglanti.close()


def update():
    sqlQuery = "UPDATE customers SET Country='Brazil' where Country='Brezilya'"
    cursor = baglanti.cursor()
    cursor.execute(sqlQuery)
    baglanti.commit()
    print("Kayıt güncellendi")
    cursor.close()


def addData():
    sqlQuery = "insert into artists(ArtistId, Name) VALUES (276,'Müslüm Gürses')"
    cursor = baglanti.cursor()
    cursor.execute(sqlQuery)
    baglanti.commit()
    print("Kayıt Eklendi")
    cursor.close()


def addDatas(id, name):
    sqlQuery = "insert into artists(ArtistId, Name) VALUES (?,?)"
    sqlQueryParametre = (id, name)
    cursor = baglanti.cursor()
    cursor.execute(sqlQuery, sqlQueryParametre)
    baglanti.commit()
    print("Kayıtlar Eklendi")
    cursor.close()


# addData()
# update()
addDatas(279, 'Selahattin Özdemir')
addDatas(280, 'Cengiz Kurtoğlu')
listeleKosul()
