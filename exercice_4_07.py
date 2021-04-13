#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A 7-es szorzótábla első 20 elemének kiíratása,
# 3 többszöröseinek jelzésével :

i = 1               # számláló: 1-től 20-ig egymás után vesszük az értékeket
while i < 21:
    # a kiírandó szorzat kiszámolása :
    t = i * 7
    # sorugrás néküli kiíratás (a vessző hasznáata) :
    print t,
    # a szorzat 3 többszöröse ? (a modulo operátor alkalmazása) :
    if t % 3 == 0:
        print "*",      # ez esetben kiíratunk egy csillagot
    i = i + 1           # minden esetben incrementáljuk a számlálót 