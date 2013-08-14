#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import multiprocessing
import time
import signal
import sys

def init_worker():
  signal.signal(signal.SIGINT, signal.SIG_IGN)

def worker():
  while True:
    time.sleep(1.1234)
    print "Working..."

if __name__ == "__main__":
  pool = multiprocessing.Pool(50, init_worker)
  try:
    for i in range(50):
      pool.apply_async(worker)

    time.sleep(10)
    pool.close()
    pool.join()
  except KeyboardInterrupt:
    print 'Caught KerboardInterrupt, terminating workers'
    pool.terminate()
    pool.join()
