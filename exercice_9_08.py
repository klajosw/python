#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Klubtagok adatainak mentése

def kodolas():
    "a beírt adatok listáját, vagy egy üres listát ad vissza"
    print "*** Írja be az adatokat (vagy <Enter> a befejezéshez) :"
    while 1:
        csaladNev = raw_input("Csaladnev : ")
        if csaladNev == "":
            return []
        utoNev = raw_input("Utonev : ")
        utcaSzam = raw_input("Cím (utca és hazszam) : ")
        irSzam = raw_input("Iranyitoszam : ")
        helyseg = raw_input("Helysegnev : ")
        tel = raw_input("Telefonszam : ")
        print csaladNev, utoNev, utcaSzam, irSzam, helyseg, tel
        ver = raw_input("<Enter> ha korrekt, <n> ha nem ")
        if ver == "":
            break
    return [csaladNev, utoNev, utcaSzam, irSzam, helyseg, tel]

def fileba_iras(lista):
    "a lista adatainak kiírása <#>-nel elválasztva a listaelemeket"
    i = 0
    while i < len(lista):
        of.write(lista[i] + "#")
        i = i + 1
    of.write("\n")              # caractère de fin de ligne    
    
nameF = raw_input('Célfile neve : ')
of = open(nameF, 'a')
while 1:
    tt = kodolas()
    if tt == []:
        break
    fileba_iras(tt)

of.close()