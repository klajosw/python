#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# A véletlenszám generátor tesztelése

from random import random           # véletlenszerûen egy 0 és 1 közé esõ valós számot sorsol

n = raw_input("Hany veletlen szamot sorsoljon (default = 1000) : ")
if n == "":
    nVal =1000
else:
    nVal = int(n)

n = raw_input("A reszintervallumok szama 0-1 -ben (2 es "
              + str(nVal/10) + " között, default =5) : ")
if n == "":
    nFra =5
else:
    nFra = int(n)

if nFra < 2:
    nFra =2
elif nFra > nVal/10:
    nFra = nVal/10

print nVal, "húzás értékeinek megoszlása ..."
listVal = [0]*nVal                      # nullákból álló listát hoz létre
for i in range(nVal):                   # majd mindegyik elemet módosítja
    listVal[i] = random()

print "Megszámolja az értékeket a(z)", nFra, "részintervallum mindegyikében ..."
listCompt = [0]*nFra                    # létrehozza a számlálók listáját 
# az értékek listájának bejárása :
for valeur in listVal:
    # megkeresi az értéket tartalmazó részintervallum indexét :    
    index = int(valeur*nFra)
    # incrementálja a megfelelõ számlálót :
    listCompt[index] = listCompt[index] +1

# kiíratja a számlálók állapotát :
for compt in listCompt:
    print compt,