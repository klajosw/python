#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Esés és visszapattanás

from Tkinter import *

def move():
    global x, y, v, dx, dv, flag
    xp, yp = x, y            # az elõzõ koordináták tárolása
    # vízszintes elmozdulás :
    if x > 385 or x < 15 :   # visszapattanás az oldalfalról :
        dx = -dx             # invertáljuk az elmozdulást
    x = x + dx
    # a függõleges sebesség variációja (mindíg lefelé):
    v = v + dv
    # függõleges elmozdulás (arányos a sebességgel)
    y = y + v       
    if y > 240:              # a föld szintje 240 pixelre : 
        y = 240              # nem mehet tovább !
        v = -v               # visszapattan : a sebesség megfordul
    # újra pozícionáljuk a labdát :    
    can.coords(labda, x-10, y-10, x+10, y+10)
    # pályavéget rajzolunk :
    can.create_line(xp, yp, x, y, fill ='light grey')
    # ... et on remet ça jusqu'à plus soif :
    if flag > 0:
        ablak.after(50,move)

def start():
    global flag
    flag = flag +1
    if flag == 1:
        move()

def stop():
    global flag
    flag =0

# a koordináták, a sebességek és az animációflag inicializálása :    
x, y, v, dx, dv, flag  = 15, 15, 0, 6, 5, 0

ablak = Tk()
ablak.title(' Esés és visszapattanás')
can = Canvas(ablak, width =400, height=250, bg="white")
can.pack()
labda = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(ablak, text='Start', command =start).pack(side =LEFT, padx =10)
Button(ablak, text='Stop', command =stop).pack(side =LEFT)
Button(ablak, text='Kilép', command =ablak.quit).pack(side =RIGHT, padx =10)

ablak.mainloop()