
After downloading Android Studio from http://developer.android.com/sdk/index.html and run it. 
The wizard give the error: "Unable to run mksdcard SDK tool"

So what is "mksdcard" ?

mksdcard
From the Android Developer Site:
> The mksdcard tool lets you quickly create a FAT32 disk image that you can load in the emulator, to simulate the presence of an SD card in the device. Because you can specify an SD card while creating an AVD in the AVD Manager, you usually use that feature to create an SD card. This tool creates an SD card that is not bundled with an AVD, so it is useful for situations where you need to share a virtual SD card between multiple emulators.

This post https://bbs.archlinux.org/viewtopic.php?id=199270 said that isntall lib32-mesa solved the problem. And in AUR, 
lib32-mesa is a dependency of Android Studio. After you install lib32-mesa, a lot of depency 32-bit lib have been installed.
And another post http://stackoverflow.com/questions/29241640/errorunable-to-run-mksdcard-sdk-tool-in-ubuntu said install some 
32-bit libs solve the problem. So it maybe just because when you instal lib32-mesa in ArchLinux, Another basic lib32 tools have 
been installed. So the mssdcard SDK tool in Android Studio Installed successful.
