#!/bin/bash
cd ./vim
make distclean
./configure --prefix=$HOME/bin/vim74 \
         --with-features=huge \
         --enable-rubyinterp \
         --enable-pythoninterp \
         --enable-perlinterp \
         --enable-gui=gtk2 \
         --enable-cscope \
         --enable-luainterp \
         --enable-multibyte \
         --enable-xim \
         --enable-fontset
         
         
make VIMRUNTIMEDIR=/usr/share/vim/vim73
