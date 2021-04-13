#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Egy szövegben elõforduló betûk elõfordulási gyakoriságának hisztogramja

nFile = raw_input('Filenev : ')
fi = open(nFile, 'r')
text = fi.read()		# a file átalakítása karakterlánccá
fi.close()

print text
dico ={}
for c in text:
    c = c.upper()		# minden betût nagybetûvé alakít
    dico[c] = dico.get(c, 0) +1

list = dico.items()
list.sort()
print list