Set the hardware clock time standard to localtime if dual boot with windows, since windows
use localtime for Real Time Clock (RTC) or CMOS clock by default.

```
timedatectl set-local-rtc 1
tzselect # Select the local time zone for software time.
# if the time is incorrect, boot into windows and let windows correct the hardware time.
```
