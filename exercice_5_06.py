#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Megadott karakter keresése egy stringben

# Kiindulási karakterlánc :
ch = "Monty python flying circus"
# A keresendõ karakter :
cr = "e"
# A keresés :
lc = len(ch)    # a megvizsgálandó karakterek száma
i = 0           # az aktuálisan vizsgált karakter indexe
t = 0           # a karakter létezése esetén beállítandó "flag"
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1    
# Kiíratás :
print "A(z)", cr, "karakter",        
if t == 1:
    print "elõfordul",
else:
    print "nem fordul elõ",
print "a(z) :", ch, "stringben"        