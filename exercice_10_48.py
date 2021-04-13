#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Szöveg szavainak előfordulási gyakoriságából készített hisztogram

nFile = raw_input('Kezelendo file neve : ')
fi = open(nFile, 'r')
text = fi.read()
fi.close()

# annak erdekeben, hogy a szoeg szavai konnyen elklulonithetok legyenek, a nem
# betu karaktereket betukozze�alakitjuk  :

alpha = "abcdefghijklmnopqrstuvwxyzíéáűúőóüöÍÉÁŰÚŐÓÜÖ"

letters = ''            # a lerehozand uj karakterlanc
for c in text:
    c = c.lower()       # minden betut kisbetuve alakit
    if c in alpha:
        letters = letters + c
    else:
        letters = letters + ' '

# az eredménystring átalakítása szavak listájává :
words = letters.split()

# a hisztogram elkészítése :
dico ={}
for m in words:
    dico[m] = dico.get(m, 0) +1

liste = dico.items()

# az eredménylista rendezése :
liste.sort()

# kiiratas :
for item in liste:
    print item[0], ":", item[1]