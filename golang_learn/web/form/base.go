
package main

import (
  "fmt"
  "html/template"
  "log"
  "net/http"
)

func sayhelloName(w http.ResponseWriter, r *http.Request) {
  r.ParseForm()
  fmt.Println(r.Form)
  fmt.Println("path", r.URL.Path)
  fmt.Println("scheme", r.URL.Scheme)
  fmt.Println(r.Form["url_long"])
  for k, v := range r.Form {
    fmt.Println("key:", k)
    fmt.Println("val:", v)
  }
  fmt.Fprintf(w, "Hello ")
}

func login(w http.ResponseWriter, r *http.Request) {
  fmt.Println("method:", r.Method)
  if r.Method == "GET" {
    t, _ := template.ParseFiles("login.gtpl")
    t.Execute(w, nil)
  } else {
    //r.ParseForm()
    fmt.Println("username:", r.Form["username"])
    fmt.Println("password:", r.Form["password"])
  }
}

func main() {
  http.HandleFunc("/", sayhelloName)
  http.HandleFunc("/login", login)

  err := http.ListenAndServe(":9090", nil)
  if err != nil {
    log.Fatal("ListenAndServe:", err)
  }
}

/*
  request.Form是一个url.Values类型
  v := url.Values{}
  v.Set("name", "Ava")
  v.Add("friend", "Jess")
  v.Add("friend", "Sarah")
  v.Add("friend", "Zoe")
  fmt.Println(v.Get("name"))
  fmt.Println(v.Get("friend"))
  fmt.Println(v["friend"])
*/
