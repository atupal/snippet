
package main

import "time"

func main() {
  c := make(chan int)
  o := make(chan bool)
  go func() {
    for {
      select {
      case v := <-c:
        println(v)
      case <- time.After(5 * time.Second):
        println("timeout")
        o <- true
        break
      }
    }
  }()
  <-o
}

