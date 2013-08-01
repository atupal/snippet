
package main

import (
  "fmt"
  "errors"
)

func main() {
  err := errors.New("_error")
  if err != nil {
    fmt.Println(err)
  }
}

