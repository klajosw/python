#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Két határérték közé esõ egész számok kezelése
print "Adja meg az alsó határt :",
a = input()
print "Adja meg a felsõ határt :",
b = input()
s = 0                   # a keresett összeg (kezdetben nulla)
# az a és b közötti számsorozat bejárása (beleértve a -t és b -t) :
n = a                   # az aktuálisan kezelt szám
while n <= b:
    if n % 3 ==0 and n % 5 ==0:      # változat : 'or' az 'and' helyet
        s = s + n
    n = n + 1

print "A keresett összeg :", s 