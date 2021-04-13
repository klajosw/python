#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Lista legnagyobb elemének megkeresése

# Kiindulási lista :
tt = [32, 5, 12, 8, 3, 75, 2, 15]
# A lista kezelésekor a max változóban fogjuk tárolni 
# a legnagyobb már megtalált elemet :
max = 0
# Az elemek vizsgálata :
i = 0
while i < len(tt):
    if tt[i] > max:
        max = tt[i]         # új maximum tárolása   
    i = i + 1
# Kiíratás :
print "Lista legnagyobb elemének értéke :", max