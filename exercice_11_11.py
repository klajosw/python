#! /usr/bin/env python
# -*- coding: Latin-1 -*-

class Domino:
    def __init__(self, pa, pb):
        self.pa, self.pb = pa, pb
         
    def kiir_pontok(self):
        print "A oldal :", self.pa,
        print "B oldal :", self.pb
        
    def ertek(self):
        return self.pa + self.pb

# Tesztprogram :

d1 = Domino(2,6)
d2 = Domino(4,3)

d1.kiir_pontok()
d2.kiir_pontok()

print "c", d1.ertek() + d2.ertek() 

lista_dominok = []
for i in range(7):
    lista_dominok.append(Domino(6, i))

vt =0
for i in range(7):
    lista_dominok[i].kiir_pontok()
    vt = vt + lista_dominok[i].ertek()
    
print "Összes pont :", vt    
