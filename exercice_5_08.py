#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Karakter besz�r�sa egy stringbe

# Kiindul�si string :
ch = "Gaston"
# A besz�rand� karakter :
cr = "*"
# A besz�rand� karakterek sz�ma eggyel kisebb a stringben l�v� karakterek
# sz�m�n�l. A stringet a m�sodik karakter�t�l kezdve manipul�ljuk
# (nem vessz�k figyelembe az els� karaktert).
lc = len(ch)    # karakterek sz�ma 
i = 1           # a megvizsg�land� els� karakter indexe (val�j�ban a m�sodik)
nch = ch[0]     # a konstru�land� �j string (m�r tartalmazza az els� karaktert.)
while i < lc:
    nch = nch + cr + ch[i]
    i = i + 1    
# Ki�rat�s :
print nch
