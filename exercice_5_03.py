#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# °Fahrenheit <-> °Celsius átalakítás

# A) °C -ban megadott hõmérséklet :
tempC = 25
# Átalakítás °Fahrenheit-ba :
tempF = tempC * 1.8 + 32
# Kiíratás :
print tempC, "°C =", tempF, "°F"

# B) °F -ban megadott hõmérséklet :
tempF = 25
# Átalakítás °Celsius-ba :
tempC = (tempF - 32) / 1.8
# Kiíratás :
print tempF, "°F =", tempC, "°C"
