# -*- coding: utf-8 -*-
'''
  author: atupal
  2013.7.21
'''
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
import requests
import lxml.html

def update_proxy():
  url = 'http://proxy.ipcn.org/proxylist.html'
  fi = open('./proxy.lst.ts', 'w')
  try:
    resp = requests.get(url, headers = {
      'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'
      })
    xparser = lxml.html.fromstring(resp.content)
    ret = xparser.xpath("//pre/text()")
    fi.write(ret[0][90:].strip().strip().encode('utf-8', errors=""))
  except:
    import traceback, sys
    print '\033[33m'
    traceback.print_exc(file = sys.stdout)
    print '\033[31m %s' % 'failed! please retri!'
  fi.close()


def get_good_proxy():
  with open('./proxy.lst') as fi:
    proxies = [_.rstrip('\n') for _ in fi]

  good_proxy = []
  for pro in proxies:
    opener = urllib2.build_opener( urllib2.ProxyHandler({'http': pro}) )
    #urllib2.install_opener( opener )
    try:
      opener.open('http://hub.hust.edu.cn', timeout=7).read()
      good_proxy.append(pro)
    except:
      pass
  with open('./proxy.lst', 'w') as fi:
    for pro in good_proxy:
      fi.write("%s\n" % pro)


if __name__ == "__main__":
  update_proxy()
  #get_good_proxy()
