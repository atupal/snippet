被 tracked 的文件加到 `.gitignore` 文件中是没有作用的。

我们可以使用以下命令忽略文件的改动：
```
git update-index --assume-unchanged <file>
```

用下面的命令则可以使忽略取消
```
git update-index --no-assume-unchanged <file>
```
