#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Iskolai érdemjegyek

jegyek = []           # A létrehozandó lista
n = 2                # valamilyen pozitív érték a ciklus elindításához
while n >= 0 :
    print "Írjon be egy érdemjegyet. : ",
    n = float(raw_input())      # egész számmá alakítás
    if n < 0 :
        print "OK. Befejezés."
    else:    
        jegyek.append(n)         # hozzátesz egy érdemjegyet a listához
        # A már be beírt érdemjegyeken végzett különbözõ számítások  :
        # minimális és maximális értékek + a jegyek összege. 
        min = 500               # valamennyi érdemjegynél nagyobb érték
        max, tot, i = 0, 0, 0        
        nn = len(jegyek)         # A már be beírt érdemjegyek száma
        while i < nn:
            if jegyek[i] > max:
                max = jegyek[i]
            if jegyek[i] < min:
                min = jegyek[i]
            tot = tot + jegyek[i]
            atlag = tot/nn
            i = i + 1
        print "Be beírt érdemjegyek száma =", nn, "Max =", max, "Min =", min, "Átlag =", atlag
