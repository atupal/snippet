# -*- coding: utf-8 -*-
import json


from PIL import Image

def pro():
  ret = json.load(open('result.json'))
  vis = [0] * 210
  cnt = 0
  r = set()
  for i in ret.keys():
    images = [i]
    while 1:
      if len(images) > 1 and images[0] == images[-1]:
        break
      right = ret.get(images[-1]).get('right')
      left = ret.get(images[0]).get('left')
      flag = 0
      if images[-1] == ret.get(right).get('left'):
        images.append(right)
        flag = 1
      if images[0] == ret.get(left).get('right'):
        images.insert(0, left)
        flag = 1
      if not flag:
        break
    if len(images) > 1 and ''.join(images) not in r:
      r.add(''.join(images))
      im = []
      for image in images:
        im.append(Image.open('img/%.3d.bmp' % int(image)  ))
      target = Image.new('RGB', ( im[0].size[0] * len(images), im[0].size[1] ))
      left = 0
      right = im[0].size[0]
      for image in im:
        target.paste(image, (left, 0, right, im[0].size[1]) )
        left += im[0].size[0]
        right += im[0].size[0]
      target.save('ret/%.3d.bmp' % cnt)
      print (target)
      cnt += 1

def pro_c():
  right = [-1] * 210
  left = [-1] * 210
  with open('c_result.raw') as fi:
    for line in fi:
      l, r = [int(_) for _ in line.strip().split()]
      right[l] = r
      left[r] = l
  cnt = 0
  cnt_n = 0
  vis = set()

  while 1:
    ff = 0
    for i in xrange(209):
      if right[i] != -1 and i not in vis:
        ff = 1
        images = [ i, right[i] ]
        vis.add(i)
        vis.add(right[i])
        right[i] = -1
        while 1:
          ll = images[0]
          rr = images[-1]
          flag = 0
          if left[ll] != -1 and left[ll] not in vis:
            flag = 1
            images.insert(0, left[ll])
            vis.add(left[ll])
          if right[rr] != -1 and right[rr] not in vis:
            flag = 1
            images.append(right[rr])
            vis.add(right[rr])
            right[rr] = -1
          if not flag:
            im = []
            for image in images:
              vis.add(image)
              from PIL import ImageFont
              from PIL import ImageDraw
              tmp = Image.open( 'img/%.3d.bmp' % int(image) )
              draw = ImageDraw.Draw(tmp)
              font = ImageFont.truetype("DejaVuSans.ttf", 16)

              draw.text((0, 0),"%d" % image, fill=40 , font=font)

              im.append(tmp)
            target = Image.new('RGB', ( im[0].size[0] * len(images), im[0].size[1] ))
            _left = 0
            _right = im[0].size[0]
            for image in im:
              target.paste(image, (_left, 0, _right, im[0].size[1]) )
              _left += im[0].size[0]
              _right += im[0].size[0]
            if len(images) < 19:
              target.save('ret_n/%.3d.bmp' % cnt_n)
              cnt_n += 1
              break
            target.save('ret/%.3d.bmp' % cnt)
            print (target)
            cnt += 1
            break
    if not ff:
      break
    print cnt

def row_splice():
  import os
  os.system("rm ret/*")
  os.system("rm ret_n/*")
  pro_c()

def col_splice():
  import os
  os.system("rm result/*.bmp")
  cnt = 0
  for images in [ [2, 6, 1, 7,  9,   3, 10, 8, 5, 0, 4] ]:
    im = []
    for image in images:
      from PIL import ImageFont
      from PIL import ImageDraw
      tmp = Image.open( 'ret/%.3d.bmp' % int(image) )
      draw = ImageDraw.Draw(tmp)
      font = ImageFont.truetype("DejaVuSans.ttf", 16)

      draw.text((0, 0),"%d" % image, fill=40 , font=font)

      im.append(tmp)
    target = Image.new('RGB', ( im[0].size[0], im[0].size[1] * len(images) ))
    _top = 0
    _bot = im[0].size[1]
    for image in im:
      target.paste(image, (0, _top, im[0].size[0], _bot))
      _top += im[0].size[1]
      _bot += im[0].size[1]
    target.save('result/result-%.3d.bmp' % cnt)
    print target
    cnt += 1

def main():
  col_splice()

if __name__ == '__main__':
  main()
