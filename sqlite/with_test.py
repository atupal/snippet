# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
  cur = con.cursor()
  cur.execute('select sqlite_version()')

  data = cur.fetchone()

  print data
