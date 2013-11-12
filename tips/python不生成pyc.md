设置如下环境变量：
```
export PYTHONDONTWRITEBYTECODE=x
```
便可以使得在导入模块时不编译为pyc文件

如果出现`easy_install fails with byte-compiling disabled`错误一般是设置了这个环境变量的原因
`export PYTHONDONTWRITEBYTECODE=` 就好了
