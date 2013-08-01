
package main

import "fmt"

func main() {
  var numbers map[string] int
  numbers = make(map[string]int) // 另一种申明方式
  numbers[`one`] = 1
  numbers["two"] = 2

  fmt.Println(numbers)
}

