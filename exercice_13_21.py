#! /usr/bin/env python
# -*- coding: Utf-8 -*-

##################################################
#                 Colordic.py                    #
#      Auteur : G.Swinnen (Li�e, Belgium)       #
#    http://www.ulg.ac.be/cifen/inforef/swi      #
#           21/07/2004 - Licence GPL             #
##################################################

from Tkinter import *
# A modul diszken levo file-ok keresesere szolgalo 
# standard dialogbox-okat allit elo :
from tkFileDialog import asksaveasfile, askopenfile

class Application(Frame):
    '''Alkalmazasablak'''
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Színszótár létrehozása")

        self.dico ={}       # szotar letrehozasa

        # A widget-ek ket keretben (Frame) vannak csoportositva : 
        frUpp =Frame(self)      # 6 widget -et tartalmazo felso frame 
        Label(frUpp, text ="Szín neve :",
              width =20).grid(row =1, column =1)
        self.enName =Entry(frUpp, width =25)        # adatbeviteli mezo
        self.enName.grid(row =1, column =2)         # a szinnek
        Button(frUpp, text ="Már létezik ?", width =12,
               command =self.searchColour).grid(row =1, column =3)
        Label(frUpp, text ="Megf. hexa kód :",
              width =20).grid(row =2, column =1)
        self.enCode =Entry(frUpp, width =25)        # adatbeviteli mezo
        self.enCode.grid(row =2, column =2)         # a hexakodnak
        Button(frUpp, text ="Teszt", width =12,
               command =self.testColour).grid(row =2, column =3)
        frUpp.pack(padx =5, pady =5)
        
        frLow =Frame(self)      # a maradekot tartalmazo also frame
        self.test = Label(frLow, bg ="white", width =45,    # tesztzona
                          height =7, relief = SUNKEN)
        self.test.pack(pady =5)   
        Button(frLow, text ="A szín hozzáadása a szótárhoz",
               command =self.addColour).pack()
        Button(frLow, text ="Szótár kiírása", width =25,
               command =self.record).pack(side = LEFT, pady =5)
        Button(frLow, text ="Szótár visszaállítása", width =25,
               command =self.restore).pack(side =RIGHT, pady =5)
        frLow.pack(padx =5, pady =5)
        self.pack()        
        
    def addColour(self):
        "az aktualis szin hozzaadasa a szotarhoz"
        if self.testColour() ==0:        # volt definialva szin ?
            return       
        name = self.enName.get()
        if len(name) >1:                 # elutasitja a tul rovid nevet
            self.dico[name] =self.cHexa
        else:
            self.test.config(text ="%s : inkorrekt nev" % name, bg ='white') 

    def searchColour(self):
        "egy a szotarba mar beirt szin keresese"
        name = self.enName.get()
        if self.dico.has_key(name):
            self.test.config(bg =self.dico[name], text ="")
        else:
            self.test.config(text ="%s : ismeretlen szin" % name, bg ='white') 
    
    def testColour(self):
        "hexakod ervenyessegenek igazolasa. - a megfelelo szin kiirasa."
        try:
            self.cHexa =self.enCode.get()
            self.test.config(bg =self.cHexa, text ="")
            return 1
        except:
            self.test.config(text ="Inkorrekt szin kodolasa", bg ='white')
            return 0

    def record(self):
        "szotar kiirasa szovegfile-ba"
        # Ez a metodus egy standard dialogbox-ot alkalmaz a diszken levo file
        # kivalasztasara. A Tkinter a tkFileDialog modulban egy sor fggv�yt ad, amik ezekhez a 
        # dialogbox-okhoz vannak asszocialva.
        # Az alabbi fuggveny egy irasra megnyitott file-objektumot ad visszateresi erteknek :
        ofi =asksaveasfile(filetypes=[("Szöveg",".txt"),("Minden","*")]) 
        for key, value in self.dico.items():
            ofi.write("%s %s\n" % (key, value))
        ofi.close()

    def restore(self):
        "szotar visszaallitasa tarolt filebol"
        # Az alabbi fuggveny egy olvasasra megnyitott file-objektumot ad visszateresi erteknek :
        ofi =askopenfile(filetypes=[("Szöveg",".txt"),("Minden","*")]) 
        lignes = ofi.readlines()
        for li in lignes:
            cv = li.split()     # a megfelelo kulcs es ertek kiszedese
            self.dico[cv[0]] = cv[1]
        ofi.close()

if __name__ == '__main__':
    Application().mainloop()

#frSup ->frUpp
#frInf ->frLow
#clef ->key
#Nom -> Name
#ajouteCoul -> addColour
#restaure -> restore
#enregistre -> record
#valeur -> value
#chercheCoul -> searchColour
#testeCoul -> testColour