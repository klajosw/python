#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A kezelt file egy szövegfile, aminek minden sora egy valós számot tartalmaz
# (exponens nélkül és karakterlánc formájában kódolva)    

def kerErtek(ch):
    "a ch stringben megadott szam lekerekitett reprezentációja"
    f = float(ch)       # string konverziója valós számmá
    e = int(f + .5)     # átalakítás egésszé (Elõször 0.5-öt hozzáadunk
                        # a valós számhoz, hogy korrekten kerekítsünk)
    return str(e)       # visszaalakítás stringgé
     
fiSource = raw_input("A kezelendo file neve : ")
fiDest = raw_input("A celfile neve : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

while 1:
    line = fs.readline()       # a file egy sorának olvasása
    if line == "" or line == "\n":
        break
    line = kerErtek(line)
    fd.write(line +"\n")
    
fd.close()
fs.close()