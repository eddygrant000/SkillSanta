#!/bin/python3

class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def view(self):
        print(f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}")

class Instructor(Student):
    def __init__(self, name, age, email, subject):
        Student.__init__(self, name, age, email)
        self.subject = subject
       
    def view(self):
        Student.view(self)
        print(f"Subject: {self.subject}")


st1 = Student("Nandita", 21, 'nandita@example.com')
in1 = Instructor("Sachin", 22, 'sachin@example.com', "Python")
st1.view()
in1.view()
