#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json

url = 'http://122.205.11.50/hubdisk/findStudentMenus.action'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def rq(id):
  try:
    data = {
      'node': id
        }
    return json.loads(requests.post(url, data=data).content)
  except KeyboardInterrupt:
    exit()
  except:
    print '出错了 :('
    return []

col = rq("sxlbm_11")
print col

def run(year):
  with open('dat-%s' % year, 'wa') as fi:
    # 遍历学院
    for c in col:
      id = c.get('id')
      cla = rq(id)
    
      # 遍历年级
      for i in cla:
        y = i.get('text')
        #if y == '2010' or y == '2011' or y == '2012':
          #pass
        if y == year:
          pass
        else:
          continue
        print '###nj-' + y
        fi.write( ('###nj-' + str(y) + "\n").encode('utf-8'))
        fi.flush()
        id = i.get('id')
        
        cla_m = rq(id)
    
        # 遍历班级
        for j in cla_m:
          print '###bj-' + j.get('text')
          fi.write( ('###bj-' + str(j.get('text')) + "\n").encode('utf-8'))
          fi.flush()
          id = j.get('id')
    
          ps = rq(id)
          # 打印这个班所有学生
          for x in ps:
            print x.get('id')
            fi.write( ( str(x.get('id')) + "\n").encode('utf-8')  )
            fi.flush()


#run("2013")
run("2012")
#run("2011")
#run("2010")
#run("2009")
#run("2008")
#run("2007")
