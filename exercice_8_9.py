# -*- coding:Latin-1 -*-

# Dámatábla rajza
 
from Tkinter import *

def dama_tabla():
    "10 négyzetbõl álló sor rajzolása váltakozó eltolódással"
    y = 0
    while y < 10:
        if y % 2 == 0:              # két alkalomból egyszer
            x = 0                   # a négyzetekbõl álló sor
        else:                       # egy négyzetnyi 
            x = 1                   # eltolódással fog kezdõdni
        line_of_squares(x*c, y*c)
        y += 1
        
def line_of_squares(x, y):
    "x, y -ból kiindulva négyzetekbõl álló vonal rajzolása" 
    i = 0
    while i < 10:
        can.create_rectangle(x, y, x+c, y+c, fill='navy')
        i += 1
        x += c*2                    # négyzetes közök hagyása
        
##### Fõprogram : ############
    
# Próbálja meg jól "paraméterezni" a programjait, ahogyan ebben a scriptben tettük.
# A script tetszõleges méretû dámatáblákat rajzolhat egyetlen érték,
# a négyzet méretének megváltoztatásával :

c = 30                  # négyzetek mérete

ablak = Tk()
can = Canvas(ablak, width =c*10, height =c*10, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(ablak, text ='dámatábla', command =dama_tabla)
b1.pack(side =LEFT, padx =3, pady =3)
ablak.mainloop()