```
SSH端口转发（隧道）
此页由Linux Wiki用户Chenxing于2012年2月5日 (星期日) 03:31的最后更改。
SSH端口转发(Port Forwarding)，是一种隧道技术，流往某端口的数据被加密后传向另一机器，依据转发方式的不同，有多种应用场景。[1][2]

以下所有的命令都是用SSH客户端执行的。执行命令的电脑下面称为“本地”电脑；而“远程服务器”则是运行着SSH服务器的机器（本文以my-remote-host.com为例）。

目录
1 本地转发
2 远程转发
3 动态转发
4 常用参数
5 相关资料
本地转发
有时，远程机器能访问某个端口（如remote-secret.com:8080），但本地机器无法访问。这时使用SSH的本地转发功能，即可将远程端口映射到本地：

ssh -L 9090:remote-secret.com:8080 my-remote-host.com
此时访问本地的9090端口就相当于用远程服务器my-remote-host.com访问remote-secret.com:8080。

Hint.gif提示： 
如果写成-L 9090:localhost:8080，就是把远程服务器的8080端口映射到本地的9090端口了
应用举例：如果远程服务器处于某受保护的内网中，可以借助其SSH服务获得与其等同的访问权限。

Hint.gif提示： 
默认情况下，本地转发的端口只能在本机上访问，要想允许外部访问，请添加-g选项。
远程转发
让远程服务器监听remote_port端口，使其被访问时像本地电脑在访问somehost:its_port一样。

ssh -R 9090:local-secret.com:8080 my-remote-host.com
这样，访问my-remote-host.com:9090就等同于用本机访问local-secret.com:8080。

应用举例：有时，本地电脑处于NAT内网中，难以从外部访问；而远程服务器可轻易被访问。利用远程转发功能，可允许他人通过远程服务器间接访问本地电脑的某个端口。

Note.gif注意： 
类似本地转发，远程转发的端口默认也只能在远程服务器本机上访问，要想允许外部访问，可改写为-R *:9090:local-secrent.com:8080，并确保在服务器的sshd_config中打开了GatewayPorts选项。
动态转发
动态转发动态地将各种数据转发到远程端口。实际上相当于在本地电脑的指定端口开了一个SOCKS代理。如：

ssh -D 9090 my-remote-host.com
本地的9090端口就是一个SOCKS代理了。

Hint.gif提示： 
如果my-remote-host.com是境外服务器，则该SOCKS代理实际上具备了“翻墙”功能。
常用参数
端口转发常与以下参数配合使用[3]：

-f
ssh将在后台运行
-N
不执行命令，仅转发端口
-C
压缩传送的数据
-i
使用指定的密钥登录
```
