### [kernel/Makefile:159: kernel/kheaders_data.tar.xz] Error 127
Full error:
```
# atupal at atupal in /home/atupal/kernel/linux-surface/pkg/arch/kernel/src/archlinux-linux [4:48:31]
$ make -j 1
  CALL    scripts/checksyscalls.sh
  CALL    scripts/atomic/check-atomics.sh
  DESCEND objtool
  CHK     include/generated/compile.h
  CC      kernel/configs.o
  AR      kernel/built-in.a
  CHK     kernel/kheaders_data.tar.xz
  GEN     kernel/kheaders_data.tar.xz
make[1]: *** [kernel/Makefile:159: kernel/kheaders_data.tar.xz] Error 127
make: *** [Makefile:1868: kernel] Error 2
```
G'[kernel/Makefile:159: kernel/kheaders_data.tar.xz] Error 127':

https://bbs.archlinux.org/viewtopic.php?id=261876 indicate that the root cause is because "cpio" package is not installed, which is required by the Makefile target (from the error line 159 in the Makefile):
https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/kernel/gen_kheaders.sh?h=v5.10.1

Installing the package sovles the issue. Also see https://bugs.gentoo.org/701678

The Arch Surface kernel PKGBUILD listed "cpio" as a dependency: https://github.com/linux-surface/linux-surface/blob/8970960cde1699c9e9e77f40440357f1b4725896/pkg/arch/kernel/PKGBUILD

> The actual build error was further up in the terminal readout. Since you had four threads, the others kept going until they finished, so the actual error is behind all those. so try scrolling back or using one thread so you can see the error (G'kernel compilation error 2' - https://github.com/jakeday/linux-surface/issues/593)
