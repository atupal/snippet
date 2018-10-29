Ref: http://askubuntu.com/questions/91426/reverse-two-finger-scroll-direction-natural-scrolling/685873#685873

Create file `/usr/share/X11/xorg.conf.d/20-natural-scrolling-touchpads.conf` and add:
```
Section "InputClass"
    Identifier "Natural Scrolling Touchpads"
    MatchIsTouchpad "on"
    MatchDevicePath "/dev/input/event*"
    Option "VertScrollDelta" "-111"
    Option "HorizScrollDelta" "-111"
EndSection
```
