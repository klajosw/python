#! /usr/bin/env python
# -*- coding: Utf-8 -*-

class Muhold:
    def __init__(self, nev, tomeg =100, sebesseg =0):
        self.nev, self.tomeg, self.sebesseg = nev, tomeg, sebesseg
         
    def lokes(self, ero, idotartam):
        self.sebesseg = self.sebesseg + ero * idotartam / self.tomeg
        
    def energia(self):
        return self.tomeg * self.sebesseg**2 / 2    
                
    def kiir_sebesseg(self):
        print "%s Műhold sebessége = %s m/s" \
                          % (self.nev, self.sebesseg)

# Tesztprogram :

s1 = Muhold('Zoé', tomeg =250, sebesseg =10)

s1.lokes(500, 15)
s1.kiir_sebesseg()
print s1.energia()
s1.lokes(500, 15)
s1.kiir_sebesseg()
print s1.energia()