#!/usr/bin/env python2
# coding: utf-8

import urllib.request
import json
import pprint


def main():
  with urllib.request.urlopen('http://python.org/') as response:
     tml = response.read()
  html1 = tml.decode("utf-8")
  pprint.pprint (html1)
  url = "https://docs.python.org/3/_static/py.png"
  urllib.request.urlretrieve(url,"c:/tmp/mentett.png")  ## kep lementes
	

##############################################################################

if __name__ == "__main__":
    main()
