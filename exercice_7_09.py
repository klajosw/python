#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def karSzamlalo(ca, ch):
    "Megadja a ca karakter el�fordul�sainak sz�m�t a ch stringben"
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot = tot + 1
        i = i + 1
    return tot    
        
# teszt :
print karSzamlalo("e","Ez a karakterl�nc egy p�lda")
