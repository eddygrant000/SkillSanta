#!/bin/python3


file2 = open("/home/eddy/Python3/batch/SkillSanta/filehandling/data2.txt", "rt+")
# print(file2)

# print(file2.read()) # read all file in single shot
# print(file2.readline()) 
# print(file2.read())
# file2.write("RT+")

file2.write("Thi") # 0--> 3
file2.seek(0)
print(file2.read())
