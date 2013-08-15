boxes download: http://www.vagrantbox.es

添加心的环境:

```
# 添加官方 box 镜像
$ vagrant box add lucid32 http://files.vagrantup.com/lucid32.box
# 为当前目录指定运行镜像，这里指定的是之前添加的 lucid32 镜像
$ vagrant init lucid32
# 启动虚拟环境
$ vagrant up
```

登陆:
```
vagrant ssh
```
