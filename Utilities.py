#!/usr/bin/env python

# Utility functions


def to_bits(a):
    return (bool(int(x, 2)) \
            for x in reversed(str(bin(a))[2:]))


def from_bits(a):
    return int(''.join((str(int(x)) \
                        for x in reversed(a))), 2)

def setbit(x, bit):
    return x[bit] == '1'

def zip_bits(x, y, val):
    return map((lambda *z: [(val if d is None else d) \
                            for d in z]), x, y)

def nand(x, y):
    return (not (x and y))

def to8bits(num):
    return '{0:08b}'.format(num)

def tobase10(num):
    return int(num, 2)



def add(x, y):
    z = zip_bits(to_bits(x), to_bits(y), False)
    sb = ripple_adder(z)
    si = from_bits(sb)
    return si


def ripple_adder(z):
    c = False
    o = []
    for xb, yb in z:
        s, c = full_adder(xb, yb, c)
        o.append(s)
    if c:
        o.append(c)
    return o


def full_adder(a, b, ci):
    s1 = nand(a, b)
    s2 = nand(s1, a)
    s3 = nand(s1, b)
    s4 = nand(s2, s3)
    s5 = nand(s4, ci)
    s6 = nand(s4, s5)
    s7 = nand(s5, ci)
    s = nand(s6, s7)
    co = nand(s1, s5)
    return s, co
