
var http = require("http")

//1

/*
http.createServer(function( request, response ){
  response.writeHead(200, {"Context-Type": "text/plain"})
  response.write("Hello World!")
  response.end()
}).listen(8000)
*/

//2

function onRequest(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.wirte("Hello World");
  response.end()
}

http.createServer(onRequest).listen(8000)
