#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# fok -> radián átalakítás
# Ismétlés : 1 radiános az a szög, melyhez tartozó körív hossza
# a kör sugarának hosszával.
# Mivel a kerület 2 pi R, ezért egy 1 radiános szög 
# 360° / 2 pi -nek, vagy 180° / pi -nek felel meg

# A kiindulási szög fok, perc, másodpercben megadva :
deg, min, sec  = 32, 13, 49

# A szögmásodpercek átalakítása szögpercekbe :
# (a tizedespont miatt az átalakítás eredménye valós szám lesz)
fm = sec/60.
# A szögpercek átalakítása fokokká :
fd = (min + fm)/60
# A szög értékének tizedestörtté alakítása :
ang = deg + fd
# pi értéke :
pi = 3.14159265359
# 1 radián fokokban megadva :
rad = 180 / pi
# A szög átalakítása radiánná :
arad = ang / rad
# Kiíratás :
print deg, "°", min, "'", sec, '" =', arad, "radián"