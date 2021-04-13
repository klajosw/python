#! /usr/bin/env python
# -*- coding: Utf-8

# Dámatábla véletlenszerűen elhelyezett korongokkal

from Tkinter import *
from random import randrange        # véletlenszám generátor

def dama_tabla():
    "10 négyzetből álló sor rajzolása váltakozó eltolódással"
    y = 0
    while y < 10:
        if y % 2 == 0:              # két alkalomból egyszer
            x = 0                   # a négyzetekből álló sor 
        else:                       # egy négyzetnyi 
            x = 1                   # eltolódással fog kezdődni
        line_of_squares(x*c, y*c)
        y += 1
        
def line_of_squares(x, y):
    "x, y -ból kiindulva négyzetekből álló vonal rajzolása" 
    i = 0
    while i < 10:
        can.create_rectangle(x, y, x+c, y+c, fill='navy')
        i += 1
        x += c*2                    # négyzetes közök hagyása
        
def circle(x, y, r, colour):
    "x,y középpontú és r sugarú kör rajzolása"
    can.create_oval(x-r, y-r, x+r, y+r, fill=colour)
    
def korong_hozzaadasa():
    "korong véletlenszerű rajzolása a dámatáblára"
    # a korong coordinátáinak sorsolása :
    x = c/2 + randrange(10) * c
    y = c/2 + randrange(10) * c
    circle(x, y, c/3, 'red')
        
##### Főprogram : ############
    
# Próbálja meg jól "paraméterezni" a programjait, ahogyan ebben a scriptben tettük.
# A script tetszőleges méretű dámatáblákat rajzolhat egyetlen érték, 
# a négyzet méretének megváltoztatásával :
 
c = 30                  # négyzetek mérete

ablak = Tk()
can = Canvas(ablak, width =c*10, height =c*10, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(ablak, text ='dámatábla', command =dama_tabla)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(ablak, text ='korongok', command =korong_hozzaadasa)
b2.pack(side =RIGHT, padx =3, pady =3)
ablak.mainloop()
