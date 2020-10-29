#!/bin/python3

class SkillSanta:
    """
    This is test class
    """
    skill_santa_type = "This is a Acadmay"
    def register(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def view(self):
        print(f'Name: {self.name}\nAge: {self.age}\nEmail: {self.email}')    

candi1 = SkillSanta()
candi2 = SkillSanta()

SkillSanta.register(candi1, "Pooja", 22, "pooja@gmail.com")
candi2.register("Nikhil", 21, 'nikhil@gmail.com')
# print(candi1.name)
# print(candi1.age)
# SkillSanta.view(candi1)
candi1.view()
candi2.view()





# name = "Python"
# print(help(candi1))
# # print(type(name))
# print(dir(candi1))
# print(dir(name))

