#!/bin/python3

class A:
    def __init__(self):
        print("Hi from A init")
    def m1(self):
        print("Hi from m1 from A")

class B:
    def __init__(self):
        print("Hi from B init")
    def m2(self):
        print("Hi from m2 from B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Hi from C init")
    def m3(self):
        print("Hi from m3 from C")

# a1 = A()
# b1 = B()
# c1 = C()

# print(help(c1))
# b1.m2()
# b1.m1()

# c1.m1()
# c1.m2()
# c1.m3()

#################33

def fun1(a,b):
    return a+b

def fun1(a, b, c):
    return a + b +c

print(fun1(10, 20))