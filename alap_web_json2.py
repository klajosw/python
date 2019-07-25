#!/usr/bin/env python2
# coding: utf-8

import urllib.request
import json
import pprint


def main():
urlData = "https://www.reddit.com/r/earthporn/.json"
  webURL = urllib.request.urlopen(urlData)
  data = webURL.read()
  encoding = webURL.info().get_content_charset('utf-8')
  dn=json.loads(data.decode(encoding))
  for dn2 in dn['data']['children']:
##    print (dn2['data']['thumbnail'])  ## kicsi kép
    print (dn2['data']['preview']['images'][0]['source']['url'])  
## k 'width': 4861, 'height'
## print (dn2['data']['preview']['images']['source']['url'])  ## kicsi kép]
  
  
# https://docs.python.org/3/library/urllib.request.html#examples
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
res = urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json')
res_body = res.read()

# https://docs.python.org/3/library/json.html
j = json.loads(res_body.decode("utf-8"))

# parse strings: 'ip_prefix' and 'region'
#for i in range(len(j['prefixes'])):
#	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
for prefix in j['prefixes']:
  print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region']))
  
 json.loads(data.decode(html1))
  dn=json.loads(html1)
  print(dn.keys)
     tml0 = response.read()
  html1 = tml0.decode("utf-8")
  print(htm11)
  pprint.pprint (tml1)
  url = "https://docs.python.org/3/_static/py.png"
  urllib.request.urlretrieve(url,"c:/tmp/mentett.png")  ## kep lementes
	

##############################################################################

if __name__ == "__main__":
    main()
