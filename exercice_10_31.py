#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Az azonos adatok kiküszöbölése

lst = [9, 12, 40, 5, 12, 3, 27, 5, 9, 3, 8, 22, 40, 3, 2, 4, 6, 25]
lst2 = []

for el in lst:
     if el not in lst2:
          lst2.append(el)

lst2.sort()
print lst2
