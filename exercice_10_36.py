#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Új elemek beszúrása egy már létezõ listába

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július',
         'Augusztus', 'Szeptember', 'Október', 'November', 'December']

c, d = 1, 0
while d < 12 :
     t2[c:c] = [t1[d]]       # ! a beszúrt elemnek listának kell lenni
     c, d = c+2, d+1