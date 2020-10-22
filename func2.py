#!/bin/python3

database = {
    101: {
        'name': 'sachin',
        'pin': 1234
    },
    102: {
        'name': 'Prajjwal',
        'pin': 2222
    }
}

def login(username, password):
    if username in database.keys() and password == database[username]['pin']:
        return True
    else:
        return False

user = int(input("Enter username: "))
passwd = int(input("Enter Pin: "))
print(login(user, passwd))


login(username, password)