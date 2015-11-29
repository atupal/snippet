#!/usr/bin/python2
# -*- coding: utf-8 -*-

import time
import requests
from StringIO import StringIO
from PIL import Image

TIME = int(time.time()*1000)
s = requests.Session()
TH_MIN = 155
TH_MAX = 256

import math
def cosine_similarity(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(max(len(v1), len(v2))):
        if len(v1)<=i:
            x = 0
        else:
            x = int(v1[i])
        if len(v2)<=i:
            y = 1
        else:
            y = int(v2[i])
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def get_random_img(url=None):
  if url:
      verify_image_url = url
  else:
      verify_image_url = 'https://passport.zhaopin.com/checkcode/imgrd'
      #verify_image_url = 'http://www.liepin.com/image/randomcode4Login'
  content = s.get(verify_image_url).content
  global vimg
  vimg = Image.open(StringIO(content))
  vimg.save('./tmp.gif')
  vimg = vimg.convert('RGB')
  #import ipdb
  #ipdb.set_trace()
  return vimg

def read_image():
  img = Image.open('vcode.jpg')
  return img

def isHit(whiteblack):
    if whiteblack <= TH_MAX and whiteblack >= TH_MIN:
        return False

    return True

def isHitRGB(rgb):
    return isHit(sum(rgb)/3)

def next_fg_bound(img, begin):
  data = img.getdata()
  for i in xrange(begin, img.size[0]):
    for j in xrange(img.size[1]):
      if isHitRGB(data[j*img.size[0]+i]):
        return i

broads = []
def next_bg_bound(img, begin):
  data = img.getdata()
  for i in xrange(begin, img.size[0]):
    if i in broads:return i+1
    flag = 1
    for j in xrange(img.size[1]):
      if isHitRGB(data[j*img.size[0]+i]):
            flag = 0
            break
    if flag: return i

def print_img(img):
  data = img.getdata()
  a = {}
  for i in xrange(img.size[1]):
    for j in xrange(img.size[0]):
      c = data[i*img.size[0]+j]
      if c in a:a[c]+=1
      else:a[c]=1
      if isHitRGB(data[i*img.size[0]+j]):
        print  '*',
      else:
        print '-',
    print
  print
  #exit()

  for c in a:
    if a[c]<50:continue
    cnt = 0
    for i in xrange(img.size[1]):
      for j in xrange(img.size[0]):
        if isHitRGB(data[i*img.size[0]+j]) and sum(map(abs, map(int.__sub__, c, data[i*img.size[0]+j]))) < 20:
            cnt += 2
    if cnt <20:continue
    left = 1000
    right = -1
    for i in xrange(img.size[1]):
      for j in xrange(img.size[0]):
        if sum(map(abs, map(int.__sub__, c, data[i*img.size[0]+j]))) < 20:
          left = min(left, j)
          right = max(right, j)
          #print  '*',
        else:
          #print '-',
          pass
      #print
    broads.append(right)
    for j in xrange(left, right):
        flag = 1
        for i in xrange(img.size[1]):
            if sum(map(abs, map(int.__sub__, c, data[i*img.size[0]+j]))) < 20:
                flag = 0
                break
        if flag:
            broads.append(j)
            break
    #print
  #exit()

def get_img_num(img):
  begin, end = 0, 0
  ret = ''
  i = 0
  cliffs = []
  while i < 4:
    try:
        begin = next_fg_bound(img, end)
        end = next_bg_bound(img, begin)
        j = get_num(img, begin, end)
    except TypeError:
        return "sorry, I can not verify this code:("
    if j == -1:
        continue
    print begin, end
    cliffs.append(end)
    #ret = ret * 10 + j
    ret += str(j)
    i += 1

  data = img.getdata()
  for i in xrange(img.size[1]):
    for j in xrange(img.size[0]):
      if j in cliffs:
        print '|',
        continue
      if isHitRGB(data[i*img.size[0]+j]):
        print  '*',
      else:
        print '-',
    print
  print
  print cliffs

  #print ret
  return ret

def get_num(img, begin, end):
  num_vector = []

  for i in xrange(10):
      with open('./data/{0}'.format(i)) as fd:
          num_vector.append( map(str.strip, fd.readlines()) )

  import string
  for i in string.lowercase:
      with open('./data/{0}'.format(i)) as fd:
          num_vector.append( map(str.strip, fd.readlines()) )

  data = img.getdata()
  top, bot = 0, img.size[1]
  for i in xrange(img.size[1]):
    if top:
      break
    for j in xrange(begin, end):
      if isHitRGB(data[i*img.size[0]+j]):
        top = i
        break

  for i in xrange(top, img.size[1]):
    flag = 1
    for j in xrange(begin, end):
      if isHitRGB(data[i*img.size[0]+j]):
        flag = 0
        break
    if flag:
      bot = i
      break

  if end-begin+bot-top < 13:
      return -1
  if bot-top < 5:
      return -1
  if end-begin<5:
      return -1

  ret = [0] * 10

  vector_a = []
  for x in xrange(top, bot):
    for y in xrange(begin, end):
      if isHitRGB(data[x*img.size[0]+y]):
        #print '*',
        vector_a.append('1')
        pass
      else:
        #print ' ',
        vector_a.append('0')
        pass
    #print

  print ''.join(vector_a)


  # execise
  """
  n = raw_input('guess:')
  if n:
      with open('./data/{0}'.format(n.lower()), 'a') as fd:
          fd.write("{0}\n".format(''.join(vector_a)))

  return
  """

  expect = [0]*36
  for i in xrange(36):
      expect[i] = max(   [cosine_similarity(vector_b, vector_a) for vector_b in num_vector[i]] + [-1]  )

  #print expect
  m = expect.index(max(expect))
  return str(m) if m < 10 else chr(ord('a')+m-10)
  return -1

if __name__ == '__main__':
  img = get_random_img()
  #img = read_image()
  print_img(img)
  print '{0}' .format( get_img_num(img) )
  print broads
