cancel a local git commit 
```
git reset HEAD^
PS: HEAD^ is equal to HEAD~1
```


fetch all branch from all remotes:
```
git pull --all
for remote in `git branch -r`; do git branch --track $remote; done
```


(gnome-ssh-askpass:13543): Gtk-WARNING **: cannot open display:

```shell
$ unset SSH_ASKPASS
```
