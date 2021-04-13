#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Elemek bejegyzése egy listába

tt = []             # A készítendõ lista (kezdetben üres)
ch = "start"        # valamilyen érték (nem nulla) 
while ch != "":
    print "Írjon be egy értéket : "
    ch = raw_input()
    if ch != "":
        tt.append(float(ch))        # másik változat : tt.append(ch)    

# a lista kiíratása :
print tt