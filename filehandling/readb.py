#!/bin/python3


# fh = open("code.jpg", "rb")
# print(fh.read())

# you have to tak file name form user : 
# you hvae to desti from user : 

filename = input("Enter filename: ") # code.jpg
destination = input("Enter destination: ")  # /home/eddy/Python3/batch/SkillSanta/filehandling/data
                                            # C:\User\Downloads\
fh = open(filename, "rb")
data = fh.read()
fh.close()
 
final_dest = destination + "/" + filename.split("/")[-1]

fh = open(final_dest, "wb")
fh.write(data)
fh.close()