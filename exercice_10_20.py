#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def mh(car):
    "ellenõrzi, hogy car magánhangzó e"
    if car in "AEIOUYaeiouy":
        return 1
    else:
        return 0

def szamlaloMh(ch):
    "megszámolja a magánhangzókat a ch karakterláncban"
    n = 0
    for c in ch:
        if mh(c):
            n = n + 1
    return n

# Test :
if __name__ == '__main__':
    print szamlaloMh("Monty Python Flying Circus")

