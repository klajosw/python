#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Mindegyik sor elsõ karakterét nagybetûvé alakítja

fiSource = raw_input("A kezelendo file neve : ")
fiDest = raw_input("A celfile neve : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

while 1:
    ch = fs.readline()
    if ch == "":
        break
    if ch[0] >= "A" and ch[0] <= "Z":
        # az elsõ karakter nagybetû. Nem csinálunk semmit sem.
        pass
    else:
        # A karakterlánc visszaállítása:
        pc = ch[0].upper()      # Az elsõ átalakított karakter
        rc = ch[1:]             # a karakterlánc többi része 
        ch = pc + rc            # egyesítés
        # egy beépített metódust alkalmazó változat :
        # ch = ch.capitalize()
    # Átírás :    
    fd.write(ch)

fd.close()    
fs.close()

