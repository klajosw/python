#! /usr/bin/python

from cmath import *
# a matekos f�ggv�nyeket "behozza" az el�z� sor
# math: val�s f�ggv�nyek, cmath: komplex f�ggv�nyek
# Ha minden igaz, az ut�bbi ugyan�gy m�k�dik val�sakra, 
# mint a math-�, csak ki�rja a komplex r�szt is, ha nulla is,
# �s nem jelez hib�t, amikor az erdm�ny komplex.
# A * azt jelenti, hogy minden f�ggv�nyt haszn�lhatunk

print 'A log(-1) �rt�ke  (komplex)',
print log(-1)  ,"(ennek nincs val�s �rt�ke, de komplex van)\n"
print 'sin(pi/3) �rt�ke' ,sin(pi/3), '(Ez val�s, de komplex alakban �rja, mivel a cmath-ot haszn�ljuk.)\n'

def cDescartes(r, fi):
 "Ez egy �j f�ggv�ny, amely pol�rkooordin�t�kat Descartes-be sz�mol\
 (a fi radi�nban)"
 return r*cos(fi), r*sin(fi)

# Haszn�ljuk az �j f�ggv�nyt!
print "cDescartes(5, pi/4):",
print cDescartes(5, pi/4)
print 'Ez �gy a komplex r�szt is ki�rja.\n'

# Haszn�ljuk a math k�nyvt�r f�ggv�nyeit!
import math # ha ilyen form�ban hozom be a math f�ggv�nyeit
		# a f�ggv�nyn�v el� mind�g kell a 'math.'
print 'sin(pi/4):',sin(pi/4)
print 'math.sin(pi/4):',math.sin(pi/4), '\n'

def Descartes(r, fi):
 "Ez egy �j f�ggv�ny, amely pol�rkooordin�t�kat Descartes-be sz�mol\
 (a fi radi�nban), az eredm�ny val�s"
 return r*math.cos(fi), r*math.sin(fi)

# Haszn�ljuk az ezt a f�ggv�nyt is!
print "Descartes(5, pi/4):",
print Descartes(5, pi/4)
print "Ez m�r val�s.\n"


####################
# Vektori szorzat
####################

def szoroz(v1, v2):
    "Vektorokat szoroz �ssze."
    if len(v1) != len(v2):
        raise ValueError, 'k�l�nb�z� hossz�s�g� vektorok'
    # Elk�sz�ti a megfelel� tagok szorzatait
    tagok = [v1[i]*v2[i] for i in range(len(v1))]
    # �sszeadja a megkapott tagokat
    return reduce(lambda x,y: x+y,   tagok)

print 'Vektori szorzat'
v1 = [1,2,3,20]
v2 = [1,5,0,5]
print '%s * %s = %d' % (`v1`,`v2`,szoroz(v1, v2))
print

v2 = [1,1]
print '%s * %s =' % (`v1`,`v2`),
print szoroz(v1, v2)

