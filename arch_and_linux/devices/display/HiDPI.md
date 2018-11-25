[ref](https://wiki.archlinux.org/index.php/HiDPI)

Add `xrdb -merge ~/.Xresources` to ~/.xinitrc

# One time change
```
xrandr --output eDP1 --scale 0.25x0.25 # Zoom out 4 times
```

# Grub:
```shell
# https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Setting_the_framebuffer_resolution
# Run videoinfo from grub shell
# Set following to /etc/default/grub
GRUB_GFXMODE=1280x1024x32
GRUB_GFXPAYLOAD_LINUX=keep

grub-mkconfig -o /boot/grub/grub.cfg # Or add 'set gfxmode=1280x1024x32' to replace 'set gfxmode=auto'
```
