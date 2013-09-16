# -*_ coding: utf-8 -*-
import fbconsole

import urllib2


import pdb

fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins']
fbconsole.authenticate()
fbconsole.logout()
