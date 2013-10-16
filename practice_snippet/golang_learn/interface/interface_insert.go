
package main

import "fmt"
import "sort"

type Interface interface {
  sort.Interface // 嵌入字段sort.Interface
  Push(x interface{})
  Pop() interface{}
}


/* 以下就是sort.Interface的字段*/
type Interface_2 interface{
  Len() int
  Less(i, j int) bool
  Swap(i, j int)


func main() {
  fmt.Println("hehe")
}
