#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def szoLista(ch):
    "a ch karakterláncot átalakítja szavakból álló listává"
    lista, ct = [], ""          # ct átmeneti string
    for c in ch:
        if c == " ":
            lista.append(ct)    # a listához adjuk a ch átmeneti stringet
            ct = ""             # a ch átmeneti string reinicializálása
        else:    
            ct = ct + c
    if ct != "":        
        lista.append(ct)        # ne felejtsük ki az utolsó szót      
    return lista

# Teszt :
if __name__ == '__main__':
    print szoLista("Une hirondelle ne fait pas le printemps")
    print szoLista("")
