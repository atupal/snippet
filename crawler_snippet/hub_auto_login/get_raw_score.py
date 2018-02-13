#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from PIL import Image
from StringIO import StringIO

username = 'U201110090'
password = 'TEtZczQ2OTAxMDI='
#username = 'U201110087'
#password = '158951'.encode('base64')


s = requests.Session()
content = s.get('http://bksjw.hust.edu.cn/index.jsp').content
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
  verify_url = 'http://bksjw.hust.edu.cn/randomKey.action?username=%s&time=%d' % (username, TIME)
  content = s.get(verify_url, headers={'referer': 'http://bksjw.hust.edu.cn/index.jsp'}).content
  global k1, k2
  k1, k2 = eval(content)
  verify_image_url = 'http://bksjw.hust.edu.cn/randomImage.action?k1=%s&k2=%s&uno=%s&time=%d' % (k1, k2, username, TIME)
  content = s.get(verify_image_url).content
  global vimg
  vimg = Image.open(StringIO(content))

get_rand_key()

try:
  #from pytesser.pytesser import image_to_string
  #vcode = image_to_string(vimg).strip()
  import ocr
  vcode = ocr.get_img_num(vimg)
  vimg.save('vcode.jpg')
except:
  import traceback, sys
  traceback.print_exc(file=sys.stdout)
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
  url = 'http://bksjw.hust.edu.cn/hublogin.action'
  data['rand'] = '%5d' % vcode
  data['random_key1'] = k1
  data['random_key2'] = k2
  headers = {
      'Host': 'bksjw.hust.edu.cn',
      'Origin': 'http://bksjw.hust.edu.cn',
      'Referer': 'http://bksjw.hust.edu.cn/index.jsp',
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'
      #'Connection': 'keep-alive',
      }
  # login post
  res = s.post(url, data = data, headers=headers)
  # print res.content

  content = s.get('http://bksjw.hust.edu.cn/frames/body_left.jsp').content
  #print content
  #print s.cookies

def get_raw_score():
  url = 'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action?cdbh=225'
  content = s.get(url, headers={'referer': 'http://bksjw.hust.edu.cn/frames/body_left.jsp'}).content
  key1str = ['name="key1" value="', '857702']
  key2str = ['name="key2" value="', 'acde42e26e31da0e3b8e7093d9cf3685']
  key1ind = content.find(key1str[0])
  key2ind = content.find(key2str[0])
  key1 = content[key1ind+len(key1str[0]):key1ind+len(key1str[0])+len(key1str[1])]
  key2 = content[key2ind+len(key2str[0]):key2ind+len(key2str[0])+len(key2str[1])]

  queryscoreurl = 'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_queryScore.action'
  data = {
      'key1': key1,
      'key2': key2,
      'type': 'cj',
      'stuSfid': username,
      'xqselect':'20132'
      }
  headers={
      'Host' :'bksjw.hust.edu.cn',
      'Origin': 'http://bksjw.hust.edu.cn',
      'Referer': 'http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action?cdbh=225'
      }
  content = s.post(queryscoreurl, data=data, headers=headers).content
  ind = content.find('cachedId=')
  cachedId = content[ind+len('cachedId=') : ind+content[ind:].find('&')]
  ind = content.find('reportParamsId=')
  reportParamsId = content[ind+len('reportParamsId=') : ind+content[ind:].find('&')]
  rawscoreurl = ('http://bksjw.hust.edu.cn:80/reportServlet?action=18&file=student_personal_score_grade.raq&srcType=file&separator=%09&reportParamsId=' + 
  reportParamsId + '&cachedId=' +
  cachedId +'&t_i_m_e=' + str(TIME)  )
  content = s.get(rawscoreurl).content
  print content.decode('gb2312')

if __name__ == '__main__':
  login()
  get_raw_score()
