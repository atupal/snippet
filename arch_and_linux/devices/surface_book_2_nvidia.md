https://wiki.archlinux.org/index.php/NVIDIA
https://wiki.archlinux.org/index.php/nouveau#Keep_NVIDIA_driver_installed

```
nvidia-xconfig # will create the /etc/X11/xorg.conf file
lspci -nnk # make sure the nvidia driver is used
```

$ sudo pacman -S nvidia
[sudo] password for atupal: 
resolving dependencies...
looking for conflicting packages...
warning: dependency cycle detected:
warning: eglexternalplatform will be installed before its nvidia-utils dependency

Packages (4) egl-wayland-1.1.0-1  eglexternalplatform-1.0+3+g7c8f8e2-1  nvidia-utils-410.57-3  nvidia-410.57-6

Total Download Size:    50.90 MiB
Total Installed Size:  194.33 MiB

:: Proceed with installation? [Y/n] Y
:: Retrieving packages...
 eglexternalplatform-1.0+3+g7c8f8e2-1-any                                                   6.9 KiB  0.00B/s 00:00 [####################################################################] 100%
 egl-wayland-1.1.0-1-x86_64                                                                20.1 KiB   543K/s 00:00 [####################################################################] 100%
 nvidia-utils-410.57-3-x86_64                                                              39.9 MiB  2.07M/s 00:19 [####################################################################] 100%
 nvidia-410.57-6-x86_64                                                                    11.0 MiB  2.92M/s 00:04 [####################################################################] 100%
(4/4) checking keys in keyring                                                                                     [####################################################################] 100%
(4/4) checking package integrity                                                                                   [####################################################################] 100%
(4/4) loading package files                                                                                        [####################################################################] 100%
(4/4) checking for file conflicts                                                                                  [####################################################################] 100%
(4/4) checking available disk space                                                                                [####################################################################] 100%
:: Processing package changes...
(1/4) installing eglexternalplatform                                                                               [####################################################################] 100%
(2/4) installing egl-wayland                                                                                       [####################################################################] 100%
(3/4) installing nvidia-utils                                                                                      [####################################################################] 100%
If you run into trouble with CUDA not being available, run nvidia-modprobe first.
Optional dependencies for nvidia-utils
    nvidia-settings: configuration tool
    xorg-server-devel: nvidia-xconfig [installed]
    opencl-nvidia: OpenCL support [installed]
(4/4) installing nvidia                                                                                            [####################################################################] 100%
:: Running post-transaction hooks...
(1/5) Updating linux module dependencies...
(2/5) Updating manpage index...
(3/5) Reloading system manager configuration...
(4/5) Creating system user accounts...
(5/5) Arming ConditionNeedsUpdate...









$ sudo pacman -S nvidia-dkms
resolving dependencies...
looking for conflicting packages...
:: nvidia-dkms and nvidia are in conflict. Remove nvidia? [y/N] y

Packages (2) nvidia-410.57-6 [removal]  nvidia-dkms-410.57-6

Total Download Size:    9.85 MiB
Total Installed Size:  27.41 MiB
Net Upgrade Size:      16.21 MiB

:: Proceed with installation? [Y/n] Y
:: Retrieving packages...
 nvidia-dkms-410.57-6-x86_64                                                                9.9 MiB  1160K/s 00:09 [####################################################################] 100%
(1/1) checking keys in keyring                                                                                     [####################################################################] 100%
(1/1) checking package integrity                                                                                   [####################################################################] 100%
(1/1) loading package files                                                                                        [####################################################################] 100%
(1/1) checking for file conflicts                                                                                  [####################################################################] 100%
(2/2) checking available disk space                                                                                [####################################################################] 100%
:: Processing package changes...
(1/1) removing nvidia                                                                                              [####################################################################] 100%
(1/1) installing nvidia-dkms                                                                                       [####################################################################] 100%
Optional dependencies for nvidia-dkms
    linux-headers: Build the module for Arch kernel [installed]
    linux-lts-headers: Build the module for LTS Arch kernel
:: Running post-transaction hooks...
(1/3) Updating linux module dependencies...
(2/3) Install DKMS modules
==> dkms install nvidia/410.57 -k 4.7.2-1-ARCH
Error! Bad return status for module build on kernel: 4.7.2-1-ARCH (x86_64)
Consult /var/lib/dkms/nvidia/410.57/build/make.log for more information.
==> dkms install nvidia/410.57 -k 4.18.14-surface
==> dkms install nvidia/410.57 -k 4.18.14-arch1-1-ARCH
(3/3) Arming ConditionNeedsUpdate...
# atupal at atupal in /home/atupal [1:36:27]



```shell
sudo pkgfile -u
pkgfile nvidia-settings
# Packages (2) libxnvctrl-410.57-2  nvidia-settings-410.57-2
```
##### Workaround

Above nvidia package and drivers doesnt' work.
So just disabled the nvidia card on BIOS (Devices - DGPU): Google "arch linux disable nvidia card"
https://www.reddit.com/r/archlinux/comments/5dmq8q/how_to_completely_disable_nvidia/
https://bbs.archlinux.org/viewtopic.php?id=218917

~and block the nouveau driver:~(no need and no use, nouveau driver still loads, also see `modinfo nouveau`)
```shell
# https:/wiki.archlinux.org/index.php/nouveau#Keep_NVIDIA_driver_installed
create /etc/modprobe.d/nouveau_blacklist_surface_book_2.conf
add:
blacklist nouveau
```

Now the nvidia card doesn't hot anymore, and windows 10 works fine since it doesn't use this GPU from exising usage experence.
