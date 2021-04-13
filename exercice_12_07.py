#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Kártyahúzáa

from random import randrange

class KartyaJatek:
    """Kártyajáték"""
    # osztályattribútumok (minden példány esetében közösek) :
    couleur = ('Pique', 'Trefle', 'Carreau', 'Coeur')
    ertek = (0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'junga', 'dama', 'kiraly', 'asz')

    def __init__(self):
        "Az 52 kártya listájának létrehozása"
        self.kartya =[]
        for coul in range(4):
            for val in range(13):
                self.kartya.append((val +2, coul))   # az érték 2-vel kezdõdik

    def kartya_neve(self, c):
        "A c kártya értékét adja meg, en clair"
        return "%s %s" % (self.couleur[c[1]], self.ertek[c[0]])
        
    def kever(self):
        "Megkeveri a kártyákat"
        t = len(self.kartya)             # a maradék kártyák száma
        # a keveréshez azonos számú cserét végzünk :
        for i in range(t):
            # 2 listabeli hely véletlenszerû sorsolása :
            h1, h2 = randrange(t), randrange(t)
            # felcseréljük az ezeken a helyeken lévõ kártyákat :
            self.kartya[h1], self.kartya[h2] = self.kartya[h2], self.kartya[h1]
        
    def huz(self):
        "A pakli elsõ kártyájának kihúzása"
        t = len(self.kartya)             # ellenõrizzük, hogy maradt-e kártya
        if t >0:                        
            kartya = self.kartya[0]       # kiválasztjuk az elsõ kártyát
            del(self.kartya[0])          # kivonjuk a játékból
            return kartya                # megadjuk a másolatát a hívó programnak
        else:
            return None                 # fakultativ

### Tesztprogramme  :

if __name__ == '__main__':
    jatek = KartyaJatek()                 # objektum létrehozása
    jatek.kever()                        # kártyák keverése
    for n in range(53):                 # 52 kártya húzása : 
        c = jatek.huz()
        if c == None:                   # egyetlen kártya sem marad
            print 'Vege !'           # a listában
        else:
            print jatek.kartya_neve(c)      # a kártya értéke és színe
