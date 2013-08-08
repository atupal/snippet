#!/bin/env python2.7
# -*- coding: utf-8 -*-

import requests
import sys
sys.path.insert(0, './lib/kerberos-1.1.1/build/lib.linux-x86_64-2.7')
import kerberos
print kerberos.__file__
from pprint import pprint as printf

URL = "http://10.2.201.65:32201/webhdfs/v1/?op=liststatus"

def un_auth():
  resp = requests.get(URL)
  assert resp.status_code == 401
  print resp.headers
  print resp.content

def negotiate_auth():
  _, krb_context = kerberos.authGSSClientInit("HTTP@hadoop")
  kerberos.authGSSClientStep(krb_context, "")
  negotiate_details = kerberos.authGSSClientResponse(krb_context)
  headers = {"Authorization": "Negotiate" + negotiate_details}
  resp = requests.get("http://hadoop:32201/webhdfs/v1/?op=liststatus", headers = headers)
  print resp.status_code
  print resp.content

 
if __name__ == "__main__":
  #un_auth()
  negotiate_auth()
