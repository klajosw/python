#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Kartyacsata

from exercice_12_07 import KartyaJatek

jatekA = KartyaJatek()        # az elso jatek letrehozasa     
jatekB = KartyaJatek()        # a masodik jatek letrehozasa     
jatekA.kever()               # m�ange de chacun
jatekB.kever()
pA, pB = 0, 0               # compteurs de points des joueurs A et B

# mindegyik jatek eseteben 52-szer huzunk :
for n in range(52):         
    cA, cB = jatekA.huz(), jatekB.huz()
    vA, vB = cA[0], cB[0]   # a kartyak ertekei
    if vA > vB:
        pA += 1
    elif vB > vA:
        pB += 1             # (semmi sem tortenik, ha vA = vB)
    # a kartyak es a pontok egymasutani kiiratasa :
    print "%s * %s ==> %s * %s" % (jatekA.kartya_neve(cA),
                                    jatekB.kartya_neve(cB), pA, pB) 

print "Az A jatekos %s pontot nyert, a B jatekos %s pontot nyert." % (pA, pB)
