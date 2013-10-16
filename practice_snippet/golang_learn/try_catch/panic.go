
package main

import (
  "fmt"
  "os"
)

var user = os.Getenv("USER")

func main() {
  if user == "" {
    panic("no value for $USER")
  } else {
    fmt.Println("$USER =", user)
  }
}

