#!/usr/bin/env python2

import cPickle

with open('./rkey.bak') as fi:
  li = cPickle.load(fi)

print li[983473]
exit()

if __name__ == '__main__':
  #import sys
  #try:
  #  print li[int(sys.argv[1])]
  #except:
  #  pass

  with open('l_rkey') as fi:
    for i in fi:
      t = i.split()[0]
      if li[int(t)]:
        print t
