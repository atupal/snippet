
package main

import "fmt"

type Human struct {
  name string
  age int
  phone string
}

type Student struct {
  Human
  school string
  loan float32
}

type Employee struct {
  Human
  company string
  money float32
}

func (h Human) SayHi() {
  fmt.Printf("Hi, I am %s you can call me %s" , h.name, h.phone)
}

func  (h Human) Sing(lyrics string) {
  fmt.Println("la la la. .", lyrics)
}

func (e Employee) SayHi() {
  fmt.Printf("Hi, I am %s, I work at %s, Call me on %s\n", e.name, e.company, e.phone)
}

type Men interface {
  SayHi()
  Sing(lyrics string)
}

func main() {
  mike := Student{ Human{"Mike", 25, "22-222-xxxx"}, "Mit", 0.00 }
  paul := Student{ Human{"paul", 26, "111-111=222"}, "Harvard", 100 }
  sam := Employee{ Human{"sam", 36, "444-222-xxx"}, "Golang inc", 1000 }
  Tom := Employee{ Human{"Tom", 36, "444-222-xxx"}, "Things ltd", 5000 }

  var i Men

  i = mike
  fmt.Println("This is mike, a student:")
  i.SayHi()
  i.Sing("November rain")

  i = Tom
  fmt.Println("this is tom, an rmployee:")
  i.SayHi()
  i.Sing("Born to be wildt ")

  fmt.Println("This is Tom, an Employee:")
  i.SayHi()
  i.Sing("Born to be wild")

  fmt.Println("Let's use a slice of Men and see what happens")
  x := make([]Men, 3)

  x[0], x[1], x[2] = paul, sam, mike

  for _, value := range x{
    value.SayHi()
  }
}
