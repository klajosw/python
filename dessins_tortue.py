#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Module contenant une série de fonctions graphiques "tortue"

from turtle import *

def forme(n, a, meret, couleur, angle):
    "forme de base, avec n = nombre de côtés, a = angle des sommets"
    down()              # leteszi a ceruzát
    right(angle)        # kezdõirány válastása
    color(couleur)      # rajzszín választása
    # garafikus alakzat választása :
    c =0
    while c < n:
        forward(meret)
        right(a)
        c = c +1
    up()

def carre(meret, couleur, szog):
    forme(4, 90, meret, couleur, szog)

def triangle(meret, couleur, szog):
    forme(3, 120, meret, couleur, szog)

def etoile5(meret, couleur, szog):
    forme(5, 144, meret, couleur, szog)
    # 144° = 180° - 360°/10

def etoile6(meret, szin, szog):
    # az elsõ egyenlõoldalú háromszög rajzolása :
    forme(3, 120, meret, szin, szog)
    # a ceruza pozícionálása :
    left(30)
    forward(meret/1.732)       # 1.732 = 2 * cos(30°)
    # második háromszög rajzolása forgatás után :
    right(90)
    forme(3, 120, meret, szin, szog)
    # ha a kezdõ irányt meg akarjuk találni :
    #left(60)

