#! /usr/bin/env python
# -*- coding: Utf-8 -*-

class auto:
    def __init__(self, marka = 'Ford', szin = 'piros'):
        self.szin = szin
        self.marka = marka
        self.vezeto = 'senki'
        self.sebesseg = 0
        
    def gyorsit(self, gyorsulas, idotartam):
        if self.vezeto =='senki':
            print "Ennek az autónak nincs vezetője !"
        else:    
            self.sebesseg = self.sebesseg + gyorsulas * idotartam
        
    def valaszt_sofort(self, nev):
        self.vezeto = nev    
        
    def kiir_mindent(self):
        print "%s %s vezeti %s, sebesseg = %s m/s" % \
            ( self.szin, self.marka, self.vezeto, self.sebesseg)     
    
a1 = auto('Peugeot', 'kék')
a2 = auto(szin = 'zöld')
a3 = auto('Mercedes')
a1.valaszt_sofort('Romeo')
a2.valaszt_sofort('Juliette')
a2.gyorsit(1.8, 12)
a3.gyorsit(1.9, 11)
a1.kiir_mindent()
a2.kiir_mindent()
a3.kiir_mindent()
