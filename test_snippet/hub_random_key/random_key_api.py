# -*- coding: utf-8 -*-

url = 'http://hub.hust.edu.cn/randomKey.action?username=U201110090&time=1387090741723'
 

import cPickle

with open('./rkey') as fi:
  try:
    li = cPickle.load(fi)
    if type(li) != type([]):
      li = [0] * 999999 + [0]
  except Exception as e:
    print e
    li = [0] * 999999 + [0]


cc = 0
for i, val in enumerate(li):
  if val:
    cc += 1
    #print i, val

print 'length:', cc

import urllib2
import json
import random


with open('./proxy.lst') as fi:
  proxies = [_.rstrip('\n') for _ in fi]

cnt = 0
scnt = len(proxies)

while 1:
  try:
    opener = urllib2.build_opener( urllib2.ProxyHandler({'http': proxies[cnt]}) )
    try:
      t = json.load( opener.open(url, timeout=5) )
    except Exception as e:
      print e
      cnt = (cnt + 1) % scnt
      continue
    print t
    if li[int(t[0])] and li[int(t[0])] != t[1]:
      print '&' * 20
      print t, li[ int(t[0]) ]
      raise Exception

    li[int(t[0])] = t[1]
  except KeyboardInterrupt:
    print 'stoped!'
    with open('./rkey', 'wb') as fi:
      cPickle.dump(li, fi)
    exit()
  except Exception as e:
    print e
    with open('./rkey', 'wb') as fi:
      cPickle.dump(li, fi)
    exit()
