#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Egyszerű szövegszerkesztő

def sansDC(ch):
    "a ch karakterláncot adja vissza az utolsó karaktere nélkül"
    uj = ""
    i, j = 0, len(ch) -1
    while i < j:
        uj = uj + ch[i]
        i = i + 1
    return uj

def fileba_ir():
    of = open(nameF, 'a')
    while 1:
        line = raw_input("Irjon be egy szovegsort (vagy <Enter>) : ")
        if line == '':
            break
        else:
            of.write(line + '\n')
    of.close()

def filebol_olvas():
    of = open(nameF, 'r')
    while 1:
        line = of.readline()
        if line == "":
            break
        # kiíratás az utolsó karakter figyelmen kívül hagyásával (= sorvége) :
        print sansDC(line)
    of.close()

nameF = raw_input('A kezelendo file neve : ')
choice = raw_input('Irjon be "i" -t irashoz, "o" -t olvasashoz : ')

if choice =='i':
    fileba_ir()
else:
    filebol_olvas()
