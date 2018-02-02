#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''


def fast_exp(base, e, mod):

    if e < 0:

        raise Exception("AgurmentOutOfRange")

    binary_exp = base
    ret = 1

    while e:
        if e & 1:
            ret = ret * binary_exp % mod
        binary_exp = binary_exp * binary_exp % mod
        e >>= 1

    return ret

def solve(p, g, h):

    B = 2**20
    preprocess_table = {}

    for i in range(B+1):
        g_i = fast_exp(g, i, p)
        g_i_1 = fast_exp(g_i, p-2, p)
        preprocess_table[h * g_i_1 % p] = i

    for i in range(B+1):
        g_b_i = fast_exp(g, B*i, p)

        if g_b_i in preprocess_table:

            print("Answer found, x0, x1: ", i, preprocess_table[g_b_i])
            # Answer found, x0, x1:  357984 787046

            return (i * B + preprocess_table[g_b_i]) % p
            # 375374217830

    return None

if __name__ == "__main__":
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
    print (solve(p, g, h))
