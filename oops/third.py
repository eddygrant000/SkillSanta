#!/bin/python3


class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    # def __init__(self, name):
    #     self.name = name

    def view(self):
        print(f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}")

# st1 = Student("Nandita")
st1 = Student("Nandita", 21, 'nandita@example.com')
# print(st1.name)
st2 = Student("Tanmay", 22, 'tanmay@example.com')

# # st1.register("Vamsi", 22, 'vamsi@example.com')
st1.view()
st2.view()

# a = 10
# a = 20
# print(a)