#! /usr/bin/env python
# -*- coding: Utf-8 -*-

def nagybetu(car):
    "<igaz> a visszatérési értéke, ha a car nagybetû"
    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return 1
    else:
        return 0

# Test :
if __name__ == '__main__':
    print nagybetu('d'), nagybetu('F')