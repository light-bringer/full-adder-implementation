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
      elif Input == "q" or Input == "Q" or Input =="Quit":
          quitcheck = "q"
          break
      else:
          print("invalid Input, please try again!")
          print("*********************************")




def calculator():
    print("This is an 8-Bit Adder used for summation purposes only.\nPlease don't use for substraction.\nDon't club with Signed and Unsigned Integers Pairs")
    signed = input("Type 'U' for Unsigned Operation, 'S' for Signed Operation : ")
    if signed == "U":
        signed = False
    elif signed == "S":
        signed = True

    first = input("Enter the first number")

if __name__ == '__main__':
    main()
