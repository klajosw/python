#! /usr/bin/env python
# -*- coding: Latin-1 -*-

n = 1       # kocka sorszáma
g = 1       # az elhelyezendõ búzaszemek száma
# A kódváltozathoz elég g-t <float> -ként definiálni
# a fenti sort a következõvel helyettesítve:  g = 1.

while n < 65 :
    print n, g
    n, g = n+1, g*2
