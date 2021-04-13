#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def changeChar(ch, ca1, ca2, eleje =0, vege =-1):
    "A ch karakterláncban kicseréli az összes ca1 karaktert a ca2 karakterre"
    if vege == -1:
        vege = len(ch)
    nch, i = "", 0            # nch : a létrehozandó új karakterlánc
    while i < len(ch) :
        if i >= eleje and i <= vege and ch[i] == ca1:
            nch = nch + ca2
        else :
            nch = nch + ch[i]
        i = i + 1
    return nch

# test :
print changeChar("Ceci est une toute petite phrase", " ", "*")
print changeChar("Ceci est une toute petite phrase", " ", "*", 8, 12)
print changeChar("Ceci est une toute petite phrase", " ", "*", 12)
