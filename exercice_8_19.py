#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# K�r�k �s  Lissajous -g�rb�k

from Tkinter import *
from math import sin, cos

def move():    
    global ang, x, y
    # az el�z� koordin�t�kat t�roljuk az �jak sz�mol�sa el�tt :
    xp, yp = x, y
    # elforgat�s 0.1 radi�nnal :
    ang = ang +.1 
    # ennek a sz�gnek a sinus-a �s cosinus-a => trigonometriai k�r egy pontj�nak koordin�t�i.
    x, y = sin(ang), cos(ang)
    # Variante d?terminant une courbe de Lissajous avec f1/f2 = 2/3 :
    # x, y = sin(2*ang), cos(3*ang)
    # sk�l�z�s (120 = k�r sugara, (150,150) = v�szon k�zepe)
    x, y = x*120 + 150, y*120 + 150
    can.coords(labda, x-10, y-10, x+10, y+10)
    can.create_line(xp, yp, x, y, fill ="blue")     # p�lyarajzol�s
    
ang, x, y = 0., 150., 270.
ablak = Tk()
ablak.title('Lissajous-g�rb�k')
can = Canvas(ablak, width =300, height=300, bg="white")
can.pack()
labda = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(ablak, text='Go', command =move).pack()

ablak.mainloop()
