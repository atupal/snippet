#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import logging
import unittest
import re
import matplotlib
from pylab import *
import time

urls = ['http://10.2.201.65:32201/dfshealth.jsp', 'http://10.2.201.66:32201/dfshealth.jsp']
urls_jmx = ['http://10.2.201.65:32201/jmx', 'http://10.2.201.66:32201/jmx']

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

import json
def get_jmx():
  for url in urls_jmx:
    ret = {}
    try:
      ret = json.loads(requests.get(url).content)
    except Exception as e:
      logging.error(str(e))
    for bean in ret.get('beans'):
      if bean.get('name') == 'Hadoop:service=NameNode,name=FSNamesystem' and bean.get('tag.HAState') == 'active':
        return ret.get('beans')
  logging.error('cat not access the urls!')
  return {}

def get_info_jmx(content):
  ret = {
      'mem': '',
      'cpu_time': '',
      }
  for bean in content:
    if bean.get('name') == 'java.lang:type=Memory':
      ret['mem'] = int( bean.get('HeapMemoryUsage').get('used') ) / 1024 / 1024
    elif bean.get('name') == 'java.lang:type=OperatingSystem':
      ret['cpu_time'] = bean.get('ProcessCpuTime')

  return ret

def _plot():
  clf()
  t = arange(0, 400, 1)
  s = [0] * 400
  for i in t:
    #s[i] = get_mem(get())
    s[i] = get_info_jmx(get_jmx()).get('cpu_time')
    print s[i]
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

  def _test_get_jmx(self):
    print get_jmx()


if __name__ == '__main__':
  unittest.main()
