#!/usr/bin/python

"""Opciók szétbontása.
 Hajtsd végre az alábbi formában:
 opciok.py --alma idared  -q kukac -r matyicd
"""
import sys, getopt

print sys.argv

# q: -q argumentumot vár bõvebben getopt.getopt.__doc__
pars= getopt.getopt(sys.argv[1:],"q:r:",['alma=', 'körte='])
print pars
