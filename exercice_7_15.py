#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def volBox(x1 =-1, x2 =-1, x3 =-1):
    "Egy parallelepipedon térfogata"
    if x1 == -1 :
        return x1           # nem adtunk meg argumentumot
    elif x2 == -1 :
        return x1**3        # egy argumentum -> kocka
    elif x3 == -1 :
        return x1*x1*x2     # két argumentum -> prizmatikus test
    else :
        return x1*x2*x3

# teszt :
print volBox()
print volBox(5.2)
print volBox(5.2, 3)
print volBox(5.2, 3, 7.4)
