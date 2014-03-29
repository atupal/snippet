#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from PIL import Image
from StringIO import StringIO

username = 'U201110090'


s = requests.Session()
content = s.get('http://hub.hust.edu.cn/index.jsp').content
qstr = 'name="ln" value="'
start = content.find(qstr) + len(qstr)
server = content[start:start+len('app66.dc.hust.edu.cn')]
k1 = 1
k2 = 1

import time
TIME = int(time.time() * 1000)
vimg = None
image_to_string = None
def get_rand_key():
  verify_url = 'http://hub.hust.edu.cn/randomKey.action?username=%s&time=%d' % (username, TIME)
  content = s.get(verify_url).content
  global k1, k2
  k1, k2 = eval(content)
  verify_image_url = 'http://hub.hust.edu.cn/randomImage.action?k1=%s&k2=%s&uno=%s&time=%d' % (k1, k2, username, TIME)
  content = s.get(verify_image_url).content
  global vimg
  vimg = Image.open(StringIO(content))

get_rand_key()

try:
  from pytesser.pytesser import image_to_string
  vcode = image_to_string(vimg).strip()
except:
  vimg.show()
  vcode = raw_input('verify code:')

data = {
    'usertype': 'xs',
    'username': username,
    'password': password,
    'rand': '',
    'ln': server,
    'random_key1' : '',
    'random_key2' : '',
    'submit': '立即登录',
    }

def login():
  url = 'http://hub.hust.edu.cn/hublogin.action'
  data['rand'] = vcode
  data['random_key1'] = k1
  data['random_key2'] = k2
  headers = {
      #'Host':'hub.hust.edu.cn',
      #'Origin':'http://hub.hust.edu.cn',
      #'Referer':'http://hub.hust.edu.cn/index.jsp',
      'User-Agent':
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
      'Connection': 'keep-alive',
      }
  res = s.post(url, data = data)

  print res.content
  content = s.get('http://hub.hust.edu.cn/frames/body_left.jsp').content
  print content
  print s.cookies

if __name__ == '__main__':
  login()
