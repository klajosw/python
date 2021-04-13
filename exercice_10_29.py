#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Szorzótáblák kiíratása

nt = [2, 3, 5, 7, 9, 11, 13, 17, 19]

def tableMulti(m, n):
     "az m-es szorzótábla n tagját adja vissza"
     ch =""
     for i in range(n):
          v = m * (i+1)               # az egyik tag kiszámolása
          ch = ch + "%4d" % (v)       # formázás 4 karakterre
     return ch

for a in nt:
     print tableMulti(a, 15)          # csak az elsõ 15 tagot
