
//在等待客户端时：
c, err := srv.newConn(rw)
if err != nil {
  continue
}

go c.serve()


type ServeMux struct {
  mu sync.RWMutex // 锁， 由于请求设计到并发处理，因此这里需要一个锁机制
  m map[string]muxEntry // 路由规则， 一个string对应一个mux实体， 这里的string就是注册的路由表达式
  hosts bool // 是否在任意的规则中带有host信息
}

type muxEntry {
  explicit bool // 是否精确匹配
  h Handler // 这个路由表达式对应的哪个handler
  pattern string // 匹配字符串
}

type Handler interface {
  ServeHTTP(ResponseWrite, *Request)
}

/*
  sayhelloName 并没有实现ServerHTTP这个接口
  是由HadlerFunc调用后强制转换
*/

type HandlerFunc func(ResponseWriter, *Request)

//SverHTTP calls f(w, r)

func (f hadlerFunc) ServerHTPP(w ResponseWrite, r *Request) {
  f(w, r)
}

//默认的路由器实现了ServeHTTP:
func (mux *ServeMux) ServeHTTP(w ResponseWriter, r *Request) {
  if r.RequestURI == "*" {
    w.Header().set("Connection", "close")
    w.WriteHeader(StatusBadRequest)
    return
  }
  h, _ := mux.Handler(r)
  h.ServeHTTP(w, r)
}

func (mux *ServeMux) Handler(r *Request) (h hadler, pattern string) {
  if r.Method != "CONNECT" {
    if p := cleanPath(r.URL.Path); p != r.URL.Path {
      _, pattern = mux.handler(r.Host, p)
      return RedirectHandler(p, StatusMovePermanently), pattern
    }
  }
  return mux.handler(r.Host, r.URL.Path)
}

func (mux *ServerMux) handler(host, path string) (h Handler, pattern string) {
  mux.mu.RLock()
  defer mux.mu.RUnlock()

  if mux.hosts {
    h, pattern = mux.match(host + path)
  }
  if h == nil {
    h, pattern = mux.match(path)
  }
  if h == nil {
    h, pattern = NotFoundHandler(), ""
  }
  return
}
