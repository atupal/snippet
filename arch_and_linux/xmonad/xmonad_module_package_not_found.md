`xmonad --recompile` failed on
```
$ xmonad --recompile
XMonad will use ghc to recompile, because "/home/atupal/.xmonad/build" does not exist.
Error detected while loading xmonad configuration file: /home/atupal/.xmonad/xmonad.hs

xmonad.hs:1:1: error:
    Could not load module ‘XMonad’
    It is a member of the package ‘xmonad-0.15-KiSjBDh8avTDacDP4rBh9F’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs data-default-0.7.1.1-9TvgjOMl8fiEDpKR9EhMBO extensible-exceptions-0.1.1.4-KI0dG6kQM84KnSzvR2Yb0 setlocale-1.0.0.8-Eyi756ahEx7HLWAe3k6Ifg utf8-string-1.0.1.1-Geq8jdOv4Q3LkcQoEOWDVv
    Use -v to see a list of the files searched for.
  |
1 | import XMonad
  | ^^^^^^^^^^^^^

xmonad.hs:2:1: error:
    Could not load module ‘XMonad.Hooks.DynamicLog’
    It is a member of the package ‘xmonad-contrib-0.15-5nmUdwEZPvs1sNRJsezwdf’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs X11-xft-0.3.1-E2YofuHBPu4DXAPLYyOuZS extensible-exceptions-0.1.1.4-KI0dG6kQM84KnSzvR2Yb0 old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78 old-time-1.1.0.3-HsoRJMkCHriE79r63Cxfu4 random-1.1-3ypV4EIycgb35PKjTYYr5q utf8-string-1.0.1.1-Geq8jdOv4Q3LkcQoEOWDVv xmonad-0.15-KiSjBDh8avTDacDP4rBh9F
    Use -v to see a list of the files searched for.
  |
2 | import XMonad.Hooks.DynamicLog
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

xmonad.hs:3:1: error:
    Could not load module ‘XMonad.Hooks.ManageDocks’
    It is a member of the package ‘xmonad-contrib-0.15-5nmUdwEZPvs1sNRJsezwdf’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs X11-xft-0.3.1-E2YofuHBPu4DXAPLYyOuZS extensible-exceptions-0.1.1.4-KI0dG6kQM84KnSzvR2Yb0 old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78 old-time-1.1.0.3-HsoRJMkCHriE79r63Cxfu4 random-1.1-3ypV4EIycgb35PKjTYYr5q utf8-string-1.0.1.1-Geq8jdOv4Q3LkcQoEOWDVv xmonad-0.15-KiSjBDh8avTDacDP4rBh9F
    Use -v to see a list of the files searched for.
  |
3 | import XMonad.Hooks.ManageDocks
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

xmonad.hs:4:1: error:
    Could not load module ‘XMonad.Util.Run’
    It is a member of the package ‘xmonad-contrib-0.15-5nmUdwEZPvs1sNRJsezwdf’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs X11-xft-0.3.1-E2YofuHBPu4DXAPLYyOuZS extensible-exceptions-0.1.1.4-KI0dG6kQM84KnSzvR2Yb0 old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78 old-time-1.1.0.3-HsoRJMkCHriE79r63Cxfu4 random-1.1-3ypV4EIycgb35PKjTYYr5q utf8-string-1.0.1.1-Geq8jdOv4Q3LkcQoEOWDVv xmonad-0.15-KiSjBDh8avTDacDP4rBh9F
    Use -v to see a list of the files searched for.
  |
4 | import XMonad.Util.Run(spawnPipe)
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

xmonad.hs:5:1: error:
    Could not load module ‘XMonad.Util.EZConfig’
    It is a member of the package ‘xmonad-contrib-0.15-5nmUdwEZPvs1sNRJsezwdf’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs X11-xft-0.3.1-E2YofuHBPu4DXAPLYyOuZS extensible-exceptions-0.1.1.4-KI0dG6kQM84KnSzvR2Yb0 old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78 old-time-1.1.0.3-HsoRJMkCHriE79r63Cxfu4 random-1.1-3ypV4EIycgb35PKjTYYr5q utf8-string-1.0.1.1-Geq8jdOv4Q3LkcQoEOWDVv xmonad-0.15-KiSjBDh8avTDacDP4rBh9F
    Use -v to see a list of the files searched for.
  |
5 | import XMonad.Util.EZConfig(additionalKeys)
  | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please check the file for errors.

xmonad: xmessage: executeFile: does not exist (No such file or directory)
  errno: 1                                                                    
```

Try to reinstall the arch linux packages of the missing dependencies like.
```
sudo pacman -S haskell-extensible-exceptions haskell-setlocale haskell-utf8-string haskell-data-default
```

>Note: if the installation shows errors (like "xx failed to executed" in `sudo pacman -Syu`), try again and the error might disappear and works.

The dependencies missed reduced:
```
$ xmonad --recompile
XMonad will use ghc to recompile, because "/home/atupal/.xmonad/build" does not exist.
Error detected while loading xmonad configuration file: /home/atupal/.xmonad/xmonad.hs

xmonad.hs:1:1: error:
    Could not load module ‘XMonad’
    It is a member of the package ‘xmonad-0.15-KiSjBDh8avTDacDP4rBh9F’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs data-default-0.7.1.1-9TvgjOMl8fiEDpKR9EhMBO
    Use -v to see a list of the files searched for.
  |
1 | import XMonad
  | ^^^^^^^^^^^^^
```

But reinstalling `haskell-x11` doesn't help.

Use `ghc ~/.xmonad/xmonad.hs` it returns:

```
$ ghc -c xmonad.hs 

xmonad.hs:1:1: error:
    Could not find module ‘Prelude’
    There are files missing in the ‘base-4.12.0.0’ package,
    try running 'ghc-pkg check'.
    Use -v to see a list of the files searched for.
  |
1 | import XMonad
  | ^

xmonad.hs:1:1: error:
    Could not load module ‘XMonad’
    It is a member of the package ‘xmonad-0.15-KiSjBDh8avTDacDP4rBh9F’
    which is unusable due to missing dependencies:
      X11-1.9-1jVNltY9i4MFrKqIqKnIHs data-default-0.7.1.1-9TvgjOMl8fiEDpKR9EhMBO
    Use -v to see a list of the files searched for.
  |
1 | import XMonad
  | ^^^^^^^^^^^^^
  errno: 1                                        
```

So run `ghc-pkg check` as it suggested. Now we know what modules missed:
```
$ ghc-pkg check    
There are problems in package data-default-instances-old-locale-0.0.1:
  dependency "old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78" doesn't exist
There are problems in package data-default-instances-dlist-0.0.1:
  dependency "dlist-0.8.0.5-HU8Aimky3DbFEV0DkwGifS" doesn't exist
Warning: haddock-interfaces: /usr/share/doc/haskell-data-default-instances-base/html/data-default-instances-base.haddock doesn't exist or isn't a file
Warning: haddock-html: /usr/share/doc/haskell-data-default-instances-base/html doesn't exist or isn't a directory
There are problems in package xmonad-contrib-0.15:
  dependency "old-locale-1.0.0.7-D4Rn5zPhtMJBwwirPJNu78" doesn't exist
  dependency "old-time-1.1.0.3-HsoRJMkCHriE79r63Cxfu4" doesn't exist
  dependency "random-1.1-3ypV4EIycgb35PKjTYYr5q" doesn't exist
There are problems in package hackage-security-0.5.3.0:
  Warning: haddock-interfaces: /usr/share/doc/haskell-hackage-security/html/hackage-security.haddock doesn't exist or isn't a file
  Warning: haddock-html: /usr/share/doc/haskell-hackage-security/html doesn't exist or isn't a directory
```

Reinstall these modules and problem solved:
```
yaourt haskell old-locale # etc. if installation has errors, try again will fix it
...
xmonad --recompile
```
