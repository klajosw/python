#!/usr/bin/python

"""Opci�k sz�tbont�sa.
 Hajtsd v�gre az al�bbi form�ban:
 opciok.py --alma idared  -q kukac -r matyicd
"""
import sys, getopt

print sys.argv

# q: -q argumentumot v�r b�vebben getopt.getopt.__doc__
pars= getopt.getopt(sys.argv[1:],"q:r:",['alma=', 'k�rte='])
print pars
