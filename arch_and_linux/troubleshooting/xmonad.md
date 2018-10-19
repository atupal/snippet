After library uprade, need to recompile the xmonad:

[Note: Remember to run xmonad --recompile after you upgrade xmonad, otherwise it might have problems finding shared libraries the next time you start it.](https://wiki.archlinux.org/index.php/xmonad#Installation)

```
xmonad --recompile
```

https://wiki.archlinux.org/index.php/xmonad#Problems_with_finding_shared_libraries_after_update
```
sudo ghc-pkg recache
```

But ghc-pkg recache throw following error:

> ignoring (possibly broken) abi-depends field for packages

Try 
```
ghc-pkg --help
```
Then found:
```
sudo ghc-pkg check
```
Got following error
> Warning: haddock-interfaces: /usr/share/doc/ghc/html/libraries/base-4.11.1.0/base.haddock doesn't exist or isn't a file
> ...
>The following packages are broken, either because they have a problem
>listed above, or because they depend on a broken package.
>xmonad-contrib-0.14
>xmonad-0.14
>  errno: 1

https://stackoverflow.com/questions/7961604/fixing-issues-noted-by-ghc-pkg-check

Above link doesn't help.

### Solution:

Upgrade the system which also upgraded the GHC and GHC-libs and xmonad. And `xmonad --recompile`. Maybe reinstall the packages will also
solve this issue.

```shell
Packages (68) alex-3.2.4-5  archlinux-keyring-20181018-1  cabal-install-2.4.0.0-2  chromium-70.0.3538.67-1  erlang-nox-21.1.1-1  ghc-8.6.1-1  ghc-libs-8.6.1-1  happy-1.19.9-5  haskell-async-2.2.1-3
              haskell-base16-bytestring-0.1.1.6-10  haskell-base64-bytestring-1.0.0.1-13  haskell-cryptohash-sha256-0.11.101.0-5  haskell-data-default-0.7.1.1-16  haskell-data-default-class-0.1.2.0-9
              haskell-data-default-instances-base-0.1.0.1-9  haskell-data-default-instances-containers-0.0.1-21  haskell-data-default-instances-dlist-0.0.1-29  haskell-data-default-instances-old-locale-0.0.1-21
              haskell-digest-0.0.1.2-10  haskell-dlist-0.8.0.5-2  haskell-echo-0.1.3-7  haskell-ed25519-0.0.5.0-9  haskell-edit-distance-0.2.2.1-10  haskell-exceptions-0.10.0-7
              haskell-extensible-exceptions-0.1.1.4-21  haskell-hackage-security-0.5.3.0-30  haskell-hashable-1.2.7.0-4  haskell-http-4000.3.12-74  haskell-network-2.7.0.2-12  haskell-network-uri-2.6.1.0-14
              haskell-old-locale-1.0.0.7-15  haskell-old-time-1.1.0.3-15  haskell-random-1.1-13  haskell-resolv-0.1.1.1-15  haskell-setlocale-1.0.0.8-2  haskell-tar-0.5.1.0-4  haskell-temporary-1.3-13
              haskell-transformers-compat-0.6.2-3  haskell-utf8-string-1.0.1.1-9  haskell-x11-1.9-2  haskell-x11-xft-0.3.1-37  haskell-zip-archive-0.3.3-9  haskell-zlib-0.6.2-4  jdk8-openjdk-8.u192-1
              jre8-openjdk-8.u192-1  jre8-openjdk-headless-8.u192-1  lib32-libdrm-2.4.96-1  libdrm-2.4.96-1  libnghttp2-1.34.0-1  nodejs-10.12.0-1  opera-56.0.3051.52-1  python2-colorama-0.4.0-1
              python2-gevent-1.3.7-1  python2-pbr-5.0.0-1  sdl2-2.0.8-10  tmux-2.8-1  xf86-input-libinput-0.28.1-1  xkeyboard-config-2.25-1  xmonad-0.15-2  xmonad-contrib-0.15-2  xorg-server-1.20.2-1
              xorg-server-common-1.20.2-1  xorg-server-devel-1.20.2-1  xorg-server-xdmx-1.20.2-1  xorg-server-xephyr-1.20.2-1  xorg-server-xnest-1.20.2-1  xorg-server-xvfb-1.20.2-1  xorg-server-xwayland-1.20.2-1
```
