After installed Arch Linux (from existing backup system) to Surface Book 2. The usage of the one CPU core is very high, almost 100%!

- Use perf to check the function eats high CPU:
```shell
# perf top
-> acpi_ns_search_one_scope
```
- Use top to check the process number
Do not use htop which looks like is not accurate.
```shell
# top
-> PID: 482, kworker/0:3+kacpi_notify
-> Note: Before the kernel upgrade to 4.18.14, the top only shows the "kworker/0:3", now it shows also the module name?
```

Google "linux kworker high cpu", Ref: https://askubuntu.com/questions/33640/kworker-what-is-it-and-why-is-it-hogging-so-much-cpu

Try to run `echo l > /proc/sysrq-trigger` multiple times. And got following CPU trace:

```
[ 1675.097903] NMI backtrace for cpu 0
[ 1675.097904] CPU: 0 PID: 482 Comm: kworker/0:3 Tainted: G           OE     4.18.14-arch1-1-ARCH #1
[ 1675.097905] Hardware name: Microsoft Corporation Surface Book 2/Surface Book 2, BIOS 389.2318.768 08/14/2018
[ 1675.097905] Workqueue: kacpi_notify acpi_os_execute_deferred
[ 1675.097906] RIP: 0010:__schedule+0x1c6/0x8b0
[ 1675.097906] Code: 00 0f 84 9d 03 00 00 83 bb 98 09 00 00 01 0f 86 d9 05 00 00 48 8b 93 a0 09 00 00 48 85 db 74 18 48 8b 83 20 0b 00 00 48 01 d0 <49> 2b 85 e0 03 00 00 48 89 83 20 0b 00 00 49 8b 45 10 48 85 c0 75 
[ 1675.097937] RSP: 0018:ffff95ff840e3b58 EFLAGS: 00000002
[ 1675.097937] RAX: 000002ea7092c4b5 RBX: ffff9156ef421b00 RCX: 00000000044aa200
[ 1675.097938] RDX: 00000186039c0805 RSI: ffff9156ef400000 RDI: ffff9156ef421b00
[ 1675.097938] RBP: ffff95ff840e3bb0 R08: 00000000ffffffff R09: 0000000000000000
[ 1675.097939] R10: 0000000000000000 R11: 0000000000000000 R12: ffffffff9cc13740
[ 1675.097939] R13: ffff9156d9488000 R14: 0000000000000000 R15: ffffffff9caf4ee8
[ 1675.097940] FS:  0000000000000000(0000) GS:ffff9156ef400000(0000) knlGS:0000000000000000
[ 1675.097940] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 1675.097940] CR2: 00002cdd711c5000 CR3: 000000039ee0a003 CR4: 00000000003606f0https://bugs.launchpad.net/ubuntu/+source/linux/+bug/887793
[ 1675.097941] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[ 1675.097941] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 000000000https://01.org/linux-acpi/documentation/debug-how-isolate-linux-acpi-issues0000400
[ 1675.097942] Call Trace:
[ 1675.097942]  ? enqueue_entity+0x3d0/0xc20
[ 1675.097942]  schedule+0x32/0x90
[ 1675.097943]  schedule_timeout+0x311/0x4a0
[ 1675.097943]  ? native_sched_clock+0x5d/0x90
[ 1675.097943]  ? resched_curr+0x23/0xd0
[ 1675.097944]  __down_timeout+0x78/0xd0
[ 1675.097944]  ? preempt_count_add+0x68/0xa0
[ 1675.097944]  down_timeout+0x43/0x50
[ 1675.097945]  acpi_os_wait_semaphore+0x69/0x180
[ 1675.097945]  acpi_ut_acquire_mutex+0x12b/0x1c0
[ 1675.097946]  acpi_ex_enter_interpreter+0x4f/0x88
[ 1675.097946]  acpi_ds_terminate_control_method+0x82/0x1bf
[ 1675.097946]  acpi_ps_parse_aml+0x381/0x4af
[ 1675.097947]  acpi_ps_execute_method+0x1ef/0x2ab
[ 1675.097947]  acpi_ns_evaluate+0x2e4/0x42c
[ 1675.097947]  acpi_evaluate_object+0x1c7/0x3eb
[ 1675.097948]  acpi_evaluate_integer+0x5e/0x120
[ 1675.097948]  acpi_lid_update_state+0x37/0x90
[ 1675.097948]  ? acpi_button_notify+0x13d/0x170
[ 1675.097949]  acpi_ev_notify_dispatch+0x4a/0x5f
[ 1675.097949]  acpi_os_execute_deferred+0x16/0x20
[ 1675.097950]  process_one_work+0x1eb/0x3c0
[ 1675.097950]  worker_thread+0x2d/0x3d0
[ 1675.097950]  ? process_one_work+0x3c0/0x3c0
[ 1675.097951]  kthread+0x112/0x130
[ 1675.097951]  ? kthread_flush_work_fn+0x10/0x10
[ 1675.097951]  ret_from_fork+0x35/0x40

```
Note: the PID on the CPU call stuck is same with the PID from top.

SO this is definately the ACPI issue.

Also take a look on https://forums.fedoraforum.org/showthread.php?307996-kworker-is-eating-one-of-my-CPU-s-threads 
and https://askubuntu.com/questions/176565/why-does-kworker-cpu-usage-get-so-high,
https://bugs.launchpad.net/ubuntu/+source/linux/+bug/887793 but this askubuntu question doesn't help, it is not my root cause, i.e. Disable the gpeXX doesn't help

Google "kacpi_notify" and from:
https://bbs.archlinux.org/viewtopic.php?id=95972
https://wiki.archlinux.org/index.php/ACPI_modules

Try to add the `acpi=off` kenel parameter, reboot, and the CPU is dropped!.

But just like in 95972 arch bbs post says, it is not acceptable to disable the ACPI functionality. For example, I can only use one CPU core
after disabling the ACPI.

Also Googled "disable ACPI module"

and tried kernel parametes on https://01.org/linux-acpi/documentation/debug-how-isolate-linux-acpi-issues

only `acpi=off` works.

So Google "Linux Surface Book 2 ACPI", I got:

https://github.com/jakeday/linux-surface/issues/65
https://github.com/jakeday/linux-surface/issues/83

In issue `65`, the call stuck is same with me with `acpi_lid_update_state`.

Actually, if you go back to the Surface Book2 Arch Linux wiki page, it says almost everything works, but it actually need to install the 
`linux-surface4` package (deprecated and cannot used at least on 10/17/2018), which point to this github project.

See https://wiki.archlinux.org/index.php/Microsoft_Surface_Book_2

#### So the finaly solution is use this surface kernel: https://github.com/jakeday/linux-surface/
##### Compiling the Kernel from Source
1. Download the kernel sources file from https://kernel.org, download the patchs from https://github.com/jakeday/linux-surface/
2.
```shell
for i in ~/linux-surface/patches/[VERSION]/*.patch; do patch -p1 < $i; done
```
3. Get current config file and patch it, google 'arch linux kernel config file location', /boot/configxx doesn't exist for archlinux
```shell
zcat /proc/config.gz > ~/arch_linux_default_config_version
zcat /proc/config.gz > .config
# For non-ubuntu distro following patch will cause a lot of conflict, just patch it manually according the patch file diffs.
# Note: Please set a name for CONFIG_LOCALVERSION in the .config, it is used for the kernal name and kernel modules directory name.
# So give it a friendly name to avoid confusiing and maintaning and overwritting exising kernels.
# patch -p1 < ~/linux-surface/patches/config.patch
```
4. Compile and install the kernel: https://wiki.archlinux.org/index.php/Kernel/Traditional_compilation
```shell
make -j 8
sudo make modules_install # install the kernel modules to /lib/modules/<kernel name>
cp -v arch/x86_64/boot/bzImage /boot/vmlinuz-linux-surface-4.18
mkinitcpio -k <kernelversion> -g /boot/initramfs-<file name>.img # sudo mkinitcpio -k 4.18.14-surface -g /boot/initramfs-linux-surface-4.18.img
# -k (--kernel <kernelversion>): Specifies the modules to use when generating the initramfs image. The <kernelversion> name will be the same as the name of the custom kernel source directory (and the modules directory for it, located in /usr/lib/modules/).
# -g (--generate <filename>): Specifies the name of the initramfs file to generate in the /boot directory. Again, using the naming convention mentioned above is recommended.
```
5. Reinstall the DKMS modules for all the kernels: https://github.com/atupal/snippet/blob/master/arch_and_linux/kernel/systemd-modules-load.service-fails_on_custom_kernel.md
   For Arch Linux official `linux` kernel, all DKMS modules will be reinstalled when you install the kernel, but for you own kernel you
   need do it youself.
6. Add new boot-menu or `grub-mkconfig`.
7. Reboot, issue resolved.
