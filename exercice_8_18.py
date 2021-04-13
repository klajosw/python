#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Körök és  Lissajous -görbék

from Tkinter import *
from math import sin, cos

def move():    
    global ang, x, y
    # az elõzõ koordinátákat tároljuk az újak számolása elõtt :
    xp, yp = x, y
    # elforgatás 0.1 radiánnal :
    ang = ang +.1 
    # ennek a szögnek a sinus-a és cosinus-a => trigonometriai kör egy pontjának koordinátái.
    x, y = sin(ang), cos(ang)
    # A Lissajous görbét f1/f2 = 2/3 -vel definiáló változat:
    # x, y = sin(2*ang), cos(3*ang)
    # skálázás (120 = kör sugara, (150,150) = vászon közepe
    x, y = x*120 + 150, y*120 + 150
    can.coords(labda, x-10, y-10, x+10, y+10)
    # can.create_line(xp, yp, x, y, fill ="blue")       # pályarajzolás
    
ang, x, y = 0., 150., 270.
ablak = Tk()
ablak.title('Lissajous-görbék')
can = Canvas(ablak, width =300, height=300, bg="white")
can.pack()
labda = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(ablak, text='Go', command =move).pack()

ablak.mainloop()