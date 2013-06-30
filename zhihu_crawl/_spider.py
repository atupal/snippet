# -*- coding=utf-8 -*-

import requests
import threading
import unittest
import lxml.html
import json
from Queue import Queue
import csv

cnt = 0

class GetQuestionId(threading.Thread):
    def __init__(self, queue, ind):
        threading.Thread.__init__(self)
        self.queue = queue
        self.question_set = []
        self.fi = open('./zhihu_question_id_%s.json' % ind, 'wa')

    def run(self):
        while 1:
            num = self.queue.get()
            if num is None:
                break

            url = 'http://www.zhihu.com/question/%s' % num
            try:
                resp = requests.get(url, timeout = 20)
            except Exception as e:
                print e, num
                self.queue.task_done()
                self.queue.put(num)
                continue

            if resp.status_code is 200:
                xparser = lxml.html.fromstring(resp.content)
                res = xparser.xpath('//*[@id="zh-question-title"]/h2/text()')
                try:
                    global cnt
                    self.question_set.append({
                        'url':url,
                        'question': res[0],
                        'id': cnt
                     })
                    cnt += 1
                    print "%s:%s\n%s" % (cnt, url, res[0])
                except Exception as e:
                    print e

            if len(self.question_set) > 30:
                for i in self.question_set:
                    self.fi.write("%s\n\n" % json.dumps(i, indent = 4))
                self.question_set = []
                self.fi.flush()

            self.queue.task_done()

        def __del__(self):
            self.fi.close()

def put_queue(queue):
    id_zone = csv.reader(open('./id.csv'))
    for i in id_zone:
        begin = int(i[1])
        end = int(i[2])

    for i in xrange(begin, end + 1, 1):
        queue.put(i)


class mainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        queue = Queue()
        import thread
        thread.start_new_thread(put_queue, (queue, ))

        spiders = [GetQuestionId(queue, _) for _ in xrange(100)]
        for spider in spiders:
            spider.setDaemon(True)
            spider.start()

        queue.join()

        for spider in spiders:
            del spider

    def _test_2(self):
        put_queue(None)


if __name__ == "__main__":
    unittest.main()
