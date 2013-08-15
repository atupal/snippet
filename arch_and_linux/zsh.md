
```
Miscellaneous: Zsh: prompts

(last edit: 2001-03-18)
                   You can alter your zsh 'PS1', 'PS2', 'PS3' and 'PS4' prompts via the command line or your
'~/.zshrc' file by resetting the value of the matching shell variable. This is e.g. '$PS1' 
for the 'PS1' prompt.

E.g.:

user@host:~#export PS1="%m [%n] %d>"

Would generate a default prompt like this:

lowlife [jappe] /home/jappe>

This is how my '.zshrc' looks like:

----
export PS1="%m [%n] %d>"
setopt AUTOLIST
----

You can type the same command on the command line instead of putting it in your '~/.zshrc'.

Here are some options and explanations extracted from the 'zshparam' man page:

PS1    The  primary prompt string, printed before a command is read; the default is "%m%# ". 

                      %d
                      %/     Present working directory ($PWD).
                      %M     The full machine hostname.
                      %m     The hostname up to  the  first  '.'.
                             An  integer  may  follow  the '%' to
                             specify how many components  of  the
                             hostname are desired.
                      %@     Current  time  of  day,  in 12-hour,
                             am/pm format.
                      %T     Current time of day, in 24-hour for-
                             mat.
                      %*     Current  time of day in 24-hour for-
                             mat, with seconds.
                      %n     $USERNAME.
                      %w     The date in day-dd format.
                      %W     The date in mm/dd/yy format.
                      %D     The date in yy-mm-dd format.

PS2    The secondary prompt, printed when the shell needs more information to  complete  
       a  command.   Recognizes the same escape sequences as $PS1.  The default is "%_> ", 
       which  displays  any  shell  constructs  or  quotation marks which are currently 
       being processed.

PS3    Selection prompt used within a select  loop. Recognizes  the  same  escape  sequences
       as $PS1.  The default is "?# ".

PS4    The execution trace prompt.  Default  is  "+".

```
