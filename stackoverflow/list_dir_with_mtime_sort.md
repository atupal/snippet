```
var files = fs.readdirSync(dir)
              .map(function(v) { 
                  return { name:v,
                           time:fs.statSync(dir + v).mtime.getTime()
                         }; 
               })
               .sort(function(a, b) { return a.time - b.time; })
               .map(function(v) { return v.name; });
```

simple:
```
var dir = './'; // your directory

var files = fs.readdirSync(dir);
files.sort(function(a, b) {
               return fs.statSync(dir + a).mtime.getTime() - 
                      fs.statSync(dir + b).mtime.getTime();
           });
```
