#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Adott karakter indexének megkeresése egy stringben

def keres(ch, car, deb=0):
    "megkeresi a car karakter indexét a ch karakterláncban"
    i = deb
    while i < len(ch):
        if ch[i] == car:
            return i		# megtalálta a karaktert -> vége
        i = i + 1
    return -1       		# az egész karakterláncot végignézte, nincs eredményz 

# Test :
if __name__ == '__main__':
    print keres("Coucou c'est moi", "z")
    print keres("Juliette & Roméo", "&")
    print keres("César & Cléopâtre", "r", 5)
