Use https://github.com/atupal/snippet/blob/master/arch_and_linux/boot/install_from_existing.md
>Note: the destination partition need to be support Linux file system permissions. E.g. do not use NTFS or FAT32 on which the permissions will lose and fails the login with "wrong password".
>`su - username` will also fail since the permissions of the `shadow` file is all `777`.

Use [pacman-fix-permissions](https://github.com/droserasprout/pacman-fix-permissions) to fix the permissions for files of the pacman packages if the backup is alraedy messsed up.
Use `chmod` and `chown` to fix personal files and directories.
