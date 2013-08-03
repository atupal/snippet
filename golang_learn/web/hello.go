
package main

import (
  "fmt"
  "net/http"
  "strings"
  "log"
)

func sayhelloName(w http.ResponseWriter, r *http.Request) {
  r.ParseForm()
  fmt.Println(r.Form)
  fmt.Println("path", r.URL.Path)
  fmt.Println("scheme", r.URL.Scheme)
  fmt.Println(r.Form["url_long"])

  for k, v := range r.Form {
    fmt.Println("key:", k)
    fmt.Println("val:", strings.Join(v, ""))
  }
  fmt.Fprintf(w, "Hello astaxie!")
}

func main() {
  http.HandleFunc("/", sayhelloName)
  err := http.ListenAndServe(":9090", nil) // 第二个参数是handler，传递nil时会调用默认的DefaultServerMux，即一个路由器
  if err != nil {
    log.Fatal("ListenAndServer:", err)
  }
}
