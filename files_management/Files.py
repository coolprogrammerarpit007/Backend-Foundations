# File Objects

# file = open('test.txt','r')
# print(file.name)
# file.close()


# using Context Manager

# using this for reading a large file can be so memory consuming, we can iterate over line
# with open('test.txt','r') as f_hand:
#     contents = f_hand.read()
#     print(contents)
    
# f_hand.close()


# with open('test.txt','r') as f_hand:
#     for line in f_hand:
#         print(line,end='')



# Working With Files in Python


# Opening and Closing a file


# 1 way to open and close file

# try:
#     file = open('dog_breeds.txt')

# except FileExistsError:
#     print("File Does not Exist!")
    
# finally:
#     file.close()


# using with to open and close file
# with open('dog_breeds.txt','r') as fhand:
#     pass



# Reading and Writing files

# with open('dog_breeds.txt','r') as f_hand:
#     # Read and Print the entire file
#     # print(f_hand.read())
    
#     # Read and print the first 5 characters of the line 5 times
#     print(f_hand.readline(5),end='')
#     print(f_hand.readline(5),end='')
#     print(f_hand.readline(5),end='')
#     print(f_hand.readline(5),end='')
#     print(f_hand.readline(5),end='')


# Iterating over each line in the file


# with open('dog_breeds.txt','r') as f_hand:
#     line = f_hand.readline()
#     while line != '':
#         print(line,end='')
#         line = f_hand.readline()


# Another way to itterate is using readlines()

# with open('dog_breeds.txt','r') as reader:
#     for line in reader.readlines():
#         print(line,end='')

# However, the above examples can be further simplified by iterating over the file object itself:

# with open('dog_breeds.txt', 'r') as reader:
#      # Read and print the entire file line by line
#      for line in reader:
#          print(line, end='')

# This final approach is more Pythonic and can be quicker and more memory efficient. Therefore, it is suggested you use this instead.


# writing files

# with open('dog_breeds.txt','r') as reader:
#     dog_breeds = reader.readlines()
    
    
# with open('reversed_dog_breeds.txt','w') as writer:
#     for breed in reversed(dog_breeds):
#         writer.write(breed)


# Working with Bytes
# Sometimes, you may need to work with files using byte strings. This is done by adding the 'b' character to the mode argument. All of the same methods for the file object apply.

# with open('test.txt','r') as fhand:
#     # print(fhand.read())
    
#     # # reading by Iterating over lines
#     # for line in fhand:
#         # print(line,end='')
#     # with fhand.read(size) -> we can set the bytes/chars we want to read
#     f_contents = fhand.read(100) # it will print first 100 chars of our file
#     print(f_contents,end='')
#     f_contents = fhand.read(100) # it will print first 100 chars of our file
#     print(f_contents,end='')
#     f_contents = fhand.read(100) # it will print first 100 chars of our file
#     print(f_contents,end='')


# reading a big file, using chunks

# with open('test.txt','r') as f_hand:
#     size_to = 10
#     file_contents = f_hand.read(size_to)
#     # print(file_contents,end='')
#     # f_hand.seek(0) # use to set position 
#     # file_contents = f_hand.read(size_to)
#     # print(file_contents,end='')
#     # print(f_hand.tell()) # -> will tell how many chars already we have read
#     # reading file in chunks
#     while len(file_contents) > 0:
#         print(file_contents,end='')
#         file_contents = f_hand.read(size_to)


# Writing Files

# with open('test2.txt','w') as fhand:
#     fhand.write("Hello World!")

# Making copy of test.txt file

#opening test.txt and reading this file

# with open('test.txt','r') as reader:
#     test_data = reader.readlines()

# with open('test2.txt','w') as writer:
#     for data in test_data:
#         writer.write(data)

# copying a image file and writing to another file

with open('dog.png','rb') as reader:
    with open('dog_copy.png','wb') as writer:
        for data in reader:
            writer.write(data)