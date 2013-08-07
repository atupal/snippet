#!/bin/env python2.7
# -*- coding: utf-8 -*-

import requests
from pprint import pprint as printf

URL = "http://10.2.201.65:32201/webhdfs/v1/?op=liststatus"

def un_auth():
  resp = requests.get(URL)
  assert resp.status_code == 401
  print resp.headers
  print resp.content

 
if __name__ == "__main__":
  un_auth()
