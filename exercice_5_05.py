#! /usr/bin/env python
# -*- coding: Latin-1 -*-

n = 1       # kocka sorsz�ma
g = 1       # az elhelyezend� b�zaszemek sz�ma
# A k�dv�ltozathoz el�g g-t <float> -k�nt defini�lni
# a fenti sort a k�vetkez�vel helyettes�tve:  g = 1.

while n < 65 :
    print n, g
    n, g = n+1, g*2
