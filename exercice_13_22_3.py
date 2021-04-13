# -*- coding: Utf-8 -*-

# Corrig�d'interro de programmation Python - Juin 2004

from Tkinter import *
from random import randrange
from math import sin, cos, pi

class FaceDom:
    def __init__(self, can, val, pos, size =70):
        self.can =can        
        x, y, c = pos[0], pos[1], size/2
        self. square = can.create_rectangle(x -c, y-c, x+c, y+c,
                                           fill ='ivory', width =2)
        d = size/3         
        # a pontok elrendezese az oldalon, mind a 6 esetre :
        self.pDispo = [((0,0),),
                       ((-d,d),(d,-d)),
                       ((-d,-d), (0,0), (d,d)),
                       ((-d,-d),(-d,d),(d,-d),(d,d)),
                       ((-d,-d),(-d,d),(d,-d),(d,d),(0,0)),
                       ((-d,-d),(-d,d),(d,-d),(d,d),(d,0),(-d,0))]
                    
        self.x, self.y, self.dim = x, y, size/15
        self.pList =[]      # ennek az oldalnak a pontjait tartalmazo lista 
        self.draw_points(val)
        
    def draw_points(self, val):
        # a val erteknek megfelelo pontok rajzainak a letrehozasa :
        disp = self.pDispo[val -1]
        for p in disp:
            self.circle(self.x +p[0], self.y +p[1], self.dim, 'red')
        self.val = val
        
    def circle(self, x, y, r, colo):
        self.pList.append(self.can.create_oval(x-r, y-r, x+r, y+r, fill=colo))
        
    def erase(self, flag =0):
        for p in self.pList:
            self.can.delete(p)
        if flag:
            self.can.delete(self.square)
        
class Project(Frame):
    def __init__(self, width_, height_):
        Frame.__init__(self)
        self.width_, self.height_ = width_, height_
        self.can = Canvas(self, bg='dark green', width =width_, height =height_)
        self.can.pack(padx =5, pady =5)
        # az elhelyezendo gombok es az esemenykezeloik listaja :
        bList = [("A", self.buttonA), ("B", self.buttonB),
                 ("C", self.buttonC), ("Quitter", self.buttonQuit)]
        bList.reverse()         # a lista sorrendjet megforditja
        for b in bList:
            Button(self, text =b[0], command =b[1]).pack(side =RIGHT, padx=3)
        self.pack()
        self.die =[]            # a kockakat tartalmazo lista
        self.actu =0            # az aktualisan kivalasztott kocka hivatkozasa
        
    def buttonA(self):
        if len(self.die):
            return              # mert a rajzok mar leteznek !
        a, da = 0, 2*pi/13
        for i in range(13):
            cx, cy = self.width_/2, self.height_/2
            x = cx + cx*0.75*sin(a)             # kor elhelyezesehez,
            y = cy + cy*0.75*cos(a)             # a trigonometriat alkalmazzuk !
            self.die.append(FaceDom(self.can, randrange(1,7) , (x,y), 65))
            a += da

    def buttonB(self):
        # a kivalasztott kocka ponterteket incrementalja. A kovetkezo kocka  ter at :
        v = self.die[self.actu].val
        v = v % 6
        v += 1        
        self.die[self.actu].erase()
        self.die[self.actu].draw_points(v)
        self.actu += 1
        self.actu = self.actu % 13

    def buttonC(self):
        for i in range(len(self.die)):
            self.die[i].erase(1)
        self.die =[]
        self.actu =0
        
    def buttonQuit(self):
        self.master.destroy()
        
Project(600, 600).mainloop()

#square -> square
#taille -> size
#tracer_points -> draw_points
#die -> die
#cercle -> circle
#coul -> colo
#effacer -> erase
#larg -> width_
#haut -> height_
#bout -> button