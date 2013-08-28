# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.realpath('.'), 'gen-py'))
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor




class HbaseClient(object):
  def __init__(self, host='10.237.14.236', port=9090):
    transport = TBufferedTransport(TSocket(host, port))
    transport.open()
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    self.client = Hbase.Client(protocol)

  def getTableNames(self):
    return self.client.getTableNames()

  def createTable(self, tableName, columnFamilies):
    columnFamilies = [ ColumnDescriptor(_) for _ in columnFamilies ]
    return self.client.createTable(tableName, columnFamilies)

  def exec_(self, name, *args, **kwargs):
    return eval('self.client.%(name)s(*%(args)s, **%(kwargs)s)' % ({'name': name, 'args': args, 'kwargs': kwargs}) )

if __name__ == "__main__":
  hclient = HbaseClient()
  print hclient.createTable('test_atupal_2', ['atupal'])
  #print hclient.exec_('getTableRegions', 'foo')

