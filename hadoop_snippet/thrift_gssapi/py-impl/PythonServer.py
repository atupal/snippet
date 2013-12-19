#!/usr/bin/env python2

import  sys
sys.path.append('../gen-py')

from hello import HelloWorld
from hello.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket

class HelloWorldHandler:
  def __init__(self):
    self.log = {}

  def ping(self):
    print 'ping()'

  def sayHello(self):
    print 'sayHello()' 
    return 'say hello from' + socket.gethostbyname(socket.gethostname())

  def sayMsg(self, msg):
    print 'sayMsg(' + msg + ')'
    return 'say ' + msg + ' from ' + socket.gethostbyname(socket.gethostname())


handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)

transport = TSocket.TServerSocket('0.0.0.0', 3030)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'Staring python server ...'
server.serve()
print 'done'
