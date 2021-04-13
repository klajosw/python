#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Két lista kombinálása

# Kiindulási listák :
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Január','Február','Március','Április','Május','Június',
      'Július','Augusztus','Szeptember','Októbrer','November','December']
# a konstruálandó új lista (kezdetben üres) :
t3 = []
# programhurok :
i = 0
while i < len(t1):
    t3.append(t2[i])
    t3.append(t1[i])
    i = i + 1

# Kiíratás :
print t3 