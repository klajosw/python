#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def indexMax(tt):
    "a tt lista legnagyobb elemének indexét adja meg"
    i, max = 0, 0
    while i < len(tt):
        if tt[i] > max :
            max, imax = tt[i], i
        i = i + 1    
    return imax

# teszt :
serie = [5, 8, 2, 1, 9, 3, 6, 4]
print indexMax(serie)