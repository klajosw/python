#!/usr/bin/env python2
# coding: utf-8

import urllib.request
import json
import pprint


def main():
  urlData = "https://www.reddit.com/r/earthporn/.json"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=25&after=t3_acvbop"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=50&after=t3_acx8u7"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=75&after=t3_acwich"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=100&after=t3_acqu9f"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=125&after=t3_acts6o"
##  urlData = "https://www.reddit.com/r/EarthPorn/.json?count=150&after=t3_acnf8m"
  webURL = urllib.request.urlopen(urlData)
  data = webURL.read()
  encoding = webURL.info().get_content_charset('utf-8')
  dn=json.loads(data.decode(encoding))
  a1 = 1
  for dn2 in dn['data']['children']:
    a1 += 1
    print  (dn2['data']['url'])
    aaa = (dn2['data']['url'])
    urllib.request.urlretrieve(aaa,"c:/tmp/kep20191106"+str(a1)+".jpg")
    
    
##    print (dn2['data']['thumbnail'])  ## kicsi kép
##    print  ((dn2['data']['preview']['images'][0]['source']['url']))  
##    limkem = dn2['data']['preview']['images'][0]['source']['url']
## k 'width': 4861, 'height'
## print (dn2['data']['preview']['images']['source']['url'])  ## kicsi kép]
    
  

##############################################################################

if __name__ == "__main__":
    main()
