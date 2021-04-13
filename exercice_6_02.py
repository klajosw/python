#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Tetszõleges háromszög kerülete és területe

from math import sqrt

print "Adja meg az a oldal hosszát : "
a = float(raw_input())
print "Adja meg a b oldal hosszát : "
b = float(raw_input())
print "Adja meg a c oldal hosszát : "
c = float(raw_input())
d = (a + b + c)/2                # a kerület fele
s = sqrt(d*(d-a)*(d-b)*(d-c))    # terület (a képlet alapján)

print "Az oldalak hossza =", a, b, c
print "Kerület =", d*2, "Terület =", s