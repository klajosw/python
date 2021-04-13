#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# karakterláncokra vonatkozó függvények modulja

def nagybetu(car):
    "visszatérési értéke <igaz> ha a car nagybetu"
    if car >= "A" and car <= "Z":
        return 1
    else:
        return 0
    
def kisbetu(car):
    "visszatérési értéke <igaz> ha a car kisbetu"
    if car >= "a" and car <= "z":
        return 1
    else:
        return 0

def alphab(car):
    "visszatérési értéke <igaz> ha a car az abc egy betûje"
    if nagybetu(car) or kisbetu(car):
        return 1
    else:
        return 0     

# Teszt :
if __name__ == '__main__':
        print nagybetu('d'), nagybetu('F')
        print kisbetu('d'), kisbetu('F')
        print alphab('q'), alphab('P'), alphab('5')