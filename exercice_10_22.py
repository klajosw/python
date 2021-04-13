#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Szavak számlálása egy szövegben

fiSource = raw_input("A file neve : ")
fs = open(fiSource, 'r')

n = 0           # számláló
while 1:
    ch = fs.readline()
    if ch == "":
        break
    # a beolvasott karakterlánc átalakítása szavak listájává :
    li = ch.split()
    # a szavak összegzése :
    n = n + len(li)    
fs.close()
print "Ez a szövegfile összesen %s szót tartalmaz" % (n)


