[ref](https://wiki.archlinux.org/index.php/HiDPI)

Add `xrdb -merge ~/.Xresources` to ~/.xinitrc

Grub:
```shell
# Generate a new GRUB font
grub-mkfont -s 30 -o /boot/grubfont.pf2 /usr/share/fonts/TTF/times.ttf

# Edit /etc/default/grub and add
GRUB_FONT="/boot/grubfont.pf2"
grub-mkconfig -o /boot/grub/grub.cfg
```
