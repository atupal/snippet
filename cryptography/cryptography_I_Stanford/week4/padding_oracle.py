#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import requests

def validate_plaintext_padding(cipher_text_hex):
    url = "http://crypto-class.appspot.com/po?er=" + cipher_text_hex

    res = requests.get(url)

    if res.status_code == 403:
        return False
    elif res.status_code == 404 or res.status_code == 200:
        print("Status code: " + str(res.status_code))
        return True
    else:
        # If not a valid hex string, the server will return 500 server internal error
        raise Exception("Bad cipher text, not hex string! Status code: " + str(res.status_code))

def solve():
    cipher_text_hex = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
    size = len(cipher_text_hex) / 2
    block_size = 128 / 8
    block_cnt = size / block_size

    plain_text = [0xff for i in xrange(size)]
    cipher_text = [int(cipher_text_hex[2*i:2*i+2], 16) for i in xrange(size)]

    for block_ind in xrange(block_cnt, 1, -1):

        byte_ind = 1 # from right to left
        start = 0
        while byte_ind <= block_size:

            cipher_text_modified = [cipher_text[i] for i in xrange(block_ind * block_size)]
            for i in xrange(1, byte_ind):
                # Note: Please see the next comment
                cipher_text_modified[(block_ind-1) * block_size - i] =\
                         cipher_text[(block_ind-1) * block_size - i] ^ plain_text[block_ind * block_size - i] ^ byte_ind

            found = False
            for g in xrange(start, 256):
                # Note: The modified result is not g ^ byte_ind but is cipher_text_previous_block ^ g ^ byte_ind.
                #       Actually you can still continue the process, but the found
                #       "plain_text" is actually cipher_text_previous_block ^ plain_text.
                cipher_text_modified[(block_ind-1) * block_size - byte_ind] =\
                         cipher_text[(block_ind-1) * block_size - byte_ind] ^ g ^ byte_ind
                print("Guessing [%s, %s] to %x" % (block_ind, byte_ind, g))
                if (validate_plaintext_padding("".join(map(lambda x: "%02x" % x, cipher_text_modified)))):
                    plain_text[block_ind * block_size - byte_ind] = g
                    print("[%s, %s] is %x" % (block_ind, byte_ind, g))
                    found = True
                    break

            if not found:
                # The previous guess must be wrong, then cannot find correct guess in current iteration
                # BTW, this can only happend when guessing the last byte of the block since there is only
                #      one byte to guess (using 01 as the padding). And the (01 ^ g ^ last_byte) with the
                #      precedding bytes, it happends to be a valid pad.
                #      g = 0x01 in this example, in the 4th block, the right value is 0x9. And the late bytes are
                #      ... 101, 9, 9, 9, 9, 9, 9, 9, 9, 9. And 1 ^ 1 ^ 9 == 9
                byte_ind -= 1
                start = plain_text[block_ind * block_size - byte_ind] + 1
            else:
                byte_ind += 1
                start = 0

    print(plain_text)
    print("".join(map(lambda x: chr(x), plain_text[block_size:len(plain_text)])))

    # The answer is
    """
    # The cipher_text_previous_block ^ plain_text: [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 166, 99, 190, 134, 178, 72, 137, 190, 211, 102, 134, 176, 237, 211, 115, 32, 57, 195, 154, 148, 114, 123, 45, 106, 21, 230, 35, 180, 124, 224, 78, 206, 57, 8, 98, 54, 71, 156, 52, 84, 164, 54, 40, 248, 131, 172, 126, 201]

    The plain text:
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 84, 104, 101, 32, 77, 97, 103, 105, 99, 32, 87, 111, 114, 100, 115, 32, 97, 114, 101, 32, 83, 113, 117, 101, 97, 109, 105, 115, 104, 32, 79, 115, 115, 105, 102, 114, 97, 103, 101, 9, 9, 9, 9, 9, 9, 9, 9, 9]

    'The Magic Words are Squeamish Ossifrage'
    """

if __name__ == "__main__":
    solve()
