#!/bin/python3

from excel import OpenExcel

fh = OpenExcel("/home/eddy/Downloads/financial_sample.xlsx")

print(fh.read("17B"))