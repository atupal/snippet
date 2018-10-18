- grub-mkcfonig -> /dev/null wil cause /dev/null is overwritten by the grub config file, hence cause cat stop working:
```
cat /dev/null permission denied
```
Solution(https://unix.stackexchange.com/questions/146633/bash-dev-null-permission-denied):
```
rm -f /dev/null; mknod -m 666 /dev/null c 1 3
```
