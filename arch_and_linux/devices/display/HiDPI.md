[ref](https://wiki.archlinux.org/index.php/HiDPI)

Add `xrdb -merge ~/.Xresources` to ~/.xinitrc

Grub:
```shell
# Generate a new GRUB font
grub-mkfont -s 30 -o /boot/grubfont.pf2 /usr/share/fonts/TTF/times.ttf
```
