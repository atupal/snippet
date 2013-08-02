
package main

import (
  "fmt"
  "strconv"
)

type Element interface{}
type List []Element

type Person struct {
  name string
  age int
}

func (p Person) String() string {
  return "<name:" + p.name + "- age :" + strconv.Itoa(p.age) + "years"
}

func main() {
  list := make(List, 3)
  list[0] = 1
  list[1] = "Hello"
  list[2] = Person{"atupal", 19}
  for index, element := range list {
    if value, ok := element.(int); ok {
      fmt.Printf("list[%d] is an int and its value is %d\n", index, value)
    } else if value, ok := element.(string); ok {
      fmt.Printf("list[%d] is a string and its value is %s\n", index, value)
    } else  if value, ok := element.(Person); ok {
      fmt.Printf("list[%d] is a person and its value is %s\n", index, value)
    } else {
      fmt.Println("list[%d] is of a different type", index)
    }
  }
}
