
package main

import "fmt"

const (
  x = iota // x = 0
  y = iota // y = 1
  z = iota // z = 2
  w // w = 3 默认和前一个字面相同， 即w = iota
)

const v = iota // 每遇到一个关键字，iota都会重置

const (
  e, f, g = iota, iota, iota // e=0, f=0, g=0 iota 在同一行值相同
)


func main() {
  fmt.Println(x)
  fmt.Println(y)
  fmt.Println(z)
  fmt.Println(w)
  fmt.Println(v)
  fmt.Println(e, f, g)
}
