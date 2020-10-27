#!/bin/python3


fh = open("data2.txt", "wt+")
fh.write("Sachin From SkillSanta\n")
fh.write("Python Training\n")
# print("Cursor Location: ", fh.tell())
fh.seek(0)
# print("Cursor Location: ", fh.tell())
print(fh.read()) # use less
# print("Cursor Location: ", fh.tell())
