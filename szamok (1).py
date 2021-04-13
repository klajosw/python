#!/usr/bin/python
""" szamok modul 
  A számokat követõ hangrendfüggõ ragok kezeléséhez ad segítséget.

  Horváth Árpád, ahorvath@szgti.bmf.hu, 2001."""

import string

def hangrend(n):
  """ hangrend(n) --> (típus, változat)

    Az n egész számot követõ rag hangrendjét adja vissza:
      típus - 'magas','mély','változó'
      változat - ezek különbözõ ragú csoportjai

	('magas', 1)  pl. 7-es -szer -nek -én
	('magas', 2)      5-ös! -ször!  
	('magas', 3)      1-jén!
    
	('mély', 1)  pl. 3-as -szor -nak -án
	('mély', 2)  6-os!

	('változó', 1)  2-án  2-szer"""

  try: string.atoi(`n`)  # Megvizsgálom, egész-e.
  except ValueError: raise ValueError, 'not integer'

  if n < 0:
    n = -n

  if n % 1000000 == 0:  #millió milliárd trillió...
    return ('mély', 1)
  
  if n % 1000 == 0:
    return ('magas', 1)

  if n % 100 == 0:
    return ('mély', 1)

  if n % 10 == 0:   # Tízzel osztahtó
    vege = n % 100  # Utolsó két számjegy
    if vege in [10, 40, 50, 70, 90]:
      return ('magas', 1)
    else:  return ('mély', 1)

  if n == 1:
    return ('magas', 3)

  if n == 2:
    return ('változó', 1)

  vege = n % 10   # Utolsó számjegy
  if vege == 5: return ('magas', 2)
  if vege == 6: return ('mély', 2)
  if vege in [1, 2, 4, 7, 9]:
    return ('magas', 1)
  else: return ('mély', 1)

def ragos(n, rag):
  """ragos(n, rag) --> ragos_szám
  Ragozza a számot. 
  pl.  a ragos(6, 'szer') eredménye '6-szor'.
  A rag az e (é) betûs alakkal adható meg:
  'szer','es','nek','nél','én','e'"""

  alap_ragok = ['szer','es','nek','nél','én','e']
  
  ragok = {}
  ragok[('magas', 1)] = ['szer','es','nek','nél','én','e']
  ragok[('magas', 2)] = ['ször','ös','nek','nél','én','e']
  ragok[('magas', 3)] = ['szer','es','nek','nél','jén','e']

  ragok[('mély', 1)] = ['szor','as','nak','nál','án','a']
  ragok[('mély', 2)] = ['szor','os','nak','nál','án','a']

  ragok[('vegyes', 1)] = ['szer','es','nek','nél','án','a'] 

  if rag in alap_ragok:
    sorszam = alap_ragok.index(rag)
    kulcs = hangrend(n)
    rag = ragok[kulcs][sorszam]
    return `n` + '-' + ragok[kulcs][sorszam]
  else:
    raise ValueError, 'a rag értéke hibás'

import time
def test():
  """ Ez a tesztfüggvény indul el, ha közvetlenül futtatjuk a fájlt."""
  
  for n in [1025, 3, 7]: 
    print '%d %s hangrendû.' % (n, hangrend(n)[0])
  print

  print ragos(6, 'szer'), ragos(1, 'én'), ragos(5, 'es'), ragos(1000000, 'nek')
  print

  ido = time.localtime(time.time())
  napsorszam = ido[2]
  print 'Ma %s van.' % ragos(napsorszam, 'e')

if __name__ == '__main__':
  test()
