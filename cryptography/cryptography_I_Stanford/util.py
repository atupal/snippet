import sys

try:
    xrange
except:
    xrange = range

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def hexxor(a, b):     # xor two hex sterings of different lengths
    if len(a) > len(b):
        a,b = b,a

    return [int(a[i*2:i*2+2], 16) ^ int(b[i*2:i*2+2], 16) for i in xrange(len(a)/2)]

def hexStringToBytesString(hexString):
    return "".join([chr(int(hexString[i*2:i*2+2], 16)) for i in xrange(len(hexString)/2)])

def random(size=16):
    return open("/dev/urandom").read(size)

def bytesStringToHexString(bytesString):
    return bytesString.encode('hex')

def encrypt(key, msg):
    c = strxor(key, msg)
    print()
    print(c.encode('hex'))
    return c

def decrypt(key, hexCipherText):
    cipherText = [int(hexCipherText[i*2:i*2+2], 16) for i in xrange(len(hexCipherText)/2)]
    msg = "".join([chr(key[i] ^ cipherText[i]) for i in xrange(len(cipherText))])
    print(msg)

def main():
    pass

if __name__ == '__main__':
    main()
