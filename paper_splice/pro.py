# -*- coding: utf-8 -*-
import json


import Image

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
    if len(images) > 5 and ''.join(images) not in r:
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
      print target
      cnt += 1

def main():
  pro()

if __name__ == '__main__':
  main()
