# print("Hello World!")
# message = 'Nice to meet you!'
# # print(message)

# greeting = 'Hello'
# name = 'Arpit'

# updated_msg = '{}, {}. {}'.format(greeting,name,message)
# # print(updated_msg)


# print(dir(name)) -> returns the method and attributes associated with obj
# help(str)

# help(str)


# courses = ['Math','English','Science','Social Science']

# for index,course in enumerate(courses):
#     print(f"Course Number {index+1}: {course}")

# course_str = ','.join(courses)
# print(course_str)



# Falsy Values
# False
# None
# Zero of Any Numerical Type
# Any Empty Sequence -> [],(),{},''

# Any Empty Mapping -> {}


# An In-depth look at pip -> python package management system




# for i in range(1,6):
#     print(str(i)*i)


# Scoping In Python

# '''
# # LEGB -> Local,Enclosing,Global.Built-In
# Python first checks in local then enclosing scope then Into Global Scope then Into Built-In Scope
# '''

# x = 'Global X'

def test():
    global x
    x = 'Local X'
    print(x)
    
    
# test()
# print(x)


# Enclosing Scope
# x = 500
def test1():
    x = 100
    def test2():
        print(x)
        
    test2()
    
# test1()
# print(x)


def outer():
    x = 'Outer X'
    def inner():
        # x = 'Inner X'
        nonlocal x
        x = 'Updated to Inner X'
        print(x)
        
    inner()
    print(x)
    
# outer()

my_list = [0,1,2,3,4,5,6,7,8,9]

# -7 index = 3
# 5 index = 5
# print(my_list[-7:5]) 
# print(my_list[-2:1:-1])

# +ve step -> Means slicing direction is rightward from left to right
# -ve step -> Means slicing direction is leftward from right to left -> reverse order

# List,Set and Dictionary Comprehensions

num_list = [number*number for number in my_list]
# print("Number List!")
# print(num_list)

# using maps in python

squared_number_list = list(map(lambda x:x*x,my_list))
# print("Square Number List")
# print(squared_number_list)

even_num_list = [number for number in my_list if number % 2==0]
# print(even_num_list)


# Using Filter in Python

filtered_even_numbers = list(filter(lambda x:x%2 ==0,my_list))
# print(filtered_even_numbers)

alphabet_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(alphabet_list)


# dictionary Comprehensions

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','SpiderMan','Wolverine','Deadpool']

# zip function in python -> it takes to lists and convert it into list of tuples
# print(list(zip(names,heros)))

my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
    
    
# print(my_dict)

# dictionary_comprehensions

my_hero_dict = {name:hero for name,hero in zip(names,heros) if name != 'Peter'}
# print(my_hero_dict)


# Set Comprehensions
numbers = [100,100,200,200,300,300,400,400,500,500,600,600,700,700,800,800,900,900,1000,1000]
my_set = {number for number in numbers}
# print(my_set)    


# Generator Expressions

nums = [1,2,3,4,5,6,7,8,9,10]
my_gen = (num*num for num in nums)
# print(my_gen)

for num in my_gen:
    print(num)

# generators 

def my_generator():
    for i in range(5):
        yield i  # instead of return
 
gen = my_generator()

for value in gen:
    print(value)
