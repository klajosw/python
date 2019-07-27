#! /usr/bin/python

""" Az argumentum�ban l�v� f�jlokb�l egy html list�t k�sz�t, �s ezt kiirja
a standard kimenetre. Ha nincs f�jln�v, az aktu�lis k�nyvt�rat list�zza.

 Ha van .bevezetes.html ill. .kiegeszites.html nev� f�jl akkor ezt a lista
el� �s m�g� illeszti.

 Haszn�lata: lista.py [fajlok]
   vagy     lista.py --help
 P�lda (unixos): lista.py *.py >ls.html

�gy k�sz�lt a 
www.szgti.kando.hu/~ahorvath/latex/dok  honlapoldal.
2001 tavasz
"""

import sys
import os
import stat
import string
import time

def hu_time(second):
    return string.lower(time.strftime("%Y. %b %d.", time.localtime(second)))

def listaz():
    # Ki�rja a html f�jl elej�t
    print """<html>
    <head>
     <meta http-equiv="Content-Type" CONTENT="text/html; charset=iso-8859-2">
     <title>Tartalomjegyz�k</title>
    </head>
    <body bgcolor="#E2FAD3">
    """
    
    #Ki�rja a bevezet�t, ha van
    allfile = os.listdir('.')
    if '.bevezetes.html' in allfile:
      bevezetes = open('.bevezetes.html')
      for sor in  bevezetes.readlines():
        print sor

    print """<p>Ebben a k�nyvt�rban a k�vetkez� f�jlok vannak:"""

    # Kiirja az argumentumban szerepl� f�jlok neveit html form�tumban
    # linket is k�sz�t hozz�juk.
    print '<table border = "2">'
    filelist = sys.argv[1:]
    if not filelist:
      filelist = os.listdir('.')
    filelist.sort()
    print '<tr> <td>N�v</td>      <td align ="right">M�ret (b�jt)</td>  <td align = "center">Utols� m�dos�t�s <br>d�tuma</td>'
    for file in filelist:
      meret = os.stat(file)[stat.ST_SIZE]
      second = os.stat(file)[stat.ST_MTIME]
      modositas_datuma = hu_time(second)
      print '<tr><td><a href="%-20s">%-20s</a></td> <td align ="right">%7d</td>  <td align ="right">%s</td>' % (file, file, meret, modositas_datuma)
    print '</table>'

    print "<p>A lista ekkor k�sz�lt:", hu_time(time.time())

    #Ki�rja a kiegeszitest, ha van
    allfile = os.listdir('.')
    if '.kiegeszites.html' in allfile:
      kiegeszites = open('.kiegeszites.html')
      for sor in  kiegeszites.readlines():
        print sor

    # A html f�jl alj�ra egy linket rak a Magyar Python Honlapra
    print """
<p>
Ez a lista egy Python programmal k�sz�lt.
<br><a href="http://www.python.hu"> Magyar Python Honlap</a>
</body>\n\
</html>"""

def keplista():
    keplist = sys.argv[1:]
    if not keplist:
	keplist = os.listdir('.')
	keplist.sort()
    for kep in keplist:
	print """<p><img src=\"%s\" alt=\"%s\">"""



if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] in ['--help', '-h', '-help']:
        print __doc__
    else:
        listaz()





