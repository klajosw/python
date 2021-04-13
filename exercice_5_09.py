#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# String inverziója

# Kiindulási string :
ch = "zorglub"
lc = len(ch)    # az összes karakter száma
i = lc - 1      # az utolsó karaktertől fogunk kezdeni
nch = ""        # a létrehozandó új string (kezdetben üres)
while i >= 0:
    nch = nch + ch[i]
    i = i - 1    
# Kiíratás :
print nch   
