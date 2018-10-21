https://wiki.archlinux.org/index.php/Getty#Have_boot_messages_stay_on_tty1

```shell
sudo mkdir /etc/systemd/system/getty@tty1.service.d/
# Create /etc/systemd/system/getty@tty1.service.d/noclear.conf
# and add
[Service]
TTYVTDisallocate=no
```
