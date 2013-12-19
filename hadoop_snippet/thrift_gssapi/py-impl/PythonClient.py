#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
sys.path.append('../gen-py')

from hello import HelloWorld
from hello.ttypes import *
from hello.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol  # note that python only supoort TBinaryProtocol,艰难

try:
  # Make socket
  transport = TSocket.TSocket('0.0.0.0', 3030)
  
  # Buffering is critical, Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = HelloWorld.Client(protocol)

  # Connect !
  transport.open()

  client.ping()
  print 'ping()'

  msg = client.sayHello()
  print msg
  msg = client.sayMsg(HELLO_1)
  print msg

  transport.close()

except Thrift.TException as tx:
  print '%s' % (tx.message)
