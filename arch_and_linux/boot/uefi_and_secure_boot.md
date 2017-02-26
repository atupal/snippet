Ref:
- https://gist.github.com/atupal/07278ff178528f8fce6b1de9149acf88
- https://wiki.archlinux.org/index.php/Secure_Boot#PreLoader

PreLoader:

```
cp /usr/share/preloader-signed/{PreLoader,HashTool}.efi esp/EFI/grub
cp esp/EFI/grub/grubx64.efi esp/EFI/grub/loader.efi

# Replace X with the drive letter and replace Y with the partition number of the EFI System Partition.
efibootmgr --disk /dev/sdX --part Y --create --label "PreLoader" --loader /EFI/systemd/PreLoader.efi
# use "efibootmgr" or "bootctl status" to check the result.

# When first start the PreLoader, use HashTool for enrolling the hash of loader.efi
```
