# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.realpath('.'), 'gen-py'))
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase

transport = TBufferedTransport(TSocket('10.237.14.236', 9090))
transport.open()
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
print client.getTableNames()
