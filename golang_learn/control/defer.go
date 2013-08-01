
package main

import "fmt"

/*
  defer : 延迟语句

*/

/*
  to read a file, we usuaualy:
*/

/*
func ReadWrite() bool {
  file.Open("file")
  if failureX {
    file.Close()
    return false
  }

  if failureY {
    file.Close()
    return false
  }

  file.Close()
  return true
}
*/

/*
  but with defer, we can:
*/

/*
func ReadWrite() bool {
  file.Open("file")
  defer file.Close()

  if failureX {
    return false
  }

  if failureY {
    return false
  }

  return true
}
*/

/*
  简单来说，defer就是在return 之前做一点事，有点像python的with块
  如果有多个defer， 则采取后进先出模式. 
  如一下例子
*/

func main() {
  for i := 0; i < 5; i ++ {
    defer fmt.Println(i)
  }
}
















