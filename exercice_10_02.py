#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def darabol(ch, n):
    "egy ch string n karakterbõl álló részekre darabolása"
    d, f = 0, n             # a részstring elejének és végének indexe
    tt = []                 # a létrehozandó string
    while d < len(ch):
        if f > len(ch):     # a végén túl nem tudunk darabolni
            f = len(ch)
        fr = ch[d:f]        # egy fragmentum kivágása
        tt.append(fr)       # a fragmentum hozzáadása a listához
        d, f = f, f +n      # a következõ indexek 
    return tt

def invertal(tt):
    "a tt lista elemeit fordított sorrendben állítja össze"
    ch = ""                 # a létrehozandó string
    i = len(tt)             # a lista végével kezdjük
    while i > 0 :
        i = i - 1           # az utolsó elem indexe n -1
        ch = ch + tt[i]
    return ch

# Teszt :
if __name__ == '__main__':
    ch ="abcdefghijklmnopqrstuvwxyz123456789"
    lista = darabol(ch, 5)
    print lista
    print invertal(lista)