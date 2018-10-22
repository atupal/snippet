`mkinitcpio -p linux`. For the fall back image, there is a warning:

```
==> WARNING: Possibly missing firmware for module: wd719x
```

But no this warning for defalt image. In `/etc/mkinitcpio.d/linux.preset`, the `fallback_options="-S autodetect"`.
And `mkinitcpio -S autodetect` also shows this warning. I guess maybe the autodetect will detect all kernel modules and
`wd719x` module (use `modinfo wd719x` to see the info of this module, it shows it contains firmware:       wd719x-risc.bin
firmware:       wd719x-wcs.bin, but the files doesn't exist) may lose the correspoding firmware.

##### Solution
Install the `wd719x-firmware` from AUR: lha, wd719x-firmware.

Now the warning of `mkinitcpio -S autodetect` is gone and the correspoding firmware files are installed: `/usr/lib/firmware/wd719x-risc.bin` and `/usr/lib/firmware/wd719x-wcs.bin`

Same with `aic94xx` module: install aic94xx-firmware.

##### Ref:G "Possibly missing firmware for module: wd719x"
https://bbs.archlinux.org/viewtopic.php?id=194977
https://wiki.archlinux.org/index.php/Mkinitcpio#Possibly_missing_firmware_for_module_XXXX

Note: install the package from AUR is same with following, the git repo just contains the PKGBUILD file and use `makepkg` to install it
https://gist.github.com/imrvelj/c65cd5ca7f5505a65e59204f5a3f7a6d
