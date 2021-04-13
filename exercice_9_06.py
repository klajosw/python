#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Két file karakterenkénti összehasonlítása :

fich1 = raw_input("Az 1. file neve : ")
fich2 = raw_input("A 2. file neve : ")
fi1 = open(fich1, 'r')
fi2 = open(fich2, 'r')

c, f = 0, 0                 # karakterszámláló és flag 
while 1:
    c = c + 1
    car1 = fi1.read(1)      # 1 karakter beolvasása 
    car2 = fi2.read(1)      # mindegyik file-ból
    if car1 =="" or car2 =="":
        break
    if car1 != car2 :
        f = 1
        break               # eltérést talált

fi1.close()
fi2.close()

print "Ez a két file",
if f ==1:
    print "eltér a ", c, "karaktertõl"
else:
    print "azonos."