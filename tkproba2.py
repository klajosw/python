#!/usr/bin/python1.5

from Tkinter import *

import time

class App:

           def __init__(self, master):

               frame = Frame(master)
               frame.pack()

               self.greeting = Label(frame, text= 'Menü')
               self.greeting.pack(side=LEFT)

##                self.image = Label(frame, image= 'next.png')
##                self.image.pack(side=LEFT)

               self.button = Button(frame, text="KILÉP", fg="red", bg="yellow", command=frame.quit)
               self.button.pack(side=LEFT)
               #print str(self.button)

               self.time = Button(frame, text="Idõ", command=self.time)
               self.time.pack(side=RIGHT)

               self.hi = Button(frame, text="Szia", command=self.hi)
               self.hi.pack(side=LEFT)

           def time(self):
               print time.asctime(time.gmtime(time.time()))

           def hi(self):
               print 'Szia felhasználó!'


root = Tk()

app = App(root)

## app2 = App(root)

## def hi():
##     print 'Szia felhasználó!'

## frame = Frame(root)
## frame.pack()
## app2.hi = Button(frame, text="Szia", command=hi)
## app2.hi.pack(side=LEFT)

root.mainloop()
