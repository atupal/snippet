



transport = TSocket.TSocket(host, port)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
transport.open()

columms = ['info:user', 'info:name', 'info:email']
scanner = client.scannerOpen('users', '', columns)
row = client.scannerOpen('users', '', columns)
row = client.scannerGet(scanner)
while row:
  yield user_from_row(row[0])
  row = scannerGet(scanner)
client.scannerClose(scanner)

def user_from_row(row):
  user = {}
  for col, cell in row.columns.items():
    user[col[5:]] = cell.value

  return "<User: {user}, {name}, {email}>".format(**user)
