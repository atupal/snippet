
package main

import "fmt"

//var fslice []int

func main() {
  //slice := []byte {'a', 'b', 'c', 'd'}
  var ar = [10]byte{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
  var a, b []byte

  a = ar[2:5]
  b = ar[3:5]
  a[0] = 33 // 这里的ar中的值也会改变，这点和python不一样, 虽然没有可比性, go 里面的slice是引用类型
  fmt.Println(ar)
  fmt.Println(a)
  fmt.Println(b)
}

