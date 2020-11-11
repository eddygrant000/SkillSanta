#!/bin/python3
# Class
import threading
from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print(f"Hi from Hello {threading.currentThread().getName()}")
            sleep(1)

class Eddy(Thread):
    def run(self):
        for i in range(5):
            print(f"Hi from Eddy {threading.currentThread().getName()}")
            sleep(1)

ob1 = Hello()
ob2 = Eddy()

ob1.start()
ob2.start()

ob1.join()
ob2.join()

print("EOF By Skillsanta")
# ob1.run()
# ob2.run()