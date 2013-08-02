
package main

import (
  "fmt"
  "strconv"
)

type Element interface{}
type list [] Element

type Person struct {
  name string
  age int
}

func (p Person) String() string {
  return "<name:" + p.name + "- age:" + strconv.Itoa(p.age) + "years>"
}

func main() {
  list := make(list, 3)
  list[0] = 1
  list[1] = "Hello"
  list[2] = Person{"Dennis", 70}

  for index, element := range list {
    switch  value := element.(type) {
    case int:
      fmt.Printf("list[%d] is an int, %s\n", index, value)
    case string:
      fmt.Printf("list[%d] is a string  %s\n", index, value)
    case Person:
      fmt.Printf("list[%d] is a person %s\n", index, value)
    default:
      fmt.Println("list[%d] is a type %s\n", index, value)
    }
  }
}
