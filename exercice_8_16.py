#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Fahrenheit <=> Celsius átalakítás

from Tkinter import *

def convFar(event):
    "a hõmérséklet értéke Fahrenheit fokban kifejezve"
    tF = eval(mezoTC.get())
    varTF.set(str(tF*1.8 +32))

def convCel(event):
    "a hõmérséklet értéke Celsius fokban kifejezve"
    tC = eval(mezoTF.get())
    varTC.set(str((tC-32)/1.8))

ablak = Tk()
ablak.title('Fahrenheit/Celsius')

Label(ablak, text='Temp. Celsius :').grid(row =0, column =0)
# Adatbeviteli mezõhöz asszociált "Tkinter változó". Ez az "objektum-változó"
# biztosítja az interface-t a TCL és a Python között (lásd jegyzet, 165. oldal) :
varTC =StringVar()
mezoTC = Entry(ablak, textvariable =varTC)
mezoTC.bind("<Return>", convFar)
mezoTC.grid(row =0, column =1)
# A Tkinter változó tartalmának inicializálása :
varTC.set("100.0")

Label(ablak, text='Temp. Fahrenheit :').grid(row =1, column =0)
varTF =StringVar()
mezoTF = Entry(ablak, textvariable =varTF)
mezoTF.bind("<Return>", convCel)
mezoTF.grid(row =1, column =1)
varTF.set("212.0")

ablak.mainloop()