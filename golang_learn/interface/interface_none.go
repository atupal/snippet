
package main

import "fmt"

var a interface{}

var i int = 5

/*
 空的interface可以存储任意类型的数值
*/


func main() {
  s := "Hello world"
  a = i
  a = s
  fmt.Println(a)
}
