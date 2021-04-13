#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# ASCII kódtábázat

c = 32      # Elsõ <nyomtatható> ASCII

while c < 128 :                 # csak az ékezet nélküli karakterek 
    print "Kód", c, ":", chr(c), "  "
    c = c + 1
