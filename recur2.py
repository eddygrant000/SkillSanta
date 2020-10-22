#!/bin/python3

# understand 
data = [10, 100, [2, [3, 3, 4], [12, 34, [12, 4, 5,[2, 4,]]], [10]]]
data2 = [[[10, 20]], [[[[[[10]], 20]]], 30], [1,[2]]]
# output : [10, 100, 2, 3, 4 ,5, 12, 34, 12.........]
# data[0]
# data[1]
# data[2][0]


data3 = [10, 100, [2, [3, 3, 4]]]

temp = []
def solution(sample): # [2, [3, 3, 4]]
    for num in sample:  #num=10
        if isinstance(num, list):
            solution(num)
        else:
            temp.append(num)
    return temp

print(data2)
print(solution(data2))