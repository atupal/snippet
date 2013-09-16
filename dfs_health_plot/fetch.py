#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import logging
import unittest
import re
import matplotlib
from pylab import *
import time

urls = ['http://10.2.201.70:32201/dfshealth.jsp', 'http://10.2.201.70:32201/dfshealth.jsp']

def get():
  for url in urls:
    content = None
    try:
      content = requests.get(url).content
    except Exception as e:
      logging.error(str(e))
    if '(active)' in content:
      return content
  logging.error('can not accesss the urls!')
  return None

def get_mem(content):
  pattern = re.compile(r'Heap Memory used ([0-9.]*) [MG]B')
  ret = re.findall(pattern, content)
  if not ret:
    return 0
  if float(ret[0]) < 5.26:
    print float(ret[0]) * 1024
    return '%f' % (  float(ret[0])  * 1024 )
  print ret[0]
  return ret[0]

def _plot():
  clf()
  t = arange(0, 30, 1)
  s = [0] * 30
  for i in t:
    s[i] = get_mem(get())
    time.sleep(1)

  plot(t, s)

  xlabel('time (s)')
  ylabel('voltage (mV)')
  title('About as simple as it gets, folks')
  grid(True)
  #savefig("test.png")
  show()

class Test(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def _test_get(self):
    pass

  def _test_mem(self):
    print get_mem(get())
    pass

  def test_plot(self):
    _plot()


if __name__ == '__main__':
  unittest.main()
