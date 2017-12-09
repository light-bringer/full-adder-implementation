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
