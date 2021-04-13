#!/usr/bin/python
""" szamok modul 
  A sz�mokat k�vet� hangrendf�gg� ragok kezel�s�hez ad seg�ts�get.

  Horv�th �rp�d, ahorvath@szgti.bmf.hu, 2001."""

import string

def hangrend(n):
  """ hangrend(n) --> (t�pus, v�ltozat)

    Az n eg�sz sz�mot k�vet� rag hangrendj�t adja vissza:
      t�pus - 'magas','m�ly','v�ltoz�'
      v�ltozat - ezek k�l�nb�z� rag� csoportjai

	('magas', 1)  pl. 7-es -szer -nek -�n
	('magas', 2)      5-�s! -sz�r!  
	('magas', 3)      1-j�n!
    
	('m�ly', 1)  pl. 3-as -szor -nak -�n
	('m�ly', 2)  6-os!

	('v�ltoz�', 1)  2-�n  2-szer"""

  try: string.atoi(`n`)  # Megvizsg�lom, eg�sz-e.
  except ValueError: raise ValueError, 'not integer'

  if n < 0:
    n = -n

  if n % 1000000 == 0:  #milli� milli�rd trilli�...
    return ('m�ly', 1)
  
  if n % 1000 == 0:
    return ('magas', 1)

  if n % 100 == 0:
    return ('m�ly', 1)

  if n % 10 == 0:   # T�zzel osztaht�
    vege = n % 100  # Utols� k�t sz�mjegy
    if vege in [10, 40, 50, 70, 90]:
      return ('magas', 1)
    else:  return ('m�ly', 1)

  if n == 1:
    return ('magas', 3)

  if n == 2:
    return ('v�ltoz�', 1)

  vege = n % 10   # Utols� sz�mjegy
  if vege == 5: return ('magas', 2)
  if vege == 6: return ('m�ly', 2)
  if vege in [1, 2, 4, 7, 9]:
    return ('magas', 1)
  else: return ('m�ly', 1)

def ragos(n, rag):
  """ragos(n, rag) --> ragos_sz�m
  Ragozza a sz�mot. 
  pl.  a ragos(6, 'szer') eredm�nye '6-szor'.
  A rag az e (�) bet�s alakkal adhat� meg:
  'szer','es','nek','n�l','�n','e'"""

  alap_ragok = ['szer','es','nek','n�l','�n','e']
  
  ragok = {}
  ragok[('magas', 1)] = ['szer','es','nek','n�l','�n','e']
  ragok[('magas', 2)] = ['sz�r','�s','nek','n�l','�n','e']
  ragok[('magas', 3)] = ['szer','es','nek','n�l','j�n','e']

  ragok[('m�ly', 1)] = ['szor','as','nak','n�l','�n','a']
  ragok[('m�ly', 2)] = ['szor','os','nak','n�l','�n','a']

  ragok[('vegyes', 1)] = ['szer','es','nek','n�l','�n','a'] 

  if rag in alap_ragok:
    sorszam = alap_ragok.index(rag)
    kulcs = hangrend(n)
    rag = ragok[kulcs][sorszam]
    return `n` + '-' + ragok[kulcs][sorszam]
  else:
    raise ValueError, 'a rag �rt�ke hib�s'

import time
def test():
  """ Ez a tesztf�ggv�ny indul el, ha k�zvetlen�l futtatjuk a f�jlt."""
  
  for n in [1025, 3, 7]: 
    print '%d %s hangrend�.' % (n, hangrend(n)[0])
  print

  print ragos(6, 'szer'), ragos(1, '�n'), ragos(5, 'es'), ragos(1000000, 'nek')
  print

  ido = time.localtime(time.time())
  napsorszam = ido[2]
  print 'Ma %s van.' % ragos(napsorszam, 'e')

if __name__ == '__main__':
  test()
