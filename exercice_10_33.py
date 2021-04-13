#! /usr/bin/env python
# -*- coding: Utf-8 -*-

## Ez a változat egymásba ágyazott listákat alkalmaz ##
## (amit könnyen helyettesíthetnénk két különbözõ listával)

# Az alábbi lista két elemet tartalmaz, amik maguk is listák.
# a 0. elem a hónapok napjainak számát tartalmazza, míg
# az 1. elem a 12 hónap nevét tartalmazza :
honap = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július',
         'Augusztus', 'Szeptember', 'Október', 'November', 'December']]

nap = ['Vasárnap','Hétfõ','Kedd','Szerda','Csütörtök','Péntek','Szombat']

evn, hon, hen, m = 0, 0, 0, 0

while evn <365:
    evn, hon = evn +1, hon +1    # en = az év napja,  hon = a hónap napja
    hen = (evn +3) % 7           # hen js = a hét napja + offset 
                                 # a kezdõnap kiválasztását teszi lehetõvé
  
    if hon > honap[0][m]:               # a 0. lista m-edik eleme
        hon, m = 1, m+1

    print honap[1][m], hon, nap[hen]    # az 1. lista m-edik eleme
