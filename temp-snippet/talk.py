# -*- codiing: utf-8 -*-

import requests
import urllib
import unittest
import json


def say_zh(msg):
  return translate( say_en(translate(msg)) )

def say_en(msg):
  """
  this is eugene bot
  """
  try:
    url = 'http://www.princetonai.com/bot/botanswer.do?request='\
          + urllib.quote(msg)
    content = requests.get(url).content
    return content
  except:
    import traceback, sys
    traceback.print_exc(file=sys.stdout)
    return 'error'


def say_en_2(msg):
  """
  this is alice
  """
  try:
    url = 'http://sheepridge.pandorabots.com/pandora/talk?botid=b69b8d517e345aba&skin=custom_input'
    data = {
        'botcust2': 'bdfc33b5de1b1c31',
        'input': msg
        }
    content = requests.post(url, data = data).content
    return content
  except:
    import traceback, sys
    traceback.print_exc(file=sys.stdout)
    return 'error'


def translate(msg):
  keyfrom = 'atupal-site'
  key = '401682907'
  url = 'http://fanyi.youdao.com/openapi.do?keyfrom=' + keyfrom \
        + '&key=' + key + '&type=data&doctype=json&version=1.1&q=' \
        + urllib.quote(msg)
  try:
    content = requests.get(url).content
    ret = json.loads(content)
  except:
    ret = {'translation': ['error']}

  return ret['translation'][0]


class Test(unittest.TestCase):
  def _test_trans(self):
    while 1:
      try:
        msg = raw_input('msg:')
        print translate(msg)
      except:
        import traceback, sys
        traceback.print_exc(file=sys.stdout)
        break
 
  def _test_say_en(self):
    while 1:
      try:
        msg = raw_input('you:')
        print say_en(msg)
      except:
        import traceback, sys
        traceback.print_exc(file=sys.stdout)
        break

  def test_say_zh(self):
    while 1:
      try:
        msg = raw_input('you:')
        print say_zh(msg)
      except:
        import traceback, sys
        traceback.print_exc(file=sys.stdout)
        break

if __name__ == "__main__":
  unittest.main()
