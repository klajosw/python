#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Kártyahúzás�
from random import randrange

colours = ['Pique', 'Trefle', 'Carreau', 'Coeur']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'junga', 'dáma', 'király', 'ász']

# Az 52 kártya listájának a létrehozása :
card =[]
for coul in colours:
     for val in values:
          card.append("%s %s" % (coul, str(val)))

# V�etlenszer? hz� :
while 1:
     k = raw_input("<c> kártyát húz, <Enter> vége") 
     if k =="":
          break
     r = randrange(52)
     print card[r]