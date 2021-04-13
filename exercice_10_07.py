#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def szoSzamlalo(ch):
    "megszámolja a szavakat a ch karakterláncban"
    if len(ch) ==0:
        return 0
    nm = 1                  # a karakterlánc legalább egy szót tartalmaz           
    for c in ch:
        if c == " ":        # elég a betûközöket megszámolni
            nm = nm + 1
    return nm

# Teszt :
if __name__ == '__main__':
    print szoSzamlalo("Les petits ruisseaux font les grandes rivières")
