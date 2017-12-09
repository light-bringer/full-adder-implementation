#!/usr/bin/env python


from Adder import *
import random

def randomgen():
    for x in range(10):
        num1 = random.randint(1,255)
        num2 = random.randint(1,255)
        print ("Sum : ", num1 + num2)


randomgen()
