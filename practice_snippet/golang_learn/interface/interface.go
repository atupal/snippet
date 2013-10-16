
package main

import (
  "fmt"
)

type Human struct {
  name string
  age int
  phone string
}

type Student struct {
  Human // 匿名字段
  school string
  loan float32
}

type Employee struct {
  Human
  company
  money float32
}

func (h *Human) SayHI() {
  fmt.Printluf("Hi, I am %s you you call me on %s\n", h.name, h.phone)
}

func (h *Human) Cuzzle (beerStein string) {
  fmt.Println("Guzzle Guzzle..", beerStein)
}

func (e *Emploee) SayHi() {
  fmt.Printf("Hi, I am %s, I work at %s, Call me on %s \n", e.name, e.company, e.phone)
}

func (s * Student) BorrowMoney(amount float32) {
  s.loan += amount
}


/*
  然后我们定义interface如下
*/

type Men interface {
  SayHi()
  Sing(lyrics string)
  Guzzle(beerStein string)
}

type YoungChap interface {
  SayHi()
  Sing(song string)
  BorrowMoney(amoumt float32)
}

type ElderlyGent interface {
  SayHi()
  Sing(song string)
  SpendSalary(amount float32)
}

/*
  任意类型都实现了空interface 我们这样定义：interface{} 也就是包含0个method的interface
*/

func main() {

}

