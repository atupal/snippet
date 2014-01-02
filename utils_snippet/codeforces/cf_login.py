#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pickle
import requests
import logging
import re

class Entry(object):

  LOG = logging.getLogger(__name__)
  login_url = 'http://codeforces.com/enter'
  login_data = {
      'csrf_token': '',
      'action': 'enter',
      'handle': '',
      'password': '',
      'remember': 'on',
      '_tta': '935',
      }

  def __init__(self):
    try:
      with open('./user') as fi:
        lines = fi.readlines()
        self.user = lines[0].rstrip('\n')
        self.password = lines[1].rstrip('\n')
    except IOEroor:
      self.user = raw_input('username:')
      self.password = raw_input('password:')

    self.session = requests.Session()

    self._login()

  def _login(self):
    content = self.session.get(self.login_url).content
    ret = re.findall(r'name="X-Csrf-Token" content="([0-9a-z]+)"', content)
    if len(ret) < 1:
      LOG.fatal('get csrf token failed!')
      exit()
    self.login_data['csrf_token'] = ret[0]
    self.login_data['handle'] = self.user
    self.login_data['password'] = self.password
    self.session.post(self.login_url, data = self.login_data)
    print self.session.get('http://wwww.codeforce.com').content.find('atupal')
    self._save_cookie()

  def _login_success(self):
    pass

  def _save_cookie(self):
    try:
      with open('./login.cookie', 'wb') as fi:
        cookie = requests.utils.dict_from_cookiejar(self.session.cookies)
        pickle.dump(cookie, fi)
    except IOEroor as e:
      logging.error('Failed save cookie to local file! \n%s' % str(e))

  def _load_cookie(self):
    try:
      with open('./login.cookie', 'rb') as fi:
        cookie = pickle.load(fi)
        self.session.cookies.update(cookie)
        if self._login_success():
          return 1
        return 0
    except:
      return 1


def test():
  entry = Entry()

if __name__ == '__main__':
  test()
