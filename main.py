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
    
outer()