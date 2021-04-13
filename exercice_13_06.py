#! /usr/bin/env python
# -*- coding: Utf-8 -*-

from Tkinter import *

def circle(can, x, y, r, colour ='white'):
    "<r> sugaru kor rajzolasa a vaszon <can> <x,y> pontjaba"
    can.create_oval(x-r, y-r, x+r, y+r, fill =colour)

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)        # a szuloosztaly constructora
        self.can =Canvas(self, width =475, height =130, bg ="white")
        self.can.pack(side =TOP, padx =5, pady =5)
        Button(self, text ="Vonat", command =self.drawing ).pack(side =LEFT)
        Button(self, text ="Hello", command =self.kukucs).pack(side =LEFT)
        Button(self, text ="Világít34", command =self.light34).pack(side =LEFT)
        
    def drawing (self):
        "4 vagon letrehozasa a vasznon"
        self.w1 = Wagon(self.can, 10, 30)
        self.w2 = Wagon(self.can, 130, 30, 'dark green')
        self.w3 = Wagon(self.can, 250, 30, 'maroon')
        self.w4 = Wagon(self.can, 370, 30, 'purple')
        
    def kukucs(self):
        "emberek jelennek meg bizonyos ablakokban"
        self.w1.perso(3)        # 1. vagon, 3. ablak
        self.w3.perso(1)        # 3. vagon, 1. ablak
        self.w3.perso(2)        # 3. vagon, 2. ablak
        self.w4.perso(1)        # 4. vagon, 1. ablak
        
    def light34(self):
        "a vilagitas bekapcsolasa a 3 & 4 vagonban"
        self.w3.light()
        self.w4.light()
        
class Wagon:
    def __init__(self, canvas_, x, y, colour ='navy'):
        "egy kis vagon rajza a <canvas_> vásznon <x,y> -ban"
        # paraméterek tárolása példány-változókban :
        self.canvas_, self.x, self.y = canvas_, x, y
        # alap téglalap : 95x60 pixel :
        canvas_.create_rectangle(x, y, x+95, y+60, fill =colour)
        # 3 ablak 25x40 pixeles, 5 pixel távolságra :
        self.wind =[]    # az ablakok hivatkozasainak tarolasara 
        for xf in range(x +5, x +90, 30):
            self.wind.append(canvas_.create_rectangle(xf, y+5,
                                xf+25, y+40, fill ='black'))
        # két 12 pixel sugarú kerék  :
        circle(canvas_, x+18, y+73, 12, 'gray')
        circle(canvas_, x+77, y+73, 12, 'gray')
  
    def perso(self, wind):
        "egy ember jelenik meg a <wind> ablakban"
        # az ablakok koordinatainak kiszamolasa :
        xf = self.x + wind*30 -12
        yf = self.y + 25
        circle(self.canvas_, xf, yf, 10, "pink")      # arc
        circle(self.canvas_, xf-5, yf-3, 2)   # balszem        
        circle(self.canvas_, xf+5, yf-3, 2)   # jobbszem
        circle(self.canvas_, xf, yf+5, 3)     # szaj
        
    def light(self):
        "felkapcsolja a vagon belso vilagitasat"
        for f in self.wind:
            self.canvas_.itemconfigure(f, fill ='yellow')

app = Application()
app.mainloop()