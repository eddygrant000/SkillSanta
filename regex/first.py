#!/bin/python3

# re : module 

import re


user_input = input("enter anything: ")
# user_input = "xyz"

# data = re.match("sac", user_input)

data = re.search("sac..", user_input)
print(data)