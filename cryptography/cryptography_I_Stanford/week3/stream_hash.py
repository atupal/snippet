#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import hashlib

def sha256sum(buffer):
    return hashlib.sha256(buffer).digest()

def get_video_hash(filepath):

    buffer = ""

    with open(filepath) as fd:
        buffer = fd.read()

    chunk_size = 1024
    size = len(buffer)
    h = sha256sum(buffer[size-size%chunk_size:size])

    div_size = size - size % chunk_size
    for i in xrange(div_size / chunk_size):
        h = sha256sum(buffer[div_size-chunk_size*(i+1):div_size-chunk_size*i] + h)

    return h.encode("hex")

def solve():
    h_test = get_video_hash("/home/atupal/Downloads/6.2.birthday.mp4_download")
    if h_test != "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8":
        print("Wrong implementation!")
        return

    h = get_video_hash("/home/atupal/Downloads/6.1.intro.mp4_download")
    print(h)

if __name__ == "__main__":
    solve()
