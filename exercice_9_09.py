#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A klub file-jának kiegészítése információval

def forditas(ch):
    "a forrásfile egy sorának átalakítása adatlistává"
    dn = ""                 # ideiglenes string az adatok kiszedéséhez
    tt = []                 # a létrehozandó lista
    i = 0
    while i < len(ch):
        if ch[i] == "#":
            tt.append(dn)   # hozzáadjuk az adatot a listához és   
            dn =""          # reinicializáljuk az ideiglenes stringet
        else:    
            dn = dn + ch[i]
        i = i + 1
    return tt    
    
def kodolas(tt):
    "a tt listát adja vissza, kiegészítve a születési dátummal és a nemmel"
    print "*** Írja be az adatokat (vagy <Enter> a befejezéshez) :"
    # A listában már meglévõ adatok kiíratása :
    i = 0
    while i < len(tt):
        print tt[i],
        i = i +1
    print
    while 1:
        daNai = raw_input("Születési dátum : ")
        sexe = raw_input("Nem (f vagy n) : ")
        print daNai, sexe
        ver = raw_input("<Enter> ha korrekt, <n> ha nem ")
        if ver == "":
            break
    tt.append(daNai)
    tt.append(sexe)
    return tt

def fileba_iras(tt):
    "a tt lista adatainak kiírása <#>-nel elválasztva a listaelemeket"
    i = 0
    while i < len(tt):
        fd.write(tt[i] + "#")
        i = i + 1
    fd.write("\n")          # sorvége karakter

fSource = raw_input('Forrasfile neve : ')
fDest = raw_input('Celfile neve : ')
fs = open(fSource, 'r')
fd = open(fDest, 'w')
while 1:
    line = fs.readline()           # a forrásfile egy sorát elolvassuk
    if line =="" or line =="\n":
        break
    liste = forditas(line)         # átalakítjuk egy listává
    liste = kodolas(liste)         # kiegészítõ adatokat fûzünk hozzá
    fileba_iras(liste)             # elmentjük a célfile-ba.

fd.close()
fs.close()
