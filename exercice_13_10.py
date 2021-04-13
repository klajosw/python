#! /usr/bin/env python
# -*- coding: Utf-8 -*-

##################################################
#                 Oscillo2.py                    #
# <Canvas> -bol szarmaztatott specializalt widget#
#   kiteres/ido gorbe rajzolasara szolgal        #
#                                                #
#      Szerzo : G.Swinnen (Liege, Belgium)       #
#         16/03/2002 - Licence GPL               #
##################################################

from Tkinter import *
from math import sin, pi

class OscilloGraphe(Canvas):
    "kiteres/ido gorbe rajzolasara szolgalo specializalt vaszon"
    def __init__(self, master=None, width_=200, height_=150):
        "A grafika constructora : tengelyek es vizszintes skala."
        # a szulo widget elkeszitese :
        Canvas.__init__(self)                             # a szuloosztaly 
        self.configure(width=width_, height=height_)      # constructoranak hivasa 
        self.width_, self.height_ = width_, height_       # tarolas
        # vizszintes skala rajzolasa 8 beosztassal :
        step = (width_-25)/8.          # vizszintes skala intervallumai
        for t in range(1, 9):
            stx = 10 + t*step        # +10, hogy az origotol eltavolodjunk
            self.create_line(stx, height_/10, stx, height_*9/10, fill='grey')
        # fuggoleges skala rajzolasa 8 beosztassal :
        step = height_*2/25.            # vizszintes skala intervallumai
        for t in range(-5, 6):
            sty = height_/2 -t*step      # height_/2 hogy az origotol eltavolodjunk
            self.create_line(10, sty, width_-15, sty, fill='grey')
        # referencia tengelyek rajzolasa :
        self.create_line(10, height_/2, width_, height_/2, arrow=LAST)    # X-tengely
        self.create_line(10, height_-5, 10, 5, arrow=LAST)           # Y-tengely
        # a tengelyek vegen megadjuk a fizikai mennyisegek nevet :
        self.create_text(20, 10, anchor =CENTER, text = "e")
        self.create_text(width_-10, height_/2-12, anchor =CENTER, text = "t")

    def drawCurve(self, freq=1, phase=0, ampl=10, colo='red'):
        "1 sec idotartamra eso kiteres/ido gorbe rajzolasa"
        curve =[]                       # koordinatak listaja
        step = (self.width_-25)/1000.      # az X-skala 1 sec-nak felel meg
        for t in range(0,1001,5):       # amit 1000 ms-ra osztunk fel
            e = ampl*sin(2*pi*freq*t/1000 - phase)
            x = 10 + t*step
            y = self.height_/2 - e*self.height_/25
            curve.append((x,y))
        n = self.create_line(curve, fill=colo, smooth=1)
        return n                        # n = a rajz sorszama

#### Kod az osztaly tesztelesehez : ####

if __name__ == '__main__':
    root = Tk()
    gra = OscilloGraphe(root, 250, 180)
    gra.pack()
    gra.configure(bg ='ivory', bd =2, relief=SUNKEN)
    gra.drawCurve(2, 1.2, 10, 'purple')
    root.mainloop()

#traceCourbe -> drawCurve
#height -> height_
#width -> width_
#pas -> step
#coul -> colo