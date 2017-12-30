#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import os
import random

adbcommandTemplate = "/home/atupal/Software/Android/Sdk/platform-tools/adb shell input swipe %.1f %.1f %0.1f %0.1f %d"


def jump(stepLength):

    command = adbcommandTemplate % (300 + random.random() - 0.5,
            589 + random.random() - 0.5,
            300 + random.random() - 0.5,
            589 + random.random() - 0.5,
            #stepLength * 100 + random.random() - 0.5)
            stepLength * 100)

    if stepLength > 0:
        os.system(command)

    return stepLength
