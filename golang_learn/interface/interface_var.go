
package main

import (
  "fmt"
  "strconv"
)

type Human struct {
  name string
  age int
  phone string
}

func (h Human) String() string {
  return "<" + h.name + " - " + strconv.Itoa(h.age) + " years -  call:" + h.phone + ">"
}

/*
当实现了erro方法时， fmt输入会调用Error方法
func (h Human) Error() string 
  return " error: <" + h.name + " - " + strconv.Itoa(h.age) + " years -  call:" + h.phone + ">"
}
*/

func main() {
  Bob := Human{ "Bob", 39, "000-777-xxx" }
  fmt.Println("This Human is :", Bob)
}

