#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import os
import random

adb_executable_path = "/home/atupal/Software/Android/Sdk/platform-tools/adb"
adb_swipe_command_template = "%s shell input swipe %.1f %.1f %0.1f %0.1f %d"

def jump(step_length):

    command = adb_swipe_command_template % (adb_executable_path,
            300 + random.random() - 0.5,
            589 + random.random() - 0.5,
            300 + random.random() - 0.5,
            589 + random.random() - 0.5,
            #step_length * 100 + random.random() - 0.5)
            step_length * 100)

    if step_length > 0:
        os.system(command)

    return step_length

def restart_game():
    command = adb_swipe_command_template % (adb_executable_path,
            245 + random.random() - 0.5,
            705 + random.random() - 0.5,
            245 + random.random() - 0.5,
            705 + random.random() - 0.5,
            random.random() * 100)

    os.system(command)

def screen_capture(filename):
    os.system("cp %s previous_screen.png" % filename)
    os.system("{0} shell screencap -p /sdcard/{1} && {0} pull /sdcard/{1} && {0} shell rm /sdcard/{1}".format(adb_executable_path, filename))
