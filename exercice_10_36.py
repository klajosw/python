#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# �j elemek besz�r�sa egy m�r l�tez� list�ba

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janu�r', 'Febru�r', 'M�rcius', '�prilis', 'M�jus', 'J�nius', 'J�lius',
         'Augusztus', 'Szeptember', 'Okt�ber', 'November', 'December']

c, d = 1, 0
while d < 12 :
     t2[c:c] = [t1[d]]       # ! a besz�rt elemnek list�nak kell lenni
     c, d = c+2, d+1