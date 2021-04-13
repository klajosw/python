#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Fahrenheit <=> Celsius �talak�t�s

from Tkinter import *

def convFar(event):
    "a h�m�rs�klet �rt�ke Fahrenheit fokban kifejezve"
    tF = eval(mezoTC.get())
    varTF.set(str(tF*1.8 +32))

def convCel(event):
    "a h�m�rs�klet �rt�ke Celsius fokban kifejezve"
    tC = eval(mezoTF.get())
    varTC.set(str((tC-32)/1.8))

ablak = Tk()
ablak.title('Fahrenheit/Celsius')

Label(ablak, text='Temp. Celsius :').grid(row =0, column =0)
# Adatbeviteli mez�h�z asszoci�lt "Tkinter v�ltoz�". Ez az "objektum-v�ltoz�"
# biztos�tja az interface-t a TCL �s a Python k�z�tt (l�sd jegyzet, 165. oldal) :
varTC =StringVar()
mezoTC = Entry(ablak, textvariable =varTC)
mezoTC.bind("<Return>", convFar)
mezoTC.grid(row =0, column =1)
# A Tkinter v�ltoz� tartalm�nak inicializ�l�sa :
varTC.set("100.0")

Label(ablak, text='Temp. Fahrenheit :').grid(row =1, column =0)
varTF =StringVar()
mezoTF = Entry(ablak, textvariable =varTF)
mezoTF.bind("<Return>", convCel)
mezoTF.grid(row =1, column =1)
varTF.set("212.0")

ablak.mainloop()