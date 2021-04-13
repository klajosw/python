#! /usr/local/bin/python2.0

def sin(x, num):
  sum = 0
  for n in range(0,num):
    sum += (-1)**n *(float(x**(2*n+1)) / factorial(2*n+1))
  return sum

from operator import mul
factorial = lambda k: reduce(mul,[1]+range(1,k+1))  

import math
diff = lambda x, num : math.sin(x) - sin(x,num)

def diffs(x,n):
  for i in range(n):
    print '%+5e %15f %15f' % (diff(x,i), sin(x,n), math.sin(x))

print diffs(0.1,6)
