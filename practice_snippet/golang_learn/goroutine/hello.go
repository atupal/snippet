
package main

import (
  "fmt"
  "runtime"
)



/*
  runtime.Gosched() 表示让cpu把时间片让给别人，下次某个时候继续恢复执行该goroutine
*/
func  say(s string) {
  for i := 0; i < 5; i++ {
    runtime.Gosched()
    fmt.Println(s)
  }
}

func main() {
  go say("world") // 开一个新的Goroutines执行
  say("******") // 当前Goroutines执行
}
