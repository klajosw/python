#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Numerikus adatok formázása
# Egy szövegfile-t kezelünk, aminek minden sora egy valós számot tartalmaz
# (exponens nélküli és string formában van kódolva)    

def kerekit(real):
    ".0 -ra vagy .5 -re kerekített egész szám reprezentációja"
    ent = int(real)             # a szám egészrésze
    fra = real - ent            # törtrész
    if fra < .25 :
        fra = 0
    elif fra < .75 :
        fra = .5
    else:
        fra = 1
    return ent + fra    

fiSource = raw_input("A kezelendo file neve : ")
fiDest = raw_input("A celfile neve : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
    line = fs.readline()
    if line == "" or line == "\n":
        break
    n = kerekit(float(line))      # átalakítás <float> -tá, majd kerekítés
    fd.write(str(n) + "\n")         # kiírás fileba

fd.close()
fs.close()