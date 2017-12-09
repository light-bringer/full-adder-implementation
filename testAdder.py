#!/usr/bin/env python


from Adder import *
import random

def randomtest():
    testcount = 0
    failed = 0
    for x in range(100):
        num1 = random.randint(0,256)
        num2 = random.randint(0,256)
        sum = num1 + num2
        binarysum = EightBitAdder(to8bits(num1), to8bits(num2))

        if sum ==  tobase10(binarysum):
            testcount = testcount + 1
        else:
            failed = failed + 1

    print("passed : ", testcount)
    print("failed : ", failed)


randomtest()
