# -*- coding:Latin-1 -*-

# D�mat�bla rajza
 
from Tkinter import *

def dama_tabla():
    "10 n�gyzetb�l �ll� sor rajzol�sa v�ltakoz� eltol�d�ssal"
    y = 0
    while y < 10:
        if y % 2 == 0:              # k�t alkalomb�l egyszer
            x = 0                   # a n�gyzetekb�l �ll� sor
        else:                       # egy n�gyzetnyi 
            x = 1                   # eltol�d�ssal fog kezd�dni
        line_of_squares(x*c, y*c)
        y += 1
        
def line_of_squares(x, y):
    "x, y -b�l kiindulva n�gyzetekb�l �ll� vonal rajzol�sa" 
    i = 0
    while i < 10:
        can.create_rectangle(x, y, x+c, y+c, fill='navy')
        i += 1
        x += c*2                    # n�gyzetes k�z�k hagy�sa
        
##### F�program : ############
    
# Pr�b�lja meg j�l "param�terezni" a programjait, ahogyan ebben a scriptben tett�k.
# A script tetsz�leges m�ret� d�mat�bl�kat rajzolhat egyetlen �rt�k,
# a n�gyzet m�ret�nek megv�ltoztat�s�val :

c = 30                  # n�gyzetek m�rete

ablak = Tk()
can = Canvas(ablak, width =c*10, height =c*10, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(ablak, text ='d�mat�bla', command =dama_tabla)
b1.pack(side =LEFT, padx =3, pady =3)
ablak.mainloop()