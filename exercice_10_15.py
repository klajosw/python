#! /usr/bin/env python
# -*- coding: Utf-8 -*-

from exercice_10_12 import nagybetu
from exercice_10_10 import szoLista

def nagybetuSzamlalo(ch):
    "a ch stringben nagybetûvel kezdõdõ szavakat számolja meg"
    c = 0
    lst = szoLista(ch)          # mondat átalakítása szavak listájává
    for szo in lst:             # a lista mindegyik szavát elemzi
        if nagybetu(szo[0]):    # a szó elsõ betûjét ellenõrzi
            c = c +1
    return c
    
# Teszt :
if __name__ == '__main__':
    phrase = "Les filles Tidgout se nomment Justine et Corinne"
    print "Ez a mondat", nagybetuSzamlalo(phrase), "nagybetûvel kezdõdõ szót tartalmaz."
