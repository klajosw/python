#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Páros és páratlan számok szétválasztása
# Kiindulási lista :
tt = [32, 5, 12, 8, 3, 75, 2, 15]
pairs = []
impairs = []
# Az elemek vizsgálata :
i = 0
while i < len(tt):
    if tt[i] % 2 == 0:
        pairs.append(tt[i])
    else:
        impairs.append(tt[i])
    i = i + 1
# Kiíratás :
print "Páros számok :", pairs
print "Páratlan számok :", impairs