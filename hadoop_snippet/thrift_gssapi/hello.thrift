
const string HELLO_1 = "hello1"
const string HELLO_2 = "hello2"
const string HELLO_3 = "hello3"

service HelloWorld {
  void ping(),
  string sayHello(),
  string sayMsg(1:string msg)
  }

