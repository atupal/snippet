
https://github.com/NickTomlin/pocketvim



```
you can get editor editor object with 
document.querySelector(".ace_editor.ace-github").env.editor 
but setKeyboardHandler won't work since they use old ace version, so 
you need to do this 

ace.require("ace/lib/net").loadScript("https://rawgithub.com/ajaxorg/ace-builds/master/src-min-noconflict/keybinding-vim.js", 
function() { 
    e = document.querySelector(".ace_editor.ace-github").env.editor; 
    e.setKeyboardHandler(ace.require("ace/keyboard/vim").handler); 
}) 
```
