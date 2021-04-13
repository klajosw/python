#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Olimpiai karikák  - minden karikát külön rajzoló változat.

from Tkinter import *

# Függvények az 5 karika rajzolásához :

def drawCircle(i):
    x1, y1 = coord[i][0], coord[i][1]
    can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =colour[i])

def a1():
    drawCircle(0)

def a2():
    drawCircle(1)

def a3():
    drawCircle(2)

def a4():
    drawCircle(3)

def a5():
    drawCircle(4)

##### Fõprogram : ##########

# Az 5 karika X,Y koordinátái :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# az 5 karika színei :
colour = ["red", "yellow", "blue", "green", "black"]

base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
but = Button(base, text ="Kilép", command =base.quit)
but.pack(side = RIGHT)

# Az 5 gomb létrehozása :
Button(base, text='1', command = a1).pack(side =LEFT)
Button(base, text='2', command = a2).pack(side =LEFT)
Button(base, text='3', command = a3).pack(side =LEFT)
Button(base, text='4', command = a4).pack(side =LEFT)
Button(base, text='5', command = a5).pack(side =LEFT)
base.mainloop()