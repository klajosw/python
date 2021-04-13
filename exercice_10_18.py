#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def csereKisNagy(ch):
    "a ch karakterláncban felcseréli egymással a kis- és a nagybetûket"
    ujC = ""                   # a létrehozandó karakterlánc
    for car in ch:
        code = ord(car)
        if car >= "A" and car <= "Z":
            code = code + 32
        elif car >= "a" and car <= "z":
            code = code - 32
        ujC = ujC + chr(code)
    return ujC

# Teszt :
if __name__ == '__main__':
    print csereKisNagy("Ferdinand-Charles de CAMARET")

