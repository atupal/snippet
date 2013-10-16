package main

import (
  "fmt"
)

func main() {
  var a rune // rune is a alias of int32 , byte is a alias of uint8
             // int8, int16, int32, int64, uint8, uint16, uint32, uint64
  a = 1
  c := "hello"
  d := []byte(c)
  fmt.Println(d[0], a)

  i := 1234
  fmt.Println(i)

  j := int32(1)
  fmt.Println(j)

  f := float32(3.14)
  fmt.Println(f)

  bytes := [5]byte{'h', 'e', 'l', 'l', 'o'} //type: [5]type
  fmt.Println("%s", bytes)

  primes := [4]int{1,2,3,4} //type: [4]int
  fmt.Println(primes)

}

