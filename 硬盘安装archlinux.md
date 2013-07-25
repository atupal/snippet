```
硬盘安装 Arch Linux


此前使用 Chakra Linux，其启动引导器为 BURG，它是基于 GRUB2 使用 Ruby 重写而来的，所以 GRUB 命令同样适用。

    如果安装 Arch Linux 的时候没有网络，下面的方法可能适合你，首先下载一个 core 仓库镜像

    $ mkdir core && cd core
    $ wget http://mirrors.163.com/archlinux/core/os/x86_64/
    $ awk '{sub(/.*="/,"http://mirrors.163.com/archlinux/core/os/x86_64/"); {sub(/".*/,"")} if(NR>=5 && NR<=399)print}' index.html | xargs wget -c
    # pacman -Sw fuse freetype2 --cachedir . 

        创建一个名为“core”的文件夹
        会下载到一个 index.html 文件，即网易源 64 位 core 仓库的页面 html 文件
        使用 awk 对 index.html 文件的内容做下替换，输出传给 wget 下载
        下载 fuse freetype2 这两个属于 extra 仓的包，这是 grub 的依赖

把下载而来的 archlinux-(version)-dual.iso 复制到U盘的根目录，重启机器。

进入 BURG 引导界面，按 C 进入命令行模式。

loopback loop (hd1,msdos1)/archlinux-2012.11.01-dual.iso
linux (loop)/arch/boot/x86_64/vmlinuz archisolabel=ARCH2012_11
initrd (loop)/arch/boot/x86_64/archiso.img
boot

    loopback 把镜像挂载为 loop 设备，在此将其 iso 挂为 loop (可自定义)
    linux 指定内核，具体见 vmlinux
    initrd 指定临时文件系统，具体见 initrd
    boot 启动

启动过程提示找不到，得到一个 Shell，进行下面的操作

# mkdir/udisk
# mount -r -t vfat /dev/sdb1 /udisk
# modprobe loop
# losetup /dev/loop6 /udisk/archlinux-2012.11.01-dual.iso
# ln -s /dev/loop6 /dev/disk/by-label/ARCH2012_11
# exit

    创建 /udisk 目录
    把 U 盘挂载到 /udisk 目录
    载入 loop 模块
    把 ISO 映射为 loop 设备
    把 /dev/disk/by-label/ARCH2012_11 软链接到刚创建的 loop 设备
    退出 Shell

一切没有问题将会自动以 root 登录，目前 Arch Linux 的安装方式和 Gentoo 差不多，都通过 Change Root。
```
