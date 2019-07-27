#! /usr/bin/python

""" Az argumentumában lévő fájlokból egy html listát készít, és ezt kiirja
a standard kimenetre. Ha nincs fájlnév, az aktuális könyvtárat listázza.

 Ha van .bevezetes.html ill. .kiegeszites.html nevű fájl akkor ezt a lista
elé és mögé illeszti.

 Használata: lista.py [fajlok]
   vagy     lista.py --help
 Példa (unixos): lista.py *.py >ls.html

Így készült a 
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
    # Kiírja a html fájl elejét
    print """<html>
    <head>
     <meta http-equiv="Content-Type" CONTENT="text/html; charset=iso-8859-2">
     <title>Tartalomjegyzék</title>
    </head>
    <body bgcolor="#E2FAD3">
    """
    
    #Kiírja a bevezetőt, ha van
    allfile = os.listdir('.')
    if '.bevezetes.html' in allfile:
      bevezetes = open('.bevezetes.html')
      for sor in  bevezetes.readlines():
        print sor

    print """<p>Ebben a könyvtárban a következő fájlok vannak:"""

    # Kiirja az argumentumban szereplő fájlok neveit html formátumban
    # linket is készít hozzájuk.
    print '<table border = "2">'
    filelist = sys.argv[1:]
    if not filelist:
      filelist = os.listdir('.')
    filelist.sort()
    print '<tr> <td>Név</td>      <td align ="right">Méret (bájt)</td>  <td align = "center">Utolsó módosítás <br>dátuma</td>'
    for file in filelist:
      meret = os.stat(file)[stat.ST_SIZE]
      second = os.stat(file)[stat.ST_MTIME]
      modositas_datuma = hu_time(second)
      print '<tr><td><a href="%-20s">%-20s</a></td> <td align ="right">%7d</td>  <td align ="right">%s</td>' % (file, file, meret, modositas_datuma)
    print '</table>'

    print "<p>A lista ekkor készült:", hu_time(time.time())

    #Kiírja a kiegeszitest, ha van
    allfile = os.listdir('.')
    if '.kiegeszites.html' in allfile:
      kiegeszites = open('.kiegeszites.html')
      for sor in  kiegeszites.readlines():
        print sor

    # A html fájl aljára egy linket rak a Magyar Python Honlapra
    print """
<p>
Ez a lista egy Python programmal készült.
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





