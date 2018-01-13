#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import sys
sys.path.insert(0, "..")

import util

def main():
    message = 'Pay Bob 100$'
    indexOfMessageToModify = message.find("1")
    IV = "20814804c1767293b99f1d9cab3bc3e7"
    newXorHex = util.bytesStringToHexString(util.strxor(util.strxor("5", "1"), util.hexStringToBytesString(IV[indexOfMessageToModify*2:indexOfMessageToModify*2+2])))
    print(newXorHex)
    print(IV[:indexOfMessageToModify*2] + newXorHex + IV[indexOfMessageToModify*2+2:])

if __name__ == "__main__":
    main()
