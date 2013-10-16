#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
  con = lite.connect('test.db')

  cur = con.cursor()
  cur.execute('select sqlite_version()')

  data = cur.fetchone()

  print 'version:', data
except lite.Error, e:
  print 'Error:', e.args[0]
  sys.exit(1)
finally:
  if con:
    con.close()
