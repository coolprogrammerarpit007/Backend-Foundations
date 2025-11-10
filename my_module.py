print("Importing My Module....")

test = 'Test String'


def find_search(to_search,target):
    ''' Finds the index of target value in search string!'''
    for index,value in enumerate(to_search):
        if target == value:
            return index
        

    return -1


result = find_search('Hello','l')
# print(f"Index Position Found: {result}")