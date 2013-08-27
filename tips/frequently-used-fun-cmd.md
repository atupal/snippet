```
Nested X session
To run a nested session of another desktop environment:
/usr/bin/Xnest :1 -geometry 1024x768+0+0 -ac -name Windowmaker & wmaker -display :1


Virtual X session
To start another X session in, for example, Ctrl+Alt+F8, you need to type this on a console:
xinit /path/to/wm -- :1

挂载windos上的共享目录
mount -t cifs -o username=easwy //windows-server/share /mnt/winshare

关闭触摸板
sudo modprobe -r psmouse

设置库搜索路径，或者直接编辑/etc/ld.so.conf
export LD_LIBRARY_PATH=/opt/gtk/lib:$LD_LIBRARY_PATH

可以用pdb或者ipdb(ipython)来调试python程序，当然也有一个神奇pudb，console下的python debugger，用法如下：
python -m pudb.run my-script.py

设置双屏（DVI-0和1的名字可以看xrandr的输出结果）
xrandr --auto --output DVI-0 --mode 1440x900 --right-of DVI-1
切换屏幕
 xrandr --output $IN --off --output $EXT --auto

vim更新帮助文档
vim -c "helptags ~/.vim/doc" -c "q"

diff两个目录
diff -ruNa s1 s2 > s12.diff

查看端口被那个进程使用：
lsof -i TCP:80


vim替换成换行
:s/abcde/abc^Mde/

你需要输入CTRL-V <CR>来得到这里的 ^M(<CR>即回车键)

或者

:s/abcde/abc\rde/
```
