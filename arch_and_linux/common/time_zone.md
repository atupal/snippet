Ref: https://wiki.archlinux.org/index.php/time

Set the hardware clock time standard to localtime if dual boot with windows, since windows
use localtime for Real Time Clock (RTC) or CMOS clock by default.

```
timedatectl set-local-rtc 1
tzselect # Select the local time zone for software time.
# if the time is incorrect, boot into windows and let windows correct the hardware time.
```
FAQ:
### The UTC time is wrong after daylight saving is changed. But the time zone info is right, and the time shift number is also right.
Make sure you performed an clean reboot but not resume from existing hibernate state, which may doens't refresh some stats which is set before the daylight saving changed
