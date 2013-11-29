
[link](http://vim.wikia.com/wiki/Map_caps_lock_to_escape_in_XWindows?file=Ubuntu-swap-esc-capslock.png)

use 
```
xev
```
to get test

or 
```
xmodmap -pke > ~/.Xmodmap
vim ~/.Xmodmap
```
and add 
```
clear lock
keycode 66 = Esecape
```

then
```
xmodmap ~/.Xmodmap
```
