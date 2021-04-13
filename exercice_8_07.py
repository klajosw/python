#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Olimpiai karikák  - tömör változat.

from Tkinter import *

# Az 5 karika X,Y koordinátái :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Az 5 karika színei :
colour = ["red", "yellow", "blue", "green", "black"]

base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou = Button(base, text ="Kilép", command =base.quit)
bou.pack(side = RIGHT)
# Az 5 karika rajza :
i = 0
while i < 5:
    x1, y1 = coord[i][0], coord[i][1]
    can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =colour[i])
    i = i +1
base.mainloop()