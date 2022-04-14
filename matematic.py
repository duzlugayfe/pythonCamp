# Class & Function
class Matematik:
    def __init__(self, sayi1, sayi2):  # Constructer (yapıcı) blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik Referansı Oluştu")

    def topla(self):
        return self.s1+self.s2

    def carp(self):
        return self.s1*self.s2

    def bol(self):
        return self.s1 / self.s2

    def cıkar(self):
        return self.s1-self.s2


matematik = Matematik(6, 7)
sonuc1 = matematik.carp()
sonuc2 = matematik.topla()
print("Sonuç 1 : ", sonuc1)
print("Sonuç 2 : ", sonuc2)


class Istatistik(Matematik):  # Inheritence
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def varyansHesapla(self):
        return self.s1*self.s2


istatistik = Istatistik(5, 5)
son = istatistik.carp()

print(son)
