#!/bin/python3

import multiprocessing
import os
import threading
from time import sleep

def func1():
    for i in range(5):
        print(f'HI from func1 THName: {threading.currentThread().getName()} PID: {os.getpid()}')
        sleep(1)

def func2(name):
    for i in range(5):
        print(f'HI from {name} func2 THName: {threading.currentThread().getName()} PID: {os.getpid()}')
        sleep(1)

m1 = multiprocessing.Process(target=func1)
m2 = multiprocessing.Process(target=func2, args=['Sachin'])

m1.start()
m2.start()
# func1()
# func2()
print(f'HI from Main body THName: {threading.currentThread().getName()} PID: {os.getpid()}')
