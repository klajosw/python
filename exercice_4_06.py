#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Kezdő értékként megadott másodpercek száma :
# (egy nagy számot adunk meg !)
nsd = 12345678912

# Egy napra eső másodpercek száma :
nspj = 3600 * 24
# Egy évre eső másodpercek száma (365 napra -
# a szökőéveket nem vesszük figyelembe ) :
nspa = nspj * 365
# Egy hónapra eső másodpercek száma (feltételezzük,
# hogy minden hónap 30 napos) :
nspm = nspj * 30
# A megadott időtartam ennyi évet tesz ki :
na = nsd / nspa         # egészosztás 
nsr = nsd % nspa        # a maradék másodpecek száma
# A megmaradó hónapok száma :
nmo = nsr / nspm        # egészosztás 
nsr = nsr % nspm        # a maradék másodpecek száma
# A megmaradó napok száma :
nj = nsr / nspj         # egészosztás 
nsr = nsr % nspj        # a maradék másodpecek száma
# A megmaradó órák száma :
nh = nsr / 3600         # egészosztás 
nsr = nsr % 3600        # a maradék másodpecek száma
# a maradék pecek száma :
nmi = nsr /60           # egészosztás 
nsr = nsr % 60          # a maradék másodpecek száma

print "Az átalakítandó másodpercek száma :", nsd
print "Ez az időtartam", na, "évnek"
print nmo, "hónapnak,",
print nj, "napnak,",
print nh, "órának,",
print nmi, "percnek és",
print nsr, " másodpercnek felel meg."