#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Leszármaztatott osztályok - polimorfizmus

class Kor:
    def __init__(self, sugar):
        self.sugar = sugar

    def terulet(self):
        return 3.1416 * self.sugar**2
        
class Henger(Kor):
    def __init__(self, sugar, magassag):
        Kor.__init__(self, sugar)
        self.magassag = magassag
        
    def terfogat(self):
        return self.terulet()*self.magassag
        
        # a terulet() metódust a szülőosztálytól örökli
        
class Kup(Henger):
    def __init__(self, sugar, magassag):
        Henger.__init__(self, sugar, magassag)
                
    def terfogat(self):
        return Henger.terfogat(self)/3
        
        # ez az új terfogat() metódus helyettesíti a
        # zülőosztálytól örökölt metódust (polimorfizmus példa)

#  Tesztprogram :

henger = Henger(5, 7)
print "Henger alapterülete =", henger.terulet()
print "Hengertérfogat =", henger.terfogat()

kup = Kup(5,7)
print "Kúp alapterülete =", kup.terulet()
print "Kúptéfogat =", kup.terfogat()
