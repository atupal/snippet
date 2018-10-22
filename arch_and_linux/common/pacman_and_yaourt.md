##### file owned by two projectes
error: file owned by 'visual-studio-code' and 'visual-studio-code-bin': 'opt/visual-studio-code/content_shell.pak'
error: file owned by 'visual-studio-code' and 'visual-studio-code-bin': 'opt/visual-studio-code/icudtl.dat'

https://unix.stackexchange.com/questions/267928/pacman-a-file-owned-by-two-packages

Just uninstall and re-install

##### error: duplicated database entry 'xxx package'
G "pacman duplicated database entry"
https://bbs.archlinux.org/viewtopic.php?id=107621

Script to remove all duplciated packags (run multiple times if doesn't clear entirely):
```python
#!/usr/bin/env python

import os,re, datetime
d = '/var/lib/pacman/local'

packages = os.listdir(d)
packages.sort()

pkgname_search = re.compile('^(.*?)-[0-9]')

old_packages = []

for pkg1 in packages:
    if pkg1 in old_packages:
        continue

    #get package name
    pkgnames = pkgname_search.findall(pkg1)
    if len(pkgnames) > 0:
        pkgname = pkgname_search.findall(pkg1)[0]
    else:
        continue

    #look for other items with the same package name
    for pkg2 in packages:
        if pkg2 == pkg1:
            continue
        if pkg2 in old_packages:
            continue
        if len(pkgname_search.findall(pkg2)) > 0 and pkgname == pkgname_search.findall(pkg2)[0]:
            # We now have two duplicate packages, we want to delete the old one

            old_package = pkg1
            path1 = os.path.join(d,pkg1)
            path2 = os.path.join(d,pkg2)
            if os.stat(path1).st_mtime > os.stat(path2).st_mtime:
                old_package = pkg2

            old_packages.append(old_package)
            #print ('duplicate found:\t')
            #print (pkg1)
            #print (pkg2)
            #print ('old:', old_package)

            oldpath = os.path.join(d,old_package)
            target = os.path.join('/var/lib/pacman/OLD',old_package)
            cmd = 'mv "%s" "%s"' % (oldpath, target)

            #double-check that the oldpath still exists (it may have been removed in a previous pass)
            if os.path.exists(oldpath):
                print(cmd)
                os.system(cmd)

```
