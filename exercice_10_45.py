#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def consult():
    while 1:
        name = raw_input("Irja be a nevet (vagy <enter> a kilepeshez) : ")
        if name == "":
            break
        if dico.has_key(name):           # a szótárban szerepel a név ?
            item = dico[name]            # megnézzük
            age, height = item[0], item[1]
            print "Név : %s - kor : %s ans - magasság : %s m."\
                   % (name, age, height)          
        else:
            print "*** ismeretlen név ! ***"

def fill():
    while 1:
        name = raw_input("Irja be a nevet (vagy <enter> a kilepeshez) : ")
        if name == "":
            break
        age = int(raw_input("Irja be az eletkort (egesz szam !) : "))
        height = float(raw_input("Irja be a testmagassagot (meterben) : "))
        dico[name] = (age, height)

dico ={}
while 1:
    choice = raw_input("Valasszon : (K)itolt - (M)egnez - (V)ege : ")
    if choice.upper() == 'V':
        break
    elif choice.upper() == 'K':
        fill()
    elif choice.upper() == 'M':
        consult()