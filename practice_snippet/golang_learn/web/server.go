
func (srv *Server) Server(l net.Listener) error {
  defer l.Close()
  var tempDelay time.Duration // how long to sleep on accept failure
  for {
    rw, e := l.Accept() // 
    if e != nil {
      if ne, ok := e.(net.Error); ok && ne.Temporary() {
        if tempDelay == 0 {
          tempDelay = 5 * time.Millisecond
        } else {
          tempDelay *= 2
        }
        if max := 1 * time.Second; tempDelay > max {
          tempDelay = max
        }
        log.Printf("http: Accept error: %v; retrying in %v", e, tempDelay)
        time.Sleep(tempDelay)
        continue
      }
      return e
    }
    tempDelay = 0
    c, err := srv.newConn(rw)
    if err != nil {
      continue
    }
    go c.serve() // 高并发， 用户的每一次请求都是新开一个goroutine的服务，相互不影响
  }
}


/*
  ListenAndServer 监听端口addr
  net.Listen("tcp", addr)
  接收到用户请求并创建Conn:
  srv.Server(l net.Listenner)
  进入for{}
  rw := l.Aceept()
  c := srv.NewConn()
  go c.serve()   //继续处理下一个conn
*/

