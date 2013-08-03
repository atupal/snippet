
首先调用http.HandleFunc
- 1. 调用了DefaultServerMux的HandleFunc
- 2. 调用了DefaultServerMux的Handle
- 3. 往DefaultServeMux的map[string]muxEntry 中增加对应的handler和路由规则



其次调用http.ListenAndServe(":9090", nil)
- 1 实例化Server
- 2 调用Server的ListenAndServer()
- 3 调用net.Listen("tcp", addr)
- 4 启动一个for循环，在循环体中Accept请求
- 5 对每个请求实例化一个Conn， 并且开启一个goroutine为这个请求进行服务go c.serve()
- 6 读取每隔请求的内容 w, err = c.readRequest()
- 7 判断handler是否为空， 如果没有设置handler，handler就设置为DefaultServeMux
- 8 调用handler的ServeHTTP
- 9 根据request选择handleer，并且进入到这个handler的ServeHTTP `mux.handler(r).ServeHTTP(w, r)`
- 判断是否有路由能满足这个request（循环遍历ServerMux的muxEntry）
  如果有路由满足，就调用这个路由handler的ServeHttp，否则返回NotFoundHandler的ServeHttp
