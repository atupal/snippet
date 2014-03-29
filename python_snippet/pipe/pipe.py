# -*- coding: utf-8 -*-

from socket import *  #导入socket包中的所有内容
from time import ctime #导入time包，同时在本地可使用ctime进行调用
import os,sys #导入os，sys包
HOST='localhost'	#定义主机
PORT=21567	#定义端口
BUFSIZ=1024 #定义缓冲区
ADDR=(HOST,PORT) #定义元组

tcpSerSock=socket(AF_INET,SOCK_STREAM)  #生成socket
tcpSerSock.bind(ADDR) #将地址及端口元组与socket绑定
tcpSerSock.listen(5) #监听用户请求

r,w=os.pipe()	 #定义管道，进程间通信就靠他了！

while True: #定义无限循环
    print "waiting ...."  #打印等待用户输入时的waiting
    try:	#检测可能的异常
    	tcpCliSock,addr=tcpSerSock.accept() #处理用户请求
    	os.write(w,"f") #在管道一侧写入字符“f”
    except:	#处理异常
    	sys.exit(0)	#如果发生异常将直接退出
    if os.fork():	 #在父进程中的处理
    	pass #跳过处理
    else:	#在子进程中的处理
        print 'con from :',addr #打印客户端信息
        while True: #定义无限循环
            data=tcpCliSock.recv(BUFSIZ) #从客户端接收1024大小的数据
	    os.write(w,data) #将数据写入到道道中
            if not data: #如果客户端没有任何输入，即直接回车或Ctrl+D
        	tcpSerSock.close()	#关闭客户端链接
                break	#跳出无限循环
            tcpCliSock.send('[%s] %s' %(ctime(),os.read(r,1024)))#否则回显用户信息并附加当前时间！

tcpSerSock.close() #这句话依然不会被执行。
