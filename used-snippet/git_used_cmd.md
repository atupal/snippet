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
