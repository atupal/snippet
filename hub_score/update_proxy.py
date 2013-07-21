#import requests
#
#proxies = {
#    'http': '58.242.249.31:10034',
#    'https': '58.242.249.31:10034',
#    }
#
#headers = {
#    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'
#    }
#
#print requests.get('http://hub.hust.edu.cn', proxies = proxies, headers = headers).content


import urllib2, random

with open('./proxy.lst') as fi:
  proxies = [_.rstrip('\n') for _ in fi]

for pro in proxies:
  opener = urllib2.build_opener( urllib2.ProxyHandler({'http': pro}) )
  #urllib2.install_opener( opener )
  try:
    opener.open('http://hub.hust.edu.cn', timeout=7).read()
    print pro
  except:
    pass
