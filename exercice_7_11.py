#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def honapNev(n):
    "az év n-edik hónapjának nevét adja meg"
    mois = ['Január,', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július',
            'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    return mois[n -1]       # az indexek számozása nullával kezdõdik

# teszt :
print honapNev(4)
