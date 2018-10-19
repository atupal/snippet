##### Kernel, see ../kernel/surface_book2_acpi_high_cpu.md
- /boot/vmlinuz-linux-surface-<kernel version>
- /boot/initramfs-linux-surface-<kernel version>.img
- /lib/modules/<kernel version>-surface/
- grub menu entry

##### /etc configuration files, see https://github.com/jakeday/linux-surface/tree/master/root/etc
- /etc/NetworkManager/conf.d/default-wifi-powersave-on-surface-book-2.conf
- /etc/NetworkManager/NetworkManager.conf # Backup to /etc/NetworkManager/NetworkManager.conf.default
- /etc/X11/xorg.conf.d/20-intel-surface-book-2.conf
- /etc/mkinitcpio.conf and `sudo mkinitcpio -k 4.18.14-surface -g /boot/initramfs-linux-surface-4.18.img` # already backuped to /etc/mkinitcpip.conf.resume before installing
- /etc/modprobe.d/ath10k-surface-book-2.conf
- /etc/udev/rules.d/98-keyboardscovers-surface-book-2.rules
- /etc/udev/rules.d/99-touchscreens-surface-book-2.rules

##### firmware, see https://github.com/jakeday/linux-surface/tree/master/firmware
- IPTS
```shell
mkdir -p /lib/firmware/intel/ipts # new directory
# Googld "archlinux get sku model": https://unix.stackexchange.com/questions/75750/how-can-i-find-the-hardware-model-in-linux
# cat /sys/devices/virtual/dmi/id/product_sku -> Surface_Book_1793
unzip -o /home/atupal/kernel/linux-surface-master/firmware/ipts_firmware_v101.zip -d /lib/firmware/intel/ipts/
```
- i915
```shell
mkdir -p /lib/firmware/i915 # backup to /lib/firmware/i915.ori
unzip /home/atupal/kernel/linux-surface-master/firmware/i915_firmware_kbl.zip -d /lib/firmware/i915/
```
- nvidia
```shell
mkdir -p /lib/firmware/nvidia/gp108 # backup to /lib/firmware/nvidia/gp108.ori
unzip -o /home/atupal/kernel/linux-surface-master/firmware/nvidia_firmware_gp108.zip -d /lib/firmware/nvidia/gp108/
```
- marvell
```shell
mkdir -p /lib/firmware/mrvl/ # backup to /lib/firmware/mrvl.ori
unzip -o /home/atupal/kernel/linux-surface-master/firmware/mrvl_firmware.zip -d /lib/firmware/mrvl/
```

##### Others
- Hibernate (This will solve the problem that the wifi doen't work after resume from hibernate, dmesg error: mwifiex_pcie, Status: reset)
```shell
cd /lib/systemd/system-sleep
touch sleep # and paste https://github.com/jakeday/linux-surface/blob/master/root/lib/systemd/system-sleep/sleep
chmod a+x /lib/systemd/system-sleep/sleep
```
- libwacom
TODO
