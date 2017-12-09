#!/usr/bin/env python3

from Utilities import *
from Adder import *

def main():
  name = input("Hi, please enter your name : ")
  quitcheck = ""
  while quitcheck is not "q":
      print("Hi %s, please Enter a/A to use the adder, enter 'Q' or 'q' to quit" % (name))
      Input = input()
      if Input == "A" or Input == "a":
          print("run_code()")
          calculator()
      elif Input == "q" or Input == "Q" or Input =="Quit":
          quitcheck = "q"
          break
      else:
          print("invalid Input, please try again!")
          print("*********************************")




def calculator():
    print("This is an 8-Bit Adder used for summation purposes only.\nPlease don't use for substraction.\nDon't club with Signed and Unsigned Integers Pairs")
    # signed = input("Type 'U' for Unsigned Operation, 'S' for Signed Operation : ")
    print("Please enter unsigned numbers only -- Range (0, 255)")

    first = int(input("Enter the first number :"))
    second = int(input("Enter the second number : "))
    print(first, type(first))
    if first not in range(0, 256):
        print("Number is Outside Range")
        return
    firstbin = to8bits(first)
    secondbin = to8bits(second)
    print(firstbin, secondbin)
    if len(firstbin) != 8 or len(secondbin)!=8:
        print("Memory Overflow, the integer is not an 8-bit number")
        return
    print("First Number : %d \nBInary Equivalent: %s"% (first, firstbin))
    print("Second Number : %d \nBInary Equivalent: %s"% (second, secondbin))

    binarysum = EightBitAdder(firstbin, secondbin)
    sum = tobase10(binarysum)
    print("Sum : ", tobase10(sum))
    print ("Sum in Binaries : ", binarysum)


if __name__ == '__main__':
    main()
