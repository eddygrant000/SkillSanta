# i want to read a text file data.txt


# open('data.txt', 'r')
# open('data.txt')
# open(file='data.txt', mode='rt')

fh = open('data.txt') # return a file object
# print(fh.read())
# print('Current Location: ', fh.tell())
# print(fh.read(3))
# fh.seek(0)
# print('Current Location: ', fh.tell())
# print(fh.read(5))
# print('Current Location: ', fh.tell())

# print('Current Location: ', fh.tell())
# print(fh.readline())
# print('Current Location: ', fh.tell())
# print(fh.readline())
# print('Current Location: ', fh.tell())
print(fh.readlines()[2]) # return a list 