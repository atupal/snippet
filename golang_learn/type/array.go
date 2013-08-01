
//var arr [n]type

package main
import "fmt"

var arr [10]int

func main() {
  arr[0] = 42
  arr[1] = 14
  fmt.Printf("%d", arr[0])
  fmt.Printf("\n%d", arr[1])

  a := [3]int{1, 2, 3}
  b := [10]int{1, 2, 3}
  c := [...]int{4 ,5 ,6}
  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)

  doubleArray := [2][4]int{ [4]int{1,2,3,4}, [4]int{5, 6, 7, 8} }
  fmt.Println(doubleArray[1][0])

  easyArray := [2][4]int{ {1, 2, 3, 4}, {4, 5, 6, 7} }
  fmt.Println(easyArray)

}
