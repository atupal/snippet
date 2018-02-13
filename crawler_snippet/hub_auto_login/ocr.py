# -*- coding: utf-8 -*-

import time
import requests
from StringIO import StringIO
from PIL import Image

TIME = int(time.time()*1000)
s = requests.Session()
TH = 125

def get_random_img():
  username = 'U201110090'
  verify_url = 'http://bksjw.hust.edu.cn/randomKey.action?username=%s&time=%d' % (username, TIME)
  content = s.get(verify_url, headers={'referer': 'http://bksjw.hust.edu.cn/index.jsp'}).content
  #global k1, k2
  k1, k2 = eval(content)
  verify_image_url = 'http://bksjw.hust.edu.cn/randomImage.action?k1=%s&k2=%s&uno=%s&time=%d' % (k1, k2, username, TIME)
  content = s.get(verify_image_url).content
  global vimg
  vimg = Image.open(StringIO(content))
  return vimg

def read_image():
  img = Image.open('vcode.jpg')
  return img

def next_fg_bound(img, begin):
  data = img.getdata()
  for i in xrange(begin, img.size[0]):
    for j in xrange(img.size[1]):
      if sum(data[j*img.size[0]+i])/3 < TH:
        return i

def next_bg_bound(img, begin):
  data = img.getdata()
  for i in xrange(begin, img.size[0]):
    flag = 1
    for j in xrange(img.size[1]):
      if sum(data[j*img.size[0]+i])/3 < TH:
        flag = 0
        break
    if flag: return i

def print_img(img):
  data = img.getdata()
  for i in xrange(img.size[1]):
    for j in xrange(img.size[0]):
      if sum(data[i*img.size[0]+j])/3 > TH:
        print  ' ',
      else:
        print '*',
    print
  print

def get_img_num(img):
  begin, end = 0, 0
  ret = 0
  for i in xrange(5):
    begin = next_fg_bound(img, end)
    end = next_bg_bound(img, begin)
    ret = ret * 10 + get_num(img, begin, end)[0]
  #print ret
  return ret

def get_num(img, begin, end):
  num_list = [
      [
        '    * * *    ',
        '  * *   * *  ',
        '  *       *  ',
        '* *       * *',
        '* *       * *',
        '* *       * *',
        '* *       * *',
        '* *       * *',
        '* *       * *',
        '  *       *  ',
        '  * *   * *  ',
        '    * * *    ',
        ],
      [
        '    * *    ',
        '* * * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '    * *    ',
        '* * * * * *',
        ],
      [
        '    * * * *    ',
        '  *     * * *  ',
        '*         * *  ',
        '          * *  ',
        '          * *  ',
        '          *    ',
        '        * *    ',
        '        *      ',
        '      *        ',
        '    *         *',
        '  * * * * * * *',
        '* * * * * * *  ',
        ],
      [
        '    * * * *  ',
        '* *     * * *',
        '*         * *',
        '          * *',
        '        * *  ',
        '      * * *  ',
        '        * * *',
        '          * *',
        '          * *',
        '          * *',
        '* *     * *  ',
        '* * * * *    ',
        ],
      [
        '          * *  ',
        '          * *  ',
        '        * * *  ',
        '      *   * *  ',
        '    *     * *  ',
        '    *     * *  ',
        '  *       * *  ',
        '*         * *  ',
        '* * * * * * * *',
        '          * *  ',
        '          * *  ',
        '          * *  ',
        ],
      [
        '    * * * *',
        '    * * * *',
        '  *        ',
        '  * * *    ',
        '* * * * *  ',
        '      * * *',
        '        * *',
        '          *',
        '          *',
        '          *',
        '*       *  ',
        '* * * *    ',
        ],
      [
        '          * * *',
        '      * * *    ',
        '    * *        ',
        '  * *          ',
        '  *   * * *    ',
        '* * *     * *  ',
        '* *         * *',
        '* *         * *',
        '* *         * *',
        '* *         * *',
        '  * *     * *  ',
        '    * * * *    ',
        ],
      [
        '  * * * * * * *',
        '  * * * * * *  ',
        '*           *  ',
        '          *    ',
        '          *    ',
        '          *    ',
        '        *      ',
        '        *      ',
        '      *        ',
        '      *        ',
        '      *        ',
        '    *          ',
        ],
      [
        '    * * * *    ',
        '  * *       * *',
        '* *         * *',
        '* *         * *',
        '  * * *   * *  ',
        '    * * *      ',
        '    * * * *    ',
        '  *       * *  ',
        '* *         * *',
        '* *         * *',
        '  * *     * *  ',
        '    * * * *    ',
        ],
      [
        '    * * * *    ',
        '  * *     * *  ',
        '* *         * *',
        '* *         * *',
        '* *         * *',
        '* *         * *',
        '  * *       * *',
        '    * * * * *  ',
        '          * *  ',
        '        * *    ',
        '      * *      ',
        '* * *          ',
        ],
]
  data = img.getdata()
  top, bot = 0, img.size[1]
  for i in xrange(img.size[1]):
    if top:
      break
    for j in xrange(begin, end):
      if sum(data[i*img.size[0]+j])/3 < TH:
        top = i
        break

  for i in xrange(top, img.size[1]):
    flag = 1
    for j in xrange(begin, end):
      if sum(data[i*img.size[0]+j])/3 < TH:
        flag = 0
        break
    if flag:
      bot = i
      break

  ret = [0] * 10
  a, b = 0, 0
  c, d = 0, 0
  for x in xrange(top, bot):
    for y in xrange(begin, end):
      if sum(data[x*img.size[0] + y])/3 < TH:
        #print '*',
        if x < (top + bot)/2:
          a += 1
        else:
          b += 1
        if y < (begin + end) / 2:
          c += 1
        else:
          d += 1
      else:
        #print ' ',
        pass
    #print 

  import operator
  for i in xrange(10):
    ret[i] = abs(a - reduce(operator.add, num_list[i][:len(num_list[i])>>1]).count('*'))
    ret[i] += abs(b - reduce(operator.add, num_list[i][len(num_list[i])>>1:]).count('*'))
    cc, dd = 0, 0
    for s in num_list[i]:
      cc += s[:len(s)/2].count('*')
      dd += s[len(s)/2:].count('*')
    ret[i] += abs(c-cc)
    ret[i] += abs(d-dd)
  return ret.index(min(ret)) , ret

if __name__ == '__main__':
  img = get_random_img()
  print_img(img)
  print '%5d' % get_img_num(img)
