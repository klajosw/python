#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A kiindulási file egy <szövegfile>, aminek minden sora egy valós számot tartalmaz
# (string formában van kódolva)    

from math import pi

def caractSphere(d):
    "megadja egy d átmérõjû gömb jellemzõit"
    d = float(d)        # az argumentum (=string) átalakítása valós számmá
    r = d/2             # sugár
    ss = pi*r**2        # fõkör területe
    se = 4*pi*r**2      # felszín
    v = 4./3*pi*r**3    # térfogat (! az elsõ osztásnak valósnak kell lenni !)
    # A lentebb alkalmazott %8.2f konverziós marker hatására a kiírt szám 
    # összesen 8 helyiértéket foglal el; úgy van kerekítve, hogy 
    # a tizedes pont után két helyiérték van : 
    ch = "Diam. %6.2f cm Section = %8.2f cm² " % (d, ss)
    ch = ch +"Surf. = %8.2f cm². Vol. = %9.2f cm³" % (se, v)
    return ch

fiSource = raw_input("A kezelendo file neve : ")
fiDest = raw_input("A celfile neve : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
    diam = fs.readline()
    if diam == "" or diam == "\n":
        break
    fd.write(caractSphere(diam) + "\n")         # kiírás fileba
fd.close()
fs.close()

