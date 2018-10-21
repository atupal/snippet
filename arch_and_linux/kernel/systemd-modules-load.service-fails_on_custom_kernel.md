1. Keep the boot message: https://github.com/atupal/snippet/blob/master/arch_and_linux/boot/keep_boot_message_on_tty1.md
2. Error and hint `systemctl status systemd-modules-load.service`
3. https://superuser.com/questions/997938/how-do-i-figure-out-why-systemctl-service-systemd-modules-load-fails
   https://wiki.archlinux.org/index.php/systemd#Investigating_systemd_errors
   ```
   systemctl --failed
   systemctl status systemd-modules-load.service
   # If the PID is not listed:
   # systemctl restart systemd-modules-load
   # systemctl status systemd-modules-load.service
   journalctl _PID=<pid>
   ls -Al /etc/modules-load.d/ # and fix incorrected configs if there are
   systemctl restart systemd-modules-load
   ```
4. My issue is
   ```
   $ systemctl status systemd-modules-load.service      
   ● systemd-modules-load.service - Load Kernel Modules
      Loaded: loaded (/usr/lib/systemd/system/systemd-modules-load.service; static; vendor preset: disabled)
      Active: failed (Result: exit-code) since Sun 2018-10-21 13:26:42 PDT; 28s ago
        Docs: man:systemd-modules-load.service(8)
              man:modules-load.d(5)
     Process: 554 ExecStart=/usr/lib/systemd/systemd-modules-load (code=exited, status=1/FAILURE)
    Main PID: 554 (code=exited, status=1/FAILURE)
   
   Oct 21 13:26:42 atupal systemd[1]: Starting Load Kernel Modules...
   Oct 21 13:26:42 atupal systemd-modules-load[554]: Failed to find module 'vboxdrv'
   Oct 21 13:26:42 atupal systemd-modules-load[554]: Failed to find module 'vboxpci'
   Oct 21 13:26:42 atupal systemd-modules-load[554]: Failed to find module 'vboxnetadp'
   Oct 21 13:26:42 atupal systemd-modules-load[554]: Failed to find module 'vboxnetflt'
   Oct 21 13:26:42 atupal systemd[1]: systemd-modules-load.service: Main process exited, code=exited, status=1/FAILURE
   Oct 21 13:26:42 atupal systemd[1]: systemd-modules-load.service: Failed with result 'exit-code'.
   Oct 21 13:26:42 atupal systemd[1]: Failed to start Load Kernel Modules.
     errno: 3                                                                                                                                                                                                
   # atupal at atupal in /home/atupal [13:27:48]
   ```
5.
   ```
   modprobe vboxdrv # Cannot find the mode
   pacman -Q | grep dkms # -> virtualbox-host-dkms
   dkms status # -> My current custom kernel(surface) doesn't install this module
   # reinstall 'virtualbox-host-dkms', which will install the DKMS modules for all kernels
   modprobe vboxdrv # Should show the kernel module.
   systemctl restart systemd-modules-load # the error should gone
   systemctl status systemd-modules-load # Shows the above modules are inserted
   ```

Successful output:

```
$ systemctl status systemd-modules-load
● systemd-modules-load.service - Load Kernel Modules
   Loaded: loaded (/usr/lib/systemd/system/systemd-modules-load.service; static; vendor preset: disabled)
   Active: active (exited) since Sun 2018-10-21 14:46:21 PDT; 32s ago
     Docs: man:systemd-modules-load.service(8)
           man:modules-load.d(5)
  Process: 18251 ExecStart=/usr/lib/systemd/systemd-modules-load (code=exited, status=0/SUCCESS)
 Main PID: 18251 (code=exited, status=0/SUCCESS)

Oct 21 14:46:21 atupal systemd[1]: Starting Load Kernel Modules...
Oct 21 14:46:21 atupal systemd-modules-load[18251]: Inserted module 'vboxdrv'
Oct 21 14:46:21 atupal systemd-modules-load[18251]: Inserted module 'vboxpci'
Oct 21 14:46:21 atupal systemd-modules-load[18251]: Inserted module 'vboxnetadp'
Oct 21 14:46:21 atupal systemd-modules-load[18251]: Inserted module 'vboxnetflt'
Oct 21 14:46:21 atupal systemd[1]: Started Load Kernel Modules.
# atupal at atupal in /home/atupal [14:46:53]
```

```
/etc/modules-load.d/*.conf, /run/modules-load.d/*.conf, /usr/lib/modules-load.d/*.conf # https://www.freedesktop.org/software/systemd/man/modules-load.d.html (Google "etc/modules-load.d")
$ pacman -Qo /lib/modules-load.d/virtualbox-host-dkms.conf
/usr/lib/modules-load.d/virtualbox-host-dkms.conf is owned by virtualbox-host-dkms 5.2.20-1
```
