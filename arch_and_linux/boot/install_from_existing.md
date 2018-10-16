### Boot from USB *or* PXE

##### USB
Ref: https://gist.github.com/atupal/07278ff178528f8fce6b1de9149acf88

Make sure the secure boot is `disable` to boot from USB, but still use UEFI. Otherwise the USB cannot boot. (https://support.microsoft.com/en-us/help/4023511/surface-boot-surface-from-a-usb-device?os=windows-10&=undefined)
(Although my original USB can be booted from secure mode, but after I wippped it and using the newest archlinux iso,
it cannot be booted from secure mode either made with dd or [Rufus](https://wiki.archlinux.org/index.php/USB_flash_installation_media#Using_Rufus) tool)

##### PXE
....

### Install the system
##### Create and encypt the partition
```shell
cryptsetup -c aes-xts-plain64 -y --use-random luksFormat /dev/sdX3
cryptsetup luksOpen /dev/sdX3 luks
mkfs.ext4 /dev/mapper/luks
```
### Copy existing system files
Ref: https://wiki.archlinux.org/index.php/Rsync#Full_system_backup
```shell
# backup:
rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /path/to/backup/folder
# restore: (Note: don't miss the '/' at end of the "/path/to/backup/folder/", otherwise the result in "/mnt" is "/mnt/folder")
rsync -aAXv --exclude=/path/to/backup/folder{"/dev/*","/proc/*","/sys/*","/run/*","/media/*","/lost+found"} /path/to/backup/folder/ /mnt
```
##### Swap file
Ref: https://github.com/atupal/snippet/blob/master/arch_and_linux/systemd/Power_management.md

##### Install fstab
Ref: Ref: https://gist.github.com/atupal/07278ff178528f8fce6b1de9149acf88
```
genfstab -pU /mnt >> /mnt/etc/fstab
# Make /tmp a ramdisk (add the following line to /mnt/etc/fstab)
tmpfs	/tmp	tmpfs	defaults,noatime,mode=1777	0	0
# Change relatime on all non-boot partitions to noatime (reduces wear if using an SSD)
```

```
arch-chroot /mnt /bin/bash
```

##### mkinitcpio
```
# Configure mkinitcpio with modules needed for the initrd image
vim /etc/mkinitcpio.conf
# Add 'ext4' to MODULES
# Add 'encrypt' and 'lvm2' to HOOKS before filesystems

# Regenerate initrd image
mkinitcpio -p linux
```

### Install the boot loader
##### Install grub
Ref:https://wiki.archlinux.org/index.php/GRUB#Installation_2
```
grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB
```

> Note: if your `/boot` folder is in a seperated partion and not encrypted, then you can grub-install directly. But if the
> `/boot` partiton is encypted, you need to add `GRUB_ENABLE_CRYPTODISK=y` in `/etc/default/grub`, grub-install will also ask you do so.
> In encypted case, `/boot` not nessessary a separate partition, `/boot` is **not** required to be kept in a separate partition;
see https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Encrypted_boot_partition_.28GRUB.29
also see https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Encrypted_boot_partition_.28GRUB.29

If `/boot` is encypted, before entering grub menu, you need to input password to read the grub configuration file from `/boot`

##### Make the grub configuration file.
If the `/root` is encypted, you need to input the password after kernel loaded, which means you need to input password again if
`/boot` and `/root` is on the same encypted disk. So you can put `/boot` on a seperated unencypted partition to avoid input two
times password. Refer the partition plan on https://gist.github.com/atupal/07278ff178528f8fce6b1de9149acf88

In /etc/default/grub edit the line GRUB_CMDLINE_LINUX to GRUB_CMDLINE_LINUX="cryptdevice=/dev/sdX3:luks:allow-discards" then run:
```
grub-mkconfig -o /boot/grub/grub.cfg
```

##### Enroll UEFI key
Ref: https://github.com/atupal/snippet/blob/master/arch_and_linux/boot/uefi_and_secure_boot.md

##### Dual boot UEFI Windows 10
Ref: https://wiki.archlinux.org/index.php/GRUB#Windows_installed_in_UEFI.2FGPT_Mode_menu_entry
See also above sention of the uefi_and_secure_boot.md.

If `grub-probe --target=hints_string esp/EFI/Microsoft/Boot/bootmgfw.efi` complains unsupported device, use
`--hint-efi=hd0,gptX`, change X to the parition number of the EFI partion. (partition number from 1).

Every time you change the BIOS, include disable/enable secure boot and change the boot order, Windows 10 bitlcoker will
ask you input the bitlocker recovery key after the changes. But then future boot doesn't ask for the key. Either for Windows Boot Manager or Grub chainloader for Windows Boot Manager. Which is good, :), otherwiwe you can set a short PIN for the bitlocker if it
is needed at every boot :(.

### Post intalltion and troubleshotting
##### Kernal panic - not syncing: VFS: Unable to mount root fs on unkown-block(0,0).
Make sure the right vmlinuz-linux.bak, initramfs is loaded in grub.cfg, in my case, there is old vmlinuz-linux.bak, initramfs.bak under /boot folder and
`grub-mkconfig` use vmlinuz-linux.bak on the first menu.