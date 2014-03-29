from multiprocessing.connection import Listener

address = ('localhost', 8000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey='secret password')

while True:
    conn = listener.accept()
    print 'connection accepted from', listener.last_accepted

    data = conn.recv()
    try:
      result = 'hi: %s' % data
      conn.send_bytes('get %s'%(result,))
    except Exception,e:
      print e
    finally:
      conn.close()

listener.close()
