#! /usr/bin/env python
# -*- coding: Utf-8 -*-

from exercice_10_08 import nagybetu
from exercice_10_10 import szoLista

txt = "Le nom de ce Monsieur est Alphonse"
lst = szoLista(txt)             # a mondatot átalakítja szavak listájává
for szo in lst:                 # a listában minden egyes szót megvizsgál
    if nagybetu(szo[0]):        # megvizsgálja a szó elsõ karakterét
        print szo
