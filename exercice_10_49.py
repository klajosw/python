#! /usr/bin/env python
# -*- coding: Utf-8 -*-
# szoveg kodolasa szotarba

nFile = raw_input('Kezelendo file neve : ')
fi = open(nFile, 'r')
text = fi.read()
fi.close()

# Ugy tekintjük, hogy a szavak olyan karakterek sorozatai, amik az alabbi stringnek
# kepezik reszeit. Minden mas karakter szeparator :

alpha = "abcdefghijklmnopqrstuvwxyzáéíóőúű"

# szotar letrehozasa :
dico ={}
# a szoveg�oszes karakterenek bejarasa :
i =0                    # az eppen beolvasott karakter indexe
word =""                # munkavaltozo : az eppen beolvasott szo�
for c in text:
    c = c.lower()       # minden betut kisbetuve alakit
    
    if c in alpha:      # alfabetikus karakter => egy szo belsejeben vagyunk
        word = word + c   
    else:               # nem alfabetikus karakter => szo vege
        if word !="":    # hogy figyelmen kivül hagyjuk az egymast koveto
            # nem alfabetikus karaktereket minden szo szamara, lerehozunk egy indexlistat :
            if dico.has_key(word):       # már listába vett szo :
                dico[word].append(i)     # egy index hozzaadasa a listahoz
            else:                       # eloszor elofordulo szo�:
                dico[word] =[i]          # indexek listájanak letrehozasa
            word =""     # a kovetkezo szo olvasasanak elokeszitese
    i = i + 1              # a kovetkezo karakter indexe
      
# A szotar kiiratasa :
for key, value in dico.items():
    print key, ":", value