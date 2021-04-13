#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def eleMax(lst, eleje =0, vege =-1):
    "az l. lista legnagyobb elemét adja vissza"
    if vege == -1:
        vege = len(lst)
    max, i = 0, 0
    while i < len(lst):
        if i >= eleje and i <= vege and lst[i] > max:
            max = lst[i]
        i = i + 1
    return max

# teszt :
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print eleMax(serie)
print eleMax(serie, 2)
print eleMax(serie, 2, 5)
