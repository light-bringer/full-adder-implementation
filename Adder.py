#!/usr/bin/env python3

from Utilities import *


class Connector:
    def __init__ (self, owner, name, activates=0, monitor=False):
        self.value = None
        self.owner = owner
        self.name = name
        self.monitor = monitor
        self.connects = []
        self.activates= activates

    def connect(self, inputs) :
        if type(inputs) != type([]):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value) :
        if self.value == value:
            return                    # Ignore if no change
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor:
            print("Connector %s-%s set to %d" % (self.owner.name, self.name,self.value))
        for con in self.connects:
                con.set(value)

    def show(self):
        print(self.value)
        print(self.owner)
        print(self.name)
        print(self.monitor)
        print(self.connects)
        print(self.activates)



class LC:
    '''
    # Logic Circuits have names and an evaluation function defined in child
    # classes. They will also contain a set of inputs and outputs.
    '''
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return


class Not(LC):
    '''
    Inverter.
    Input A.
    Output B.
    '''
    def __init__(self, name):
        LC.__init__ (self, name)
        self.A = Connector(self, 'A', activates=1)
        self.B = Connector(self, 'B')

    def evaluate (self):
        self.B.set(not self.A.value)



class Gate2(LC):

    '''
    two input gate template.
    Inputs A, B.
    Output C
    '''
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self,'A',activates=1)
        self.B = Connector(self,'B',activates=1)
        self.C = Connector(self,'C')


class And(Gate2):         # two input AND Gate
    '''
    LC.
    Inputs A, B.
    Output C
    # two input AND gate.
    '''
    def __init__ (self, name):
        Gate2.__init__ (self, name)

    def evaluate (self):
        self.C.set(self.A.value and self.B.value)


class Or(Gate2):
    '''
    LC.
    Inputs A, B.
    Output C
    # two input OR gate.
    '''
    def __init__(self, name):
        Gate2.__init__(self, name)

    def evaluate(self):
        self.C.set(self.A.value or self.B.value)



class Xor(Gate2):
    '''
    Composite LC.
    Inputs A, B.
    Output C
    C = A'B + AB'
    # two input XOR gate.
    '''
    def __init__(self, name):
        Gate2.__init__(self, name)
        self.AND1 = And("AND1")
        self.AND2 = And("AND2")
        self.I1 = Not("I1")
        self.I2 = Not("I2")
        self.OR = Or("OR")
        self.A.connect([self.AND1.A, self.I2.A])
        self.B.connect([self.I1.A, self.AND2.A])
        self.I1.B.connect([self.AND1.B ])
        self.I2.B.connect([self.AND2.B ])
        self.AND1.C.connect([self.OR.A ])
        self.AND2.C.connect([self.OR.B ])
        self.OR.C.connect([self.C ])



class Nand(Gate2):
    '''
    Composite LC.
    Inputs A, B.
    Output C
    C = (AB)'
    # two input NAND gate.
    '''
    def __init__ (self, name):
        Gate2.__init__ (self, name)

    def evaluate (self):
        self.C.set(not(self.A.value and self.B.value))




class HalfAdder(LC):
    '''
    # One bit adder
    input : A,B
    output : Sum, Carry
    '''
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', 1)
        self.B = Connector(self, 'B', 1)
        self.S = Connector(self, 'S')
        self.C = Connector(self,'C')
        self.XOR= Xor("XOR")
        self.AND= And("AND")
        self.A.connect([self.XOR.A, self.AND.A])
        self.B.connect([self.XOR.B, self.AND.B])
        self.XOR.C.connect([self.S])
        self.AND.C.connect([self.C])


class FullAdderHA(LC):
    '''
    # One bit Adder, by two Half Adders
    input : A, B, Cin`
    output : Sum, Cout
    '''
    # One bit adder, A,B,Cin in. Sum and Cout out
    def __init__(self, name, mon=0):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', 1, monitor=mon)
        self.B = Connector(self, 'B', 1, monitor=mon)
        self.Cin = Connector(self, 'Cin', 1, monitor=mon)
        self.S = Connector(self, 'S', monitor=mon)
        self.Cout = Connector(self, 'Cout', monitor=mon)
        self.HA1 = HalfAdder("HA1")
        self.HA2 = HalfAdder("HA2")
        self.OR = Or("OR")
        self.A.connect([self.HA1.A ])
        self.B.connect([self.HA1.B ])
        self.Cin.connect([self.HA2.A ])
        self.HA1.S.connect([self.HA2.B ])
        self.HA1.C.connect([self.OR1.B])
        self.HA2.C.connect([self.OR1.A])
        self.HA2.S.connect([self.S])
        self.OR.C.connect([self.Cout])



class FullAdder(LC):         # One bit adder, A,B,Cin in. Sum and Cout out
    def __init__(self, name, mon=0):
        # Defining the GATES here
        LC.__init__(self, name)
        self.A = Connector(self, 'A', 1, monitor=mon)
        self.B = Connector(self, 'B', 1, monitor=mon)
        self.Cin = Connector(self, 'Cin', 1, monitor=mon)
        self.S = Connector(self, 'S', monitor=mon)
        self.Cout = Connector(self, 'Cout', monitor=mon)
        self.XOR1 = Xor("XOR1")
        self.XOR2 = Xor("XOR2")
        self.OR = Or("OR")
        self.AND1 = And("AND1")
        self.AND2 = And("AND2")
        # Starting with the connections
        self.A.connect([self.XOR1.A])
        self.B.connect([self.XOR1.B])
        self.A.connect([self.AND2.A])
        self.B.connect([self.AND2.B])

        self.XOR1.C.connect([self.XOR2.A])
        self.Cin.connect([self.XOR2.B])

        self.XOR1.C.connect([self.AND1.A])
        self.Cin.connect([self.AND1.B])

        self.AND1.C.connect([self.OR.A])
        self.AND2.C.connect([self.OR.B])

        self.XOR2.C.connect([self.S])
        self.OR.C.connect([self.Cout])



def FourBitAdder(a, b):      # a, b four char strings like '0110'
    F0 = FullAdder("F0")
    F1 = FullAdder("F1")
    F0.Cout.connect(F1.Cin)
    F2 = FullAdder("F2")
    F1.Cout.connect(F2.Cin)
    F3 = FullAdder("F3")
    F2.Cout.connect(F3.Cin)

    F0.Cin.set(0)
    F0.A.set(setbit(a, 3))
    F0.B.set(setbit(b, 3))  # bits in lists are reversed from natural order
    F1.A.set(setbit(a, 2))
    F1.B.set(setbit(b, 2))
    F2.A.set(setbit(a, 1))
    F2.B.set(setbit(b, 1))
    F3.A.set(setbit(a, 0))
    F3.B.set(setbit(b, 0))

    print(F3.Cout.value, end='')
    print(F3.S.value, end='')
    print(F2.S.value, end='')
    print(F1.S.value, end='')
    print(F0.S.value, end='')

    sum = "{0}{1}{2}{3}{4}".format(int(F3.Cout.value), int(F3.S.value),
                                                int(F2.S.value), int(F1.S.value), int(F0.S.value))

    return sum





def EightBitAdder(a, b):    # a, b four char strings like '0110'
    F0 = FullAdder("F0")
    F1 = FullAdder("F1")
    F0.Cout.connect(F1.Cin)
    F2 = FullAdder("F2")
    F1.Cout.connect(F2.Cin)
    F3 = FullAdder("F3")
    F2.Cout.connect(F3.Cin)
    F4 = FullAdder("F4")
    F3.Cout.connect(F4.Cin)
    F5 = FullAdder("F5")
    F4.Cout.connect(F5.Cin)
    F6 = FullAdder("F6")
    F5.Cout.connect(F6.Cin)
    F7 = FullAdder("F7")
    F6.Cout.connect(F7.Cin)

    F0.Cin.set(0)
    # bits in lists are reversed for Natural Order
    F0.A.set(setbit(a, 7))
    F0.B.set(setbit(b, 7))
    F1.A.set(setbit(a, 6))
    F1.B.set(setbit(b, 6))
    F2.A.set(setbit(a, 5))
    F2.B.set(setbit(b, 5))
    F3.A.set(setbit(a, 4))
    F3.B.set(setbit(b, 4))
    F4.A.set(setbit(a, 3))
    F4.B.set(setbit(b, 3))
    F5.A.set(setbit(a, 2))
    F5.B.set(setbit(b, 2))
    F6.A.set(setbit(a, 1))
    F6.B.set(setbit(b, 1))
    F7.A.set(setbit(a, 0))
    F7.B.set(setbit(b, 0))

    sum = "{0}{1}{2}{3}{4}{5}{6}{7}{8}".format(int(F7.Cout.value), int(F7.S.value),
                                                int(F6.S.value), int(F5.S.value),
                                                int(F4.S.value), int(F3.S.value),
                                                int(F2.S.value), int(F1.S.value), int(F0.S.value))

    return sum


print(EightBitAdder("11110000", "00001111"))
