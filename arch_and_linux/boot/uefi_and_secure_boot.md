Ref:
- https://gist.github.com/atupal/07278ff178528f8fce6b1de9149acf88
- https://wiki.archlinux.org/index.php/Secure_Boot#PreLoader

> Note: In the entire article `esp` denotes the mountpoint of the [EFI system partition](https://wiki.archlinux.org/index.php/EFI_system_partition) aka ESP. From [GRUB](https://wiki.archlinux.org/index.php/GRUB) wiki.
>
> When you specify the loader using `/EFI/path`, don't confuse with the ESP, it is the absolute path of the ESP. So don't
> use the mount point path. `/EFI/path` is right, using `bootctl status` to check the paths of all entries.

> BTW, you may need to update the package beforing copying, otherwise the old package files may be rejected by the UEFI.
> For either PreLoader or Shim, you need to enroll the hash of grubefi bin at first boot time to supress future prompt.
## PreLoader:

```
cp /usr/share/preloader-signed/{PreLoader,HashTool}.efi esp/EFI/grub
cp esp/EFI/grub/grubx64.efi esp/EFI/grub/loader.efi

# Replace X with the drive letter and replace Y with the partition number of the EFI System Partition.
efibootmgr --disk /dev/sdX --part Y --create --label "PreLoader" --loader /EFI/systemd/PreLoader.efi
# use "efibootmgr" or "bootctl status" to check the result.

# When first start the PreLoader, use HashTool for enrolling the hash of loader.efi
```

## [Optional] Shim:
```
# When run, shim tries to launch grubx64.efi, 
# if MokList does not contain the hash of grubx64.efi or the key it is signed with, 
# shim will launch mmx64.efi
cp /usr/share/shim-signed/{shimx64,mmx64}.efi esp/EFI/grub
efibootmgr --disk /dev/sda --part 1 --create --label "Shim" --loader /EFI/grub/shimx64.efi
```

## Dual boot with windows 10 (doesn't work with bitblocker? Update: works on at least Windows 10, 1809, Surface Book 2)

Add to `grub.cfg` or `/boot/grub/custom.cfg` (see [Grub](https://wiki.archlinux.org/index.php/GRUB)):
```
if [ "${grub_platform}" == "efi" ]; then
	menuentry "Microsoft Windows Vista/7/8/8.1 UEFI-GPT" {
		insmod part_gpt
		insmod fat
		insmod search_fs_uuid
		insmod chain
		search --fs-uuid --set=root $hints_string $fs_uuid
		chainloader /EFI/Microsoft/Boot/bootmgfw.efi
	}
fi
```
