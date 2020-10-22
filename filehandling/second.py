##############################
    # read = 0
    # write = 0
    # truncate : wt, 
    # create a new file
    # append : at , a : end

# eddy = open('data.txt', 'w')
# eddy.write('Sachin Saini\n')
# eddy.write("Eddy Grant")
# print(eddy.read())

# user_input = input("Enter a file name: ")

# fh = open(user_input, 'w')
# n = int(input("How many names: "))
# for i in range(n):
#     data = input(f"Enter name {i+1}: ")
#     fh.write(data+'\n')

fh = open('skillsanta.txt', 'a')
print(fh.closed)
print(fh.readable())
print(fh.writable())
# print("Pointer location: ", fh.tell())
# n = int(input("How many names: "))
# for i in range(n):
#     data = input(f"Enter name {i+1}: ")
#     fh.write(data+'\n')
# fh.close()
# fh.write("EOF")

