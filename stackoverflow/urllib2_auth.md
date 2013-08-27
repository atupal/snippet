```
import urllib2, base64

request = urllib2.Request("http://api.foursquare.com/v1/user")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
```
