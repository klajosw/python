#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Simulation du phénomène de gravitation universelle

from Tkinter import *
from math import sqrt

def distance(x1, y1, x2, y2):
    "az x1,y1 és x2,y2 pontokat elválasztó távolság"
    d = sqrt((x2-x1)**2 + (y2-y1)**2)       # Pythagoras tétele
    return  d

def forceG(m1, m2, di):
    "egymástól di távolságra lévõ m1 et m2 tömegû tömegpontok közötti gravitációs erõ"
    return m1*m2*6.67e-11/di**2             # Newton-törvény

def mozdul(n, gd, hb):
    "az n csillag elmozdulása, balról jobbra vagy fentrõl lefelé"
    global x, y, step
    # új koorddináták :
    x[n], y[n] = x[n] +gd, y[n] +hb
    # a rajz elmozdulása a vásznon :
    can.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)
    # az új távolság számolása :
    di = distance(x[0], y[0], x[1], y[1])
    # a "képernyõtávolság" konverziója "asztronómiai távolsággá" :
    diA = di*1e9            # (1 pixel => 1 millió km)
    # a megfelelõ gravitációs erõ számolása :
    f = forceG(m1, m2, diA)
    # az új távolság- és erõértékek számolása :
    valDis.configure(text="Távolság = " +str(diA) +" m")
    valFor.configure(text="Erõ = " +str(f) +" N")
    # a "lépés" adaptálása a távolság függvényében :
    step = di/10

def balra1():
    mozdul(0, -step, 0)

def jobbra1():
    mozdul(0, step, 0)

def fel1():
    mozdul(0, 0, -step)

def le1():
    mozdul(0, 0, step)

def balra2():
    mozdul(1, -step, 0)

def jobbra2():
    mozdul (1, step, 0)

def fel2():
    mozdul(1, 0, -step)

def le2():
    mozdul(1, 0, step)

# A csillagok tömege :
m1 = 6e24          # (a Föld tömege, kg-ban)
m2 = 6e24          #
astre = [0]*2      # lista a rajzok hivatkozásainak tárolására
x =[50., 350.]     # a csillagok X (képernyõ)koordinátáinak  listája 
y =[100., 100.]    # a csillagok Y (képernyõ)koordinátáinak  listája
step =10           # egy elmozdulás "lépés"

# Ablak létrehozása :
ablak = Tk()
ablak.title(' Newton-féle gravitációs törvény')
# Címkék :
valM1 = Label(ablak, text="M1 = " +str(m1) +" kg")
valM1.grid(row =1, column =0)
valM2 = Label(ablak, text="M2 = " +str(m2) +" kg")
valM2.grid(row =1, column =1)
valDis = Label(ablak, text="Distance")
valDis.grid(row =3, column =0)
valFor = Label(ablak, text="Force")
valFor.grid(row =3, column =1)
# Vászon 2 csillag rajzával:
can = Canvas(ablak, bg ="light yellow", width =400, height =200)
can.grid(row =2, column =0, columnspan =2)
astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10,
                           fill ="red", width =1)
astre[1] = can.create_oval(x[1]-10, y[1]-10, x[1]+10, y[1]+10,
                           fill ="blue", width =1)
# 4 gombból álló 2 gombcsoport, mindegyikük egy keretbe (frame) van téve :
fra1 = Frame(ablak)
fra1.grid(row =4, column =0, sticky =W, padx =10)
Button(fra1, text="<-", fg ='red',command =balra1).pack(side =LEFT)
Button(fra1, text="->", fg ='red', command =jobbra1).pack(side =LEFT)
Button(fra1, text="^", fg ='red', command =fel1).pack(side =LEFT)
Button(fra1, text="v", fg ='red', command =le1).pack(side =LEFT)
fra2 = Frame(ablak)
fra2.grid(row =4, column =1, sticky =E, padx =10)
Button(fra2, text="<-", fg ='blue', command =balra2).pack(side =LEFT)
Button(fra2, text="->", fg ='blue', command =jobbra2).pack(side =LEFT)
Button(fra2, text="^", fg ='blue', command =fel2).pack(side =LEFT)
Button(fra2, text="v", fg ='blue', command =le2).pack(side =LEFT)

ablak.mainloop()