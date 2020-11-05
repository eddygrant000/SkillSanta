#!/bin/python3

import re

# @ should be contain in email
# only accept _ 123 asdf .  
# atlease username >= 5
# domain , gmail, yahoo, skillsanta, ap2v
# .com , .in, .co.in, .org

user_input = ''
while user_input != 'exit':
    user_input = input("Enter email: ")
    # data = re.search("[a-z].....@gmail.com", user_input)
    # data = re.search("[a-z]+@gmail.com", user_input)
    # data = re.search("[a-z0-9.]+@gmail.com", user_input)
    # data = re.search("^[a-z0-9.]+@gmail.com", user_input)
    # data = re.search("^[a-z0-9.]+@gmail.com$", user_input)
    # data = re.search("^[a-z0-9_.]+@gmail.com$", user_input)
    # data = re.search("^[a-z0-9_.]+@gmail\.com$", user_input)
    # data = re.search("^[a-z0-9_.]{5,25}@gmail\.com$", user_input)
    # data = re.search("^[a-z0-9_.]{5,25}@(gmail|skillsanta|yahoo)\.com$", user_input)
    data = re.search("^[a-z0-9_.]{5,25}@(gmail|skillsanta|yahoo)(\.[a-z]{2,3})?\.[a-z]{2,3}$", user_input)
    if data != None:
        print('Valid Email:', data)
