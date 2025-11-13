# Generators and decorators

# Generators

# def square_numbers(*nums):
#     for num in nums:
#         yield num*num
        
# result = square_numbers(1,2,3,4,5)

# for num in result:
#     print(f"Square: {num}")


# Source - https://stackoverflow.com/q
# Posted by SaiKiran, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-13, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/a
# Posted by H S Umer farooq, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-13, License - CC BY-SA 3.0

# import memory_profiler as mem_profile
# import random
# import time

# names = ['Kiran','King','John','Corey']
# majors = ['Math','Comps','Science']

# print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

# def people_list(num_people):
#     results = []
#     for i in num_people:
#         person = {
#                     'id':i,
#                     'name': random.choice(names),
#                     'major':random.choice(majors)
#                   }
#         results.append(person)
#     return results

# def people_generator(num_people):
#     for i in range(num_people):
#         person = {
#                     'id':i,
#                     'name': random.choice(names),
#                     'major':random.choice(majors)
#                   }
#         yield person

# t1 = time.clock()
# people = people_list(10000000)
# t2 = time.clock()


# # t1 = time.clock()
# # people = people_generator(10000000)
# # t2 = time.clock()

# print('Memory (After): {}Mb'.format(mem_profile.memory_usage_resource()))
# print('Took {} Seconds'.format(t2-t1))


# # decorators -> dynamically alter the functuanillity of your function


def decorator_function(org_function):
    def wrapper_function():
        return org_function()
    return wrapper_function

@decorator_function
def display():
    print('Display Function Ran!')
    
    
# decorated_display = decorator_function(display)
# decorated_display()

display()

