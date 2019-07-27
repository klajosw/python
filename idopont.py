#!/usr/bin/python
"""
 Az idõvel kapcsolatos modulok használatára pár példa.
 Egy része magyarítva.
"""


####################
# time modul
####################
import time 

second = time.time() # 1970 jan 1. 1:00:00 után eltelt másodpercek
print "Holnap ilyenkor van:"
print time.strftime("%a, %d %b %Y %H:%M:%S %Z",
			time.localtime(second+24*3600))
#print time.strftime("%a, %d %B %Y %H:%M:%S %Z", time.localtime(second))
print
print 'Változtathatunk a kiirás módján.  Most van:'
date_hu = time.strftime("%Y. %b %d. %H:%M:%S ", time.localtime(time.time()))
print date_hu
print

import string
print "És még egy változat a string modullal."
## date_hu = time.strftime("%Y. %b %d.", time.localtime(time.time()))
## print date_hu
date_hu = string.lower(date_hu)
print date_hu

####################
# calendar modul
####################
import calendar

# Az idõpontnevek magyar megfelelõi  (abbr. = rövidítés)
calendar.day_name = ['hétfõ', 'kedd', 'szerda', 'csütörtök',
            'péntek', 'szombat', 'vasárnap']

calendar.day_abbr = ['hétf', 'kedd', 'sze', 'csüt', 'pént', 'szo', 'vas']

calendar.month_name = ['', 'Január', 'Február', 'Március', 'Április',
              'Május', 'Június', 'Július', 'Augusztus',
              'Szeptember', 'Október',  'November', 'December']

calendar.month_abbr = ['   ', 'jan', 'feb', 'márc', 'ápr', 'máj', 'jún',
              'júl', 'aug', 'szept', 'okt', 'nov', 'dec']

#print dir()

# Éves naptár

second = time.time() # 1970 jan 1. 1:00:00 után eltelt másodpercek
year = time.localtime(second)[0]
print calendar.calendar(year)

# Egy hónapos naptár
second = time.time() # 1970 jan 1. 1:00:00 után eltelt másodpercek
month = time.localtime(second)[1]
print calendar.month(year, month)

# Egy hónapos naptár. Az oszlopok szélessége 10
calendar.prmonth(year, month, w=10)

