#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A kulcsok és �értékek felcserélése egy szótárban

def inverse(dico):
    "egy új szótár létrehozása lépésről lépésre"
    dic_inv ={} 
    for cle in dico:
        item = dico[cle]  
        dic_inv[item] = cle
        
    return dic_inv

# programteszt :

dico = {'Computer':'Szamitogep',
        'Mouse':'Eger',
        'Keyboard':'Billentyuzet',
        'Hard disk':'Merev lemez',
        'Screen':'Kepernyo'}

print dico
print inverse(dico)