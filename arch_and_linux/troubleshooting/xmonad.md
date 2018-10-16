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
