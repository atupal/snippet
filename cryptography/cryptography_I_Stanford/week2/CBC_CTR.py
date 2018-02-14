#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

from Crypto.Cipher import AES
from Crypto.Util import Counter

def AES__CBC_encrpt(key, iv, message):
    #cipher_text = AES.new('this is a key123', AES.MODE_CBC, 'This is an IV456').encrypt("1234567890123456")
    cipher_text = AES.new(key, AES.MODE_CBC, iv).encrypt(message)

    return cipher_text

def AES_CBC_decrypt(key, iv, cipher_text):
    plain_text = AES.new(key, AES.MODE_CBC, iv).decrypt(cipher_text)

    # Trim the padding at end
    return plain_text[:-ord(plain_text[-1])]

def AES_CTR_decrypt(key, iv, cipher_text):
    plain_text = AES.new(key, AES.MODE_CTR, counter=Counter.new(128, initial_value=int(iv, 16))).decrypt(cipher_text)

    return plain_text

def solve_cbc(key_hex, cipher_text_hex):
    key = "".join([chr(int(key_hex[2*i:2*i+2], 16)) for i in xrange(len(key_hex)/2)])
    cipher_text = "".join([chr(int(cipher_text_hex[2*i:2*i+2], 16)) for i in xrange(len(cipher_text_hex)/2)])
    print(AES_CBC_decrypt(key, cipher_text[:16], cipher_text[16:]))

def solve_ctr(key_hex, cipher_text_hex):
    key = "".join([chr(int(key_hex[2*i:2*i+2], 16)) for i in xrange(len(key_hex)/2)])
    cipher_text = "".join([chr(int(cipher_text_hex[2*i:2*i+2], 16)) for i in xrange(len(cipher_text_hex)/2)])
    print(AES_CTR_decrypt(key, cipher_text_hex[:32], cipher_text[16:]))

def solve():
    key_hex = "140b41b22a29beb4061bda66b6747e14"
    cipher_text_hex = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
    solve_cbc(key_hex, cipher_text_hex)

    key_hex = "140b41b22a29beb4061bda66b6747e14"
    cipher_text_hex = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
    solve_cbc(key_hex, cipher_text_hex)

    key_hex = "36f18357be4dbd77f050515c73fcf9f2"
    cipher_text_hex = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
    solve_ctr(key_hex, cipher_text_hex)

    key_hex = "36f18357be4dbd77f050515c73fcf9f2"
    cipher_text_hex = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
    solve_ctr(key_hex, cipher_text_hex)

    # Answer:
    """
Basic CBC mode encryption needs padding.
Our implementation uses rand. IV
CTR mode lets you build a stream cipher from a block cipher.
Always avoid the two time pad!
    """

if __name__ == "__main__":
    solve()
