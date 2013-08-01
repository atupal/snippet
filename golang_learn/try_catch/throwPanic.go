
package main


/*
  follow func will check function f is or not is throw a panic
*/
func throwsPanic(f func()) (b bool) {
  defer func() {
    if x := recover(); x != nil {
      b = true
    }
  }()
  f()
  return
}

func main() {
}
