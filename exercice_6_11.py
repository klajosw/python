#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Háromszögek számolásai

from sys import exit      # rendszerfüggvényeket tartalmazó module 

print """
Adja meg az oldalak hosszát
(az értéküket vesszõvel válassza el) :"""
a, b, c = input()
# Csak akkor szerkeszthetõ meg egy háromszög, ha 
# egy oldalának hossza rövidebb, mint a másik két oldal hosszának az összege :
if a < (b+c) and b < (a+c) and c < (a+b) :
    print "Ez a három hossz meghatároz egy háromszöget."
else:
    print "Nem lehet ilyen háromszöget szerkeszteni !"
    exit()          # ezért kilépünk a programból.

f = 0
if a == b and b == c :
    print "Ez egyenlõoldalú háromszög."
    f = 1
elif a == b or b == c or c == a :
    print "Ez egyenlõszárú háromszög."
    f = 1
if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b :
    print "Ez derékszögû háromszög."
    f = 1
if f == 0 :
    print "Ez általános háromszög."

#########  Másik változat (proposée par Alex Misbah) ######### :
a=input('Adjuk meg az a oldal hosszát :')
b=input('Adjuk meg az b oldal hosszát :')
c=input('Adjuk meg az c oldal hosszát :')

ab_carre=(a*b)**2
pytha=(b*c)**2+(c*a)**2

if a<(b+c) and b<(a+c) and c <(a+b):
    print " a hosszok egy háromszöget definiálnak"
    if ab_carre == pytha:
        print "Ez derékszögû háromszög."
    elif a == b == c:
        print "Ez egyenlõoldalú háromszög."
    elif a == b or b == c or c == a:
        print "Ez egyenlõszárú háromszög."
    else:
        print "Ez általános háromszög."
else:
    print "Az a, b és c nem határoznak meg háromszöget."