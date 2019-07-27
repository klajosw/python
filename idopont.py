#!/usr/bin/python
"""
 Az id�vel kapcsolatos modulok haszn�lat�ra p�r p�lda.
 Egy r�sze magyar�tva.
"""


####################
# time modul
####################
import time 

second = time.time() # 1970 jan 1. 1:00:00 ut�n eltelt m�sodpercek
print "Holnap ilyenkor van:"
print time.strftime("%a, %d %b %Y %H:%M:%S %Z",
			time.localtime(second+24*3600))
#print time.strftime("%a, %d %B %Y %H:%M:%S %Z", time.localtime(second))
print
print 'V�ltoztathatunk a kiir�s m�dj�n.  Most van:'
date_hu = time.strftime("%Y. %b %d. %H:%M:%S ", time.localtime(time.time()))
print date_hu
print

import string
print "�s m�g egy v�ltozat a string modullal."
## date_hu = time.strftime("%Y. %b %d.", time.localtime(time.time()))
## print date_hu
date_hu = string.lower(date_hu)
print date_hu

####################
# calendar modul
####################
import calendar

# Az id�pontnevek magyar megfelel�i  (abbr. = r�vid�t�s)
calendar.day_name = ['h�tf�', 'kedd', 'szerda', 'cs�t�rt�k',
            'p�ntek', 'szombat', 'vas�rnap']

calendar.day_abbr = ['h�tf', 'kedd', 'sze', 'cs�t', 'p�nt', 'szo', 'vas']

calendar.month_name = ['', 'Janu�r', 'Febru�r', 'M�rcius', '�prilis',
              'M�jus', 'J�nius', 'J�lius', 'Augusztus',
              'Szeptember', 'Okt�ber',  'November', 'December']

calendar.month_abbr = ['   ', 'jan', 'feb', 'm�rc', '�pr', 'm�j', 'j�n',
              'j�l', 'aug', 'szept', 'okt', 'nov', 'dec']

#print dir()

# �ves napt�r

second = time.time() # 1970 jan 1. 1:00:00 ut�n eltelt m�sodpercek
year = time.localtime(second)[0]
print calendar.calendar(year)

# Egy h�napos napt�r
second = time.time() # 1970 jan 1. 1:00:00 ut�n eltelt m�sodpercek
month = time.localtime(second)[1]
print calendar.month(year, month)

# Egy h�napos napt�r. Az oszlopok sz�less�ge 10
calendar.prmonth(year, month, w=10)

