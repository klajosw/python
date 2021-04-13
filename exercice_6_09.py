#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Szökõévek

print "Adjon meg egy évszámot :",
a = input()

if a % 4 != 0:
    # a nem osztható 4-gyel -> nem szökõév
    bs = 0      
else:
    if a % 400 ==0:
        # a osztható 400-zal -> szökõév
        bs = 1
    elif a % 100 ==0:
        # a osztható 100-zal -> nem szökõév
        bs = 0
    else:
        # más esetek, amikor a est osztható 4 -> szökõév
        bs = 1
if bs ==1:
    ch = "szökõév"
else:
    ch = "nem szökõév"
print a, ch

########### (Alex Misbah által javasolt változat) : #####

a = input('Adjon meg egy évszámot :')

if (a%4==0) and ((a%100!=0) or (a%400==0)):
    print a,"szökõév"
else:
    print a,"nem szökõév"