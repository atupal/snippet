#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import sys
sys.path.insert(0, "..")
sys.path.insert(0, ".")

import util

def sqrt_ceil(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid * mid < n:
            low = mid + 1
        elif mid * mid > n:
            high = mid - 1
        else:
            return mid

    if high * high >= n:
        return high
    return high + 1

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

def ext_euclid(a, b):
    if (b == 0):
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b , a % b ) # q = GCD(a, b) = GCD(b, a%b)
        x, y = y, ( x - (a // b) * y )
        return x, y, q

def solve1():
    N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581

    A = sqrt_ceil(N)

    if not (A * A > N and N > (A-1) * (A-1)):
        print("Wrong A!")
        return

    x = sqrt_ceil(A * A - N)

    if (A-x) * (A+x) == N:
        print("p:", A-x)
        print("q:", A+x)

def solve2():
    N = 648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877

    N_sqrt = sqrt_ceil(N)
    for i in range(2**20):
        A = N_sqrt + i
        x = sqrt_ceil(A*A - N)
        if (A-x) * (A+x) == N:
            print("p:", A-x)
            print("q:", A+x)
            break

def solve3():
    N = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929

    # Noticed that (3p + 2q) / 2 = A is not a interger.
    # So we use (6p + 4q) / 2 = 2A
    # And we know A - (6N)^0.5 < 1/(8*6^0.5)
    #             2A - 2*(6N)^0.5 < 1/(4*6^0.5)
    # (2A + x) * (2A - x) = 6p * 4q = 24N
    _2A = sqrt_ceil(24*N)

    if not (_2A * _2A >= 24*N and 24*N > (_2A-1) * (_2A-1)):
        print("Wrong A!")
        return

    x = sqrt_ceil(_2A*_2A - 24*N)

    if x*x != _2A*_2A - 24*N:
        print("Wrong x!")
        return

    p = (_2A - x) // 6
    q = (_2A + x) // 4

    if p*q == N:
        print("p:", p)
        print("q:", q)
    else:
        p = (_2A + x) // 6
        q = (_2A - x) // 4

def solve4():
    # p, q is output from solve1()
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073662768891111614362326998675040546094339320838419523375986027530441562135724301
    q = 13407807929942597099574024998205846127479365820592393377723561443721764030073778560980348930557750569660049234002192590823085163940025485114449475265364281

    N = p * q

    phi = (p-1) * (q-1)

    e = 65537

    _, d, _ = ext_euclid(phi, e)
    while d < 0:
        d += phi

    if e*d % phi != 1:
        print("Wrong d!")

    cipher_text_number = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540

    plain_text = fast_exp(cipher_text_number, d, N)

    plain_text_hex_string = ('%0256x' % plain_text)
    plain_text_hex_string = plain_text_hex_string.split('00')[1]
    print(util.hexStringToBytesString(plain_text_hex_string))

if __name__ == "__main__":
    solve1()
    solve2()
    solve3()
    # Need to run Python2
    #solve4(), the answer is 'Factoring lets us break RSA.'
