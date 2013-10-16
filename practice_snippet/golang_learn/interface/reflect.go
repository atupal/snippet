
package main

import "fmt"
import "reflect"

/*
  go语言实现了反射，所谓反射就是动态运行时的状态 , 我们一般用到的包是reflect包，
*/


func main() {

  var x float64 = 3.4
  v := reflect.ValueOf(x)
  fmt.Println("type:", v.Type())
  fmt.Println("kind is float64:", v.Kind() == reflect.Float64)
  fmt.Println("value:", v.Float())

  /*  
      t := reflect.TypeOf(i)
      v := reflect.ValueOf(i)

 

      var x float64 = 3.4
      p := reflect.ValueOf(x)
      v := p.Elem()
      v.SetFloat(7.1)
  */

  //name := v.Elem().Field(0).String()
  //fmt.Println(tag, name)

}

