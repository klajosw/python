#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Erasztotenészi szita az 1 és 999 közé esõ prímszámok megkereséséhez

# Egy 1-esekbõl álló 1000 elemû lista létrehozása (az indexei 0-tól 999-ig mennek) :
lst = [1]*1000           
# A lista bejárása a 2 indexértéktõl kezdve:
for i in range(2,1000):
    # a listának azokat az elemeit, melyek indexe 
    # az i-nek többszörösei nullává tesszük :
    for j in range(i*2, 1000, i):
        lst[j] = 0

# Kiíratjuk azoknak az elemeknek az indexét, melyek értéke 1 maradt
# (a 0 elemet nem vesszük figyelembe) :
for i in range(1,1000):
    if lst[i]:
        print i,
