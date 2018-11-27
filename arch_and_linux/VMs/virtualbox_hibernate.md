```
$ cat /lib/systemd/system-sleep/sleep 
#!/bin/bash
case $1 in
  pre)
    # atupal start
    # The "running" VM will prevent hibernate(but not sleep)
    espeak "start hibernate"
    # No need, the vbox will do it automatically
    #VBoxManage controlvm "win10" pause || true
    #VBoxManage controlvm "win10" savestate
    # atupal end
    # unload the modules before going to sleep
    systemctl stop NetworkManager.service
    modprobe -r intel_ipts
    modprobe -r mei_me
    modprobe -r mei
    modprobe -r mwifiex_pcie;
    modprobe -r mwifiex;
    modprobe -r cfg80211;
    ;;
  post)
    # need to cycle the modules on a resume and after the reset is called, so unload...
    modprobe -r intel_ipts
    modprobe -r mei_me
    modprobe -r mei
    modprobe -r mwifiex_pcie;
    modprobe -r mwifiex;
    modprobe -r cfg80211;
    # and reload
    modprobe -i intel_ipts
    modprobe -i mei_me
    modprobe -i mei
    modprobe -i cfg80211;
    modprobe -i mwifiex;
    modprobe -i mwifiex_pcie;
    echo 1 > /sys/bus/pci/rescan
    systemctl restart NetworkManager.service
    # atupal start
    espeak "Welcome, $USERNAME"
    # Doesn't work, vbox will resume the VM after resume from hibernate automatically.
    # And resume manually with throw "VBoxManage: error: VM is paused due to host power management" error
    # So currently run the "reset_win10_network" manually after resuming from hibernate
    #VBoxManage controlvm "win10" resume
    # Reset the network of the VM otherwise the internet in guess OS will lose after resuming from sleep or hibernate
    # Need run as the user owns the VM, otherwise will get "VBoxManage: error: Could not find a registered machine named 'win10'" error since this script is run by root
    # Acually no need to wait for the network can access internet
    #sleep 7 # wait the host network connected
    espeak "Start resetting the VM network"
    sudo su - atupal --command='VBoxManage controlvm "win10" nic1 null'
    sudo su - atupal --command='VBoxManage controlvm "win10" nic1 bridged wlp1s0'
    # atupal end
    ;;
esac
```

See also https://github.com/atupal/snippet/blob/master/arch_and_linux/devices/surface_book_2.md
