#!/bin/python3

fh = open("data2.txt", "at+")
fh.write("From Append Method\n")
fh.seek(0)
print(fh.read())
