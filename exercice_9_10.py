#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Megadott sor keresése egy szövegfile-ban :

def searchCP(ch):
    "ch -ban keresi a postai irányító számot (CP) tartalmazó stringrészt"
    i, f, ns = 0, 0, 0          # ns számlálja a # kódokat
    cc = ""                     # a létrehozandó string
    while i < len(ch):
        if ch[i] =="#":
            ns = ns +1
            if ns ==3:          # az irányítószám a 3. # után található
                f = 1           # flag
            elif ns ==4:        # nincs értelme a 4. # kód után olvasni
                break
        elif f ==1:             # az olvasott karakter részét képezi
            cc = cc + ch[i]     # a keresett CP -nek -> elmentjük
        i = i +1
    return cc    
        
nevF = raw_input("A kezelendo file neve : ")
codeP = raw_input("A keresendo iranyitoszam : ")
fi = open(nevF, 'r')
while 1:
    line = fi.readline()
    if line =="":
        break
    if searchCP(line) == codeP:
        print line
fi.close()