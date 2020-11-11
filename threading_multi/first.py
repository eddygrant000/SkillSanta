#!/bin/python3
from time import sleep
from threading import Thread
import threading
import os

def func1():
    for i in range(5):
        print(f"Hi from func1 ThreadName: {threading.currentThread().getName()} PID: {os.getpid()}")
        sleep(1)
        
def func2():
    for i in range(5):
        print(f"Hi from func2 ThreadName: {threading.currentThread().getName()} PID: {os.getpid()}")
        sleep(1)

t1 = Thread(target=func1, name="th1")
t2 = Thread(target=func2, name='th2')

t1.start()
t2.start()

t1.join()
t2.join()

print(f"EOF By Skillsanta TH Name: {threading.currentThread().getName()} PID: {os.getpid()}")