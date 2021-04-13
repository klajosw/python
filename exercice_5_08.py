#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Karakter beszúrása egy stringbe

# Kiindulási string :
ch = "Gaston"
# A beszúrandó karakter :
cr = "*"
# A beszúrandó karakterek száma eggyel kisebb a stringben lévõ karakterek
# számánál. A stringet a második karakterétõl kezdve manipuláljuk
# (nem vesszük figyelembe az elsõ karaktert).
lc = len(ch)    # karakterek száma 
i = 1           # a megvizsgálandó elsõ karakter indexe (valójában a második)
nch = ch[0]     # a konstruálandó új string (már tartalmazza az elsõ karaktert.)
while i < lc:
    nch = nch + cr + ch[i]
    i = i + 1    
# Kiíratás :
print nch
