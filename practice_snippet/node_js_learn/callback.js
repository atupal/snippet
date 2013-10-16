
var fs = require('fs');
var EventEmitter = require('events').EventEmitter;
var event = new EventEmitter();

event.on('some_event', function() {
  console.log('some_event occured.');
});

fs.readFile('hello.js', 'utf-8', function(err, data) {  
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

fs.readFile('callback.js', 'utf-8', function(err, data) {  
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

setTimeout(function() {
  // while (1);
  event.emit('some_event')
}, 1000);

console.log('end. ');

