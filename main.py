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


courses = ['Math','English','Science','Social Science']

for index,course in enumerate(courses):
    print(f"Course Number {index+1}: {course}")

course_str = ','.join(courses)
print(course_str)



# Falsy Values
# False
# None
# Zero of Any Numerical Type
# Any Empty Sequence -> [],(),{},''
# Any Empty Mapping -> {}