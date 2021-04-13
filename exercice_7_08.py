#! /usr/bin/env python
# -*- coding: Utf-8 -*-

from dessins_tortue import *

up()                        # felemeli a ceruzát
goto(-20, 120)              # kiindulási pont beállítása
tracer(1)                   # ne húzza el

# egy sorozat egyre kisebb méretû forma rajzolása :
i, t = 0, 40
while i < 9:
    carre(t, 'red', 0)      # négyzet rajzolása
    forward(t + 5)          # továbbmegy
    etoile6(t, 'blue', 0)
    forward(t +5)           # továbbmegy
    triangle(t, 'red', 0)
    forward(t +5)           # továbbmegy
    etoile5(t, 'blue', 0)
    forward(t +5)           # továbbmegy

    t -= 3                  # csökkenti a méretet
    i = i +1

a = input()                 # várakozik
