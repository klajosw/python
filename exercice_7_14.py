#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def volBox(x1 =10, x2 =10, x3 =10):
    "Egy  parallelepipedon térfogata"
    return x1 * x2 * x3

# teszt :
print volBox()
print volBox(5.2)
print volBox(5.2, 3)
