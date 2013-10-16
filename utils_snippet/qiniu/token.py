
import hmac
from base64 import urlsafe_b64encode
from hashlib import sha1
import json
import time

def token(ak, sk, b):
  data = urlsafe_b64encode(b)
  hashed = hmac.new(sk, data, sha1)
  return "%s:%s:%s" % (ak, urlsafe_b64encode(hashed.digest()), data)


if __name__ == "__main__":
  ak ='1QC9ogsi7s1Q5egZXKI-DHsCzVhOySzI9JnkG59l'
  sk = '5fWMHhGUDi1gTjIwKqSeZRQ6eTQ77rqPXyWyuT40'
  t = dict(
      scope = 'eding',
      deadline = int(time.time()) + 36000000
      )
  print(token(ak, sk, json.dumps(t, separators=(',',':'))   ) )
