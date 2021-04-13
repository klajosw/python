#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Module contenant une s�rie de fonctions graphiques "tortue"

from turtle import *

def forme(n, a, meret, couleur, angle):
    "forme de base, avec n = nombre de c�t�s, a = angle des sommets"
    down()              # leteszi a ceruz�t
    right(angle)        # kezd�ir�ny v�last�sa
    color(couleur)      # rajzsz�n v�laszt�sa
    # garafikus alakzat v�laszt�sa :
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
    # 144� = 180� - 360�/10

def etoile6(meret, szin, szog):
    # az els� egyenl�oldal� h�romsz�g rajzol�sa :
    forme(3, 120, meret, szin, szog)
    # a ceruza poz�cion�l�sa :
    left(30)
    forward(meret/1.732)       # 1.732 = 2 * cos(30�)
    # m�sodik h�romsz�g rajzol�sa forgat�s ut�n :
    right(90)
    forme(3, 120, meret, szin, szog)
    # ha a kezd� ir�nyt meg akarjuk tal�lni :
    #left(60)

