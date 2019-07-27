#! /usr/bin/python

from re import search, match

print search('a', 'mamia').span()
#print match('a', 'mamia').span()
print match('a', 'amia').span()
print search('ma*d?', 'maaaaaadmiad').group()
print search('a', 'mamia').span()



print search('[aA]*?A', 'aaAaaA').group()
print search('[aA]*A', 'aaAaaA').group()

print search('[\t]*A', 'aaAaa		A').group()
