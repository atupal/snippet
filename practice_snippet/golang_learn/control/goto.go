
package main

import "fmt"

func main() {
  i := 0
  goto here
  i = 2
  here:
  i = 3
  fmt.Println(i)
}

