
package main

import "fmt"

func max(a, b int) int {
  if a > b {
    return a
  }
  return b;
}

/*
  the func syntax:
  
  func funcNmae(input1 type1, input2 type2) (output1 type1, output2 type2) {
    //do something
    return value1, value2
  }

  // 如果只有一个返回值且不申明返回值变量，那么你可以省略包括返回值的括号
  
  func SumAndProduct(A, B int) (add int, multiplied int) {
    add = A + B
    multiplied = A * B
    return
  }

  func myfunc(arg ...int) {
    for _, n := range arg {
      fmt.Printf("the number is: %d\n", n)
    }
  }

  传形参传引用和C语言一样

*/

func main() {
  fmt.Println(max(1, 3))
}

