#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def tableMulti(n):
    # n-es szorzótáblát generáló függvény n (20 tag)
    # a táblát egy karakterlánc formájában adja vissza :
    i, ch = 0, ""
    while i < 20:        
        i = i + 1
        ch = ch + str(i * n) + " "
    return ch

NomF = raw_input("A letrehozando file neve : ")
file = open(NomF, 'w')

# A létrehozandó táblák 2 -tõl 30 -ig :
table = 2
while table < 31:
    file.write(tableMulti(table) + '\n')
    table = table + 1
file.close()