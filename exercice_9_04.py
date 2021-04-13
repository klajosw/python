#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Ez a script azt is bemutatja, hogyan változtatjuk meg egy file tartalmát 
# úgy, hogy elõször átvisszük az egészet egy listába, majd
# a listát a módosítás után kiírjuk a file-ba

def triplerEspaces(ch):
    "a függvény megháromszorozza a szavak közötti távolságot a ch karakterláncban"
    i, uj = 0, ""
    while i < len(ch):
        if ch[i] == " ":
            uj = uj + "   "
        else:
            uj = uj + ch[i]
        i = i +1    
    return uj

nameF = raw_input("File neve : ")
file = open(nameF, 'r+')              # 'r+' = mode read/write
lines = file.readlines()            # az összes sort elolvassa

n=0
while n < len(lines):
    lines[n] = triplerEspaces(lines[n])
    n =n+1
    
file.seek(0)                         # visszatérés a file elejére
file.writelines(lines)              # újra kiírja
file.close()