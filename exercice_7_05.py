#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def maximum(n1, n2, n3):
    "A három szám közül a legnagyobb megadása"
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# test :
print maximum(4.5, 5.7, 3.9)
print maximum(8.2, 2.1, 6.7)
print maximum(1.3, 4.8, 7.6)