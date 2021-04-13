#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Egy kis adatbázis létrehozása és feltöltése

import gadfly
import os

path_ = os.getcwd()        # aktualis konyvtar

connection = gadfly.gadfly()
connection.startup("music", path_)
cur = connection.cursor()
request = "create table zeneszerzok (eloado varchar, ev_szul integer,\
           ev_halal integer)" 
cur.execute(request)
request = "create table muvek (eloado varchar, cim varchar,\
           ido integer, interpr varchar)" 
cur.execute(request)

print "Bevitt adatok kiirasa a zeneszerzok adattablaba :"
while 1:
    nv = raw_input("Zeneszerzo neve (<Enter> befejezes) : ")
    if nm =='':
        break
    esz = raw_input("Szuletes eve : ")
    eha = raw_input("Halal eve : ")
    request ="insert into zeneszerzok(eloado, ev_szul, ev_halal) values \
                 ('%s', %s, %s)" % (nv, esz, eha)
    cur.execute(request)
# Ellenorzeskent kiirja a bevitt adatokat :
cur.execute("select * from zeneszerzok")
print cur.pp()

print "Bevitt adatok rögzitese a muvek adattablaba :"
while 1:
    nev_ = raw_input("Zeneszerzo neve (<Enter> befejezes) : ")
    if nev_ =='':
        break
    cim_ = raw_input("Zenemu cime : ")
    ido_ = raw_input("idotartam (perc) : ")
    int = raw_input("eloado : ")
    request ="insert into muvek(eloado, cim, ido, interpr) values \
                 ('%s', '%s', %s, '%s')" % (nev_, cim_, ido_, int)
    cur.execute(request)
# Ellenorzeskent kiirja a bevitt adatokat :
cur.execute("select * from muvek")
print cur.pp()

connection.commit()