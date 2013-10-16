
package main


/*
  ci := make(chan int)
  cs := make(chan string)
  cf := make(chan interface{})
  
  channel 通过 <- 来接受 和 发送数据
  ch <- v
  v := <-ch
*/

import "fmt"

func sum(a []int, c chan int) {
  total := 0
  for _, v := range a {
    total += v
  }
  c <- total
}

/*
  默认情况下 channel接受和发送数据都是堵塞的,除非另一端已经准备好，这样就使得Goroutines同步变的更加的简单， 而不需要显示的lock
  所谓堵塞，也就是如果读取(value := <-ch) ，它将被堵塞，直到有数据被接收，其次，任何发送(ch <-5)将会被堵塞，直到数据被读出，
*/

func main() {
  a := []int{1,2,3,4}
  c := make(chan int)
  go sum(a[:len(a)], c)
  go sum(a[len(a)/2:], c)
  x, y := <-c, <-c  // recieve from c

  fmt.Println(x, y, x + y)
}
