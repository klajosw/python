#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Két szövegfile kombinálása egy új szövegfile-lá

fichA = raw_input("Az 1. file neve : ")
fichB = raw_input("A 2. file neve : ")
fichC = raw_input("A célfile neve : ")
fiA = open(fichA, 'r')
fiB = open(fichB, 'r')
fiC = open(fichC, 'w')

while 1:
    lineA = fiA.readline()    
    lineB = fiB.readline()
    if lineA =="" and lineB =="":
        break               # Elértük a két file végét
    if lineA != "":
        fiC.write(lineA)
    if lineB != "":    
        fiC.write(lineB)

fiA.close()
fiB.close()
fiC.close()