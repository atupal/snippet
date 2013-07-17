tarball方式安装tmux


```
#!/bin/bash
#
# Install tmux 1.6 on Ubuntu 10.04
#
# Ref: http://bionicraptor.co/2011/07/23/how-to-compiling-tmux-1-5-for-ubuntu-10-04/
#
DOWNLOAD_URL="http://downloads.sourceforge.net/project/tmux/tmux/tmux-1.6/tmux-1.6.tar.gz?r=http%3A%2F%2Ftmux.sourceforge.net%2F&ts=1326463650&use_mirror=jaist"
 
sudo apt-get install build-essential debhelper diffstat dpkg-dev fakeroot g++ g++-4.4 html2text intltool-debian libmail-sendmail-perl libncurses5-dev libstdc++6-4.4-dev libsys-hostname-long-perl po-debconf quilt xz-utils libevent-1.4-2 libevent-core-1.4-2 libevent-extra-1.4-2 libevent-dev
 
wget $DOWNLOAD_URL -O tmux-1.6.tar.gz
 
tar xvvf tmux-1.6.tar.gz
 
cd tmux-1.6/
./configure --prefix=/usr
make
sudo make install
```

- 然后执行：`wget -q -O - https://raw.github.com/gist/2204072/install_tmux_1.6_on_ubuntu_10.04.sh | sudo bash`
