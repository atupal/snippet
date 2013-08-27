# -*- coding: utf-8 -*-

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from gen_py.hbase import Hbase

transport = TBufferedTransport(TSocket('10.237.14.236', 9090))
transport.open()
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
print help(client)
