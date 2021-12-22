See [Power management/Suspend and hibernate](https://wiki.archlinux.org/index.php/Power_management/Suspend_and_hibernate#High_level_interfaces) for more details.

### Auto connect to network
```bash
systemctl enable wicd
```

### Swap file

[Creat a swap file:](https://wiki.archlinux.org/index.php/Swap#Swap_file)

```bash
# Tip: You might want to decrease the Swap#Swappiness for your swapfile
#      if the only purpose is to be able to hibernate and not expand RAM.
fallocate -l 8G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile

# vim /etc/fstab
/swapfile none swap defaults 0 0

# change the swappiness
sysctl vm.swappiness=10

# To set the swappiness value permanently, edit a sysctl configuration file
/etc/sysctl.d/99-sysctl.conf
vm.swappiness=10
```

>Note: Sometimes if the hibernate failed, it might because the swap is small, try to use swap sapce = 2 * memory.

### Required kernel parameters
```bash
# vim /boot/efi/grub/grub.cfg, add following parameters in the linux/kernel line
resume=/dev/sda5
# Using a swap file instead of a swap partition requires 
# an additional kernel parameter resume_offset=swap_file_offset
## The The resume kernel parameter specifies the device of the partition 
## that contains the swap file, not swap file itself! The parameter resume_offset
## informs the system where the swap file starts on the resume device.
## Before the first hibernation a reboot is required for them to be active.
filefrag -v /swapfile
resume_offset=xxxxxx
```
Or update `/etc/default/grub` to generate grub.cfg automatically:
```
Using a swap file requires also setting the resume=swap_device and additionally a resume_offset=swap_file_offset kernel parameters
The following command may be used to identify swap_device: findmnt -no UUID -T /swapfile
The following command may be used to identify swap_file_offset: filefrag -v /swapfile | awk '$1=="0:" {print substr($4, 1, length($4)-2)}'
```

### Configure the initramfs
```bash
# vim /etc/mkinitcpio.conf
HOOKS="base udev resume autodetect modconf block filesystems keyboard fsck"
sudo mkinitcpio -p linux
```

### Sleep or hibernate
```bash
systemctl hybrid-sleep
# or
systemctl hibernate
```
