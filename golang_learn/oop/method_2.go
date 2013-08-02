
package main

import (
  "fmt"
)

const (
  WHITE = iota
  BLACK
  BLUE
  RED
  YELLOW
)

type Color byte

type Box struct {
  width, height, depth float64
  color Color
}

type BoxList []Box   // a slice of boxes

func (b Box) Volume() float64 {
  return b.width * b.height * b.depth
}

func (b *Box) SetColor(c Color) {
  b.color = c
}

func (b1 BoxList) BiggestColor() Color{
  v := 0.00
  k := Color(WHITE)
  for _, b := range b1 {
    if b.Volume() > v {
      v = b.Volume()
      k = b.color
    }
  }
  return k
}

func (b1 BoxList) PaintItBlack() {
  for i, _ := range b1 {
    b1[i].SetColor(BLACK)
  }
}

func  (c Color) String() string {
  strings := []string {"WHITR", "BLACK", "RED", "YELLOW"}
  return strings[c]
}

func main() {
  boxes := BoxList {
    Box{4, 4, 4, RED},
    Box{10, 10, 1, YELLOW},
    Box{1, 1, 20, BLACK},
    Box{10, 10, 1, BLUE},
    Box{10, 30, 1, WHITE},
    Box{20, 20, 20, YELLOW},
  }
  fmt.Printf("We have %d boxes\n", len(boxes))
  fmt.Println("The volume of the first one is", boxes[0].Volume(), "cm")
  fmt.Println("The color of last one is", boxes[len(boxes)-1].color.String())
  fmt.Println("The biggest one is ", boxes.BiggestColor().String())

  fmt.Println("Lest's painy thm all black")
  boxes.PaintItBlack()
  fmt.Println("The color of the second one is ", boxes[1].color.String())
  fmt.Println("OBvioursly, now the biggest one is", boxes.BiggestColor().String())
}

