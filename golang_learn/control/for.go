
package main

import "fmt"

func main() {
  sum := 0;
  for index:= 0; index < 10; index++ {
    sum += index
  }
  fmt.Println(sum)

  /*
    while as this:
      for expr: {
        // do something
      }

      break, continue also availble .
      and continue could add a tag.
  */

  /*
    for k,v:= range map {
      fmt.Println("key:", k)
      fmt.Println("value", v)
    }

    if you do not use k, then you can :
    for _, v := range map {
      fmt.Println(k)
    }
  */

}

