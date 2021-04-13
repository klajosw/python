#! /usr/bin/env python
# -*- coding: Utf-8 -*-

##################################################
#                Vibrations.py                   #
#            3 harmonikus rezgomozg�as           #
#     kiteres/ido grafikonjanak kirajzollasa     #
#                                                #
#      Szerzo : G.Swinnen (Liege, Belgium)       #
#    http://www.ulg.ac.be/cifen/inforef/swi      #
#           2002/03/16 - Licenc GPL              #
##################################################

from Tkinter import *
from math import sin, pi

##################################################
#               Oscillographe                    #
#  <Canvas> -bol  leszarmaztatott widget, a      #
#  kiteres/ido grafikon rajzolasara specializalt #
##################################################

class OscilloGraphe(Canvas):
    "Kiteres/ido gorbe rajzolasara szolgalo specializalt vaszon"
    def __init__(self, master=None, width_=200, height_=150):
        "A grafika constructora : tengelyek és vizszintes skala."
        # a szl? widget elk�z��e  :
        Canvas.__init__(self)                             # a szuloosztaly
        self.configure(width=width_, height=height_)      # constructoranak hivasa 
        self.width_, self.height_ = width_, height_       # tarolas
        # vizszintes skala rajzolasa 8 beosztassal :
        step = (width_-25)/8.          # vizszintes skala intervallumai
        for t in range(0, 9):
            stx = 10 + t*step        # +10, hogy az origotol eltavolodjunk
            self.create_line(stx, height_/10, stx, height_*9/10, fill='grey')
        # Y-tengely rajzolasa :
        self.create_line(10+4*step, height_-5, 10+4*step, 5, fill ='grey90',
                         arrow=LAST)
        # fuggoleges skala rajzolasa 5 beosztassal :
        step = height_*2/25.            # fuggoleges skala intervallumai
        for t in range(-5, 6):
            sty = height_/2 -t*step      # height_/2 hogy az origotol eltavolodjunk
            self.create_line(10, sty, width_-15, sty, fill ='grey')
        # referencia tengelyek rajzolasa :
        self.create_line(10, height_/2, width_, height_/2, fill= 'grey90',
                         arrow=LAST)    # X-tengely
        # a tengelyek vegen megadjuk a fizikai mennyisegek nevet� :
        self.create_text(20, 20, anchor =CENTER, text ="e", fill='red')
        self.create_text(width_-5, height_/2-12, anchor =CENTER, text ="t", fill='red')

    def drawCurve(self, freq=1, phase=0, ampl=10, colo='red'):
        "1 sec idotartamra eso kiteres/ido gorbe rajzolasa"
        curve =[]                       # koordinatak listaja
        step = (self.width_-25)/1000.      # az X-skala 1 sec-nak felel meg
        for t in range(0,1001,5):       # amit 1000 ms-ra osztunk fel.
            e = ampl*sin(2*pi*freq*t/1000 - phase)
            x = 10 + t*step
            y = self.height_/2 - e*self.height_/25
            curve.append((x,y))
        n = self.create_line(curve, fill=colo, smooth=1)
        return n                        # n = a rajz sorszama

##################################################
#              Classe ChoiceVibra                #
#  Az f,phi,a parameterek beallitasara szolgalo  #
#  cursor-csoportot tartalmazo widget.           #
#  A parameterek minden modositasakor egy        #
#  specialis esemeny generalodik a master widget #
#  figyelmeztetesere, ami tud ra reagalni        #
##################################################

class ChoiceVibra(Frame):
    """kurzorok egy rezges frekvenciajanak, fazisanak es amplitudojanak kivalasztasahoz"""
    def __init__(self, master=None, colo='red'):
        Frame.__init__(self)        # a szuloosztaly constructora 
        # nehany peldanyattributum definicioja :
        self.freq, self.phase, self.ampl, self.colo = 0, 0, 0, colo
        # a checkbox allapotvaltozoja :
        self.chk = IntVar()                 # Tkinter 'objektum-valtozo'
        Checkbutton(self, text='Show', variable=self.chk,
                    fg = self.colo, command=self.setCurve).pack(side=LEFT)
        # 3 cursor-widget definicioja :
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Frequency (Hz) :', from_=1., to=9., tickinterval =2,
              resolution =0.25,
              showvalue =0, command = self.setFrequency).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =15,
              label ='Phase (degree) :', from_=-180, to=180, tickinterval =90,
              showvalue =0, command = self.setPhase).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Amplitude :', from_=2, to=10, tickinterval =2,
              showvalue =0, command = self.setAmplitude).pack(side=LEFT, pady =5)

    def setCurve(self):
        self.master.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq = float(f)
        self.master.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp =float(p)
        self.phase = pp*2*pi/360        # fok -> radian atalakitas
        self.master.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.master.event_generate('<Control-Z>')

###########################
#    Foosztaly            #
###########################

class ShowVibra(Frame):
    """Harmonikus rezgomozgasok bemutatasa"""
    def __init__(self, master=None):
        Frame.__init__(self)          # a szuloosztaly constructora
        self.colour = ['green', 'yellow', 'orange']
        self.trace = [0]*3            # kirajzoland�g�b� list�a)
        self.control = [0]*3         # kontrolpanelek list�a
        # v�zonp�d�y l�rehoz�a az x � y koordin�a-tengelyekkel :
        self.gra = OscilloGraphe(self, width_ =400, height_=300)
        self.gra.configure(bg ='grey40', bd=3, relief=SUNKEN)
        self.gra.pack(side =TOP, pady=3)
        # 3 vez�l? panel (cursorok) l�rehoz�a :
        for i in range(3):
            self.control[i] = ChoiceVibra(self, self.colour[i])
            self.control[i].configure(bd =3, relief = GROOVE)
            self.control[i].pack(padx =10, pady =3)
        # Az �r� kirajzol�� ind��esem�yek defini��a :
        self.master.bind('<Control-Z>', self.showCurves)
        self.master.title('Harmonikus rezgomozgasok')
        self.pack()

    def showCurves(self, event):
        """A h�om kit��-id? grafikon (jra)kirajzol�a"""
        for i in range(3):
            # El?sz� t��jk az (esetleges) el?z? �r� :
            self.gra.delete(self.trace[i])
            # Azt� kirajzoljuk az j �r� :
            if self.control[i].chk.get():
                self.trace[i] = self.gra.drawCurve(
                                    colo=self.colour[i],
                                    freq=self.control[i].freq,
                                    phase=self.control[i].phase,
                                    ampl=self.control[i].ampl)

#### Code pour tester la classe : ###

if __name__ == '__main__':
    ShowVibra().mainloop()

#traceCourbe -> drawCurve
#height -> height_
#width -> width_
#pas -> step
#montreCourbes -> showCurves
#ChoixVibra -> ChoiceVibra
#couleur -> colour
#controle -> control