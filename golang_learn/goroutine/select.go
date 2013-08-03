
package main
import "fmt"

func fib(c, quit chan int) {
  x, y := 1, 1
  for {
    select {
    case c <- x:
      x, y = y, x + y
    case <- quit:
      fmt.Println("quit")
      return
    //default:
    //  //当c和quit阻塞时执行这里
    }
  }
}

/*
  select 里面还有default方法， select其实就是类似switch的功能， default就是监听的channel都没有准备好的时候，默认执行的(select不再阻塞等待channel)
*/


func main() {
  c := make(chan int)
  quit := make(chan int)
  go func() {
    for i := 0; i < 10; i++ {
      fmt.Println(<-c)
    }
    quit <- 0
  }()
  fib(c, quit)
}
