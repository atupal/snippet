
package main

import "fmt"

func main() {
  i := 10
  switch i {
  case 1:
    fmt.Println(i)
    //by defualt, there is break
  case 2, 3, 4:
    fmt.Println(i)
    //by defualt, there is break
  default:
    fmt.Println("default")
  }

  /*
    if you want not break, you can:

    switch i {
    case 1:
      fmt.Println(i)
      fallthrough
     ...
    }
  */
}
