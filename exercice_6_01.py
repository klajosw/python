#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# mérföld/h átalakítása km/h és m/s -má

print "Írja be az óránként megtett mérföldek számát : ",
ch = raw_input()            # általában az input() helyett ezt preferáljuk
mph = float(ch)             # string átalakítása valós számmá
mps = mph * 1609 / 3600     # átalakítás m/sec -má
kmph = mph * 1.609          # átalakítás km/h -vá

# Kiíratás :
print mph, "mérföld/h =", kmph, "km/h, vagy", mps, "m/s"