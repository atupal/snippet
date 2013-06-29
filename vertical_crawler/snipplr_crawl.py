
import threading
import lxml.html
import requests
import random
import itertools
import time

user_agent = [
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',

        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0;'
        ' SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C) QQBrowser/6.14.15493.201' ,

        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)' ,

        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)' ,

        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1' ,

        'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) '
        'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
        ]


class SnipplrDownloader(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.any_true = lambda predicate, sequence: True in itertools.imap(predicate, sequence)

    def run(self):
        while 1:
            url = self.queue.get()
            try:
                print url
                time.sleep(random.random())
                header = {
                        'User-Agent': random.choice(user_agent)
                        }
                resp = requests.get(url, headers = header)
                xparser = lxml.html.fromstring(resp.content)
                res = xparser.xpath("//@href")
                res.extend(xparser.xpath("//@src"))
                for url in res:
                    if self.any_true(url.endswith, ('.jpg', '.gif', '.png')) is False:
                        if url.startswith('http') is False:
                            url = resp.url + url
                        self.queue.put(url)

            except Exception as e:
                print e

            self.queue.task_done()

class SnipplrAnalyze(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        from Queue import Queue
        self.queue = Queue()
        self.queue.put('http://snipplr.com/all/tags/scrapy/')
        self.client = [SnipplrDownloader(self.queue) for i in xrange(10)]

    def tearDown(self):
        pass

    def test_main(self):
        for client in self.client:client.setDaemon(True)
        for client in self.client:client.start()
        self.queue.join()

if __name__ == "__main__":
    unittest.main()
