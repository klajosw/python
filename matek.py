#! /usr/bin/python

from cmath import *
# a matekos függvényeket "behozza" az elõzõ sor
# math: valós függvények, cmath: komplex függvények
# Ha minden igaz, az utóbbi ugyanúgy mûködik valósakra, 
# mint a math-é, csak kiírja a komplex részt is, ha nulla is,
# és nem jelez hibát, amikor az erdmény komplex.
# A * azt jelenti, hogy minden függvényt használhatunk

print 'A log(-1) értéke  (komplex)',
print log(-1)  ,"(ennek nincs valós értéke, de komplex van)\n"
print 'sin(pi/3) értéke' ,sin(pi/3), '(Ez valós, de komplex alakban írja, mivel a cmath-ot használjuk.)\n'

def cDescartes(r, fi):
 "Ez egy új függvény, amely polárkooordinátákat Descartes-be számol\
 (a fi radiánban)"
 return r*cos(fi), r*sin(fi)

# Használjuk az új függvényt!
print "cDescartes(5, pi/4):",
print cDescartes(5, pi/4)
print 'Ez így a komplex részt is kiírja.\n'

# Használjuk a math könyvtár függvényeit!
import math # ha ilyen formában hozom be a math függvényeit
		# a függvénynév elé mindíg kell a 'math.'
print 'sin(pi/4):',sin(pi/4)
print 'math.sin(pi/4):',math.sin(pi/4), '\n'

def Descartes(r, fi):
 "Ez egy új függvény, amely polárkooordinátákat Descartes-be számol\
 (a fi radiánban), az eredmény valós"
 return r*math.cos(fi), r*math.sin(fi)

# Használjuk az ezt a függvényt is!
print "Descartes(5, pi/4):",
print Descartes(5, pi/4)
print "Ez már valós.\n"


####################
# Vektori szorzat
####################

def szoroz(v1, v2):
    "Vektorokat szoroz össze."
    if len(v1) != len(v2):
        raise ValueError, 'különbözõ hosszúságú vektorok'
    # Elkészíti a megfelelõ tagok szorzatait
    tagok = [v1[i]*v2[i] for i in range(len(v1))]
    # összeadja a megkapott tagokat
    return reduce(lambda x,y: x+y,   tagok)

print 'Vektori szorzat'
v1 = [1,2,3,20]
v2 = [1,5,0,5]
print '%s * %s = %d' % (`v1`,`v2`,szoroz(v1, v2))
print

v2 = [1,1]
print '%s * %s =' % (`v1`,`v2`),
print szoroz(v1, v2)

