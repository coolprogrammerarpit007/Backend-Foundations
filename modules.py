import os

# print(dir(os)) -> will print the all built-in methods from the module

# to get the current working directory

# print(os.getcwd())

# to change current working directory
# os.chdir('/Users/Arpit/Desktop/')

# to print folders/files inside dir
# print(os.listdir())

# to create directory
# os.makedirs('programs/tests') # -> mkdirs is used to create directory inside directory
# os.mkdir('first') #-> will create only 1-level directory not nested


# deleting folders
# rmdir and removedirs
# os.removedirs('programs/tests')
# os.rmdir('first')
# print(os.listdir()) -> to list modules and files inside directory


# renaming file

# os.rename('first.txt','second.txt')

# to print out all the info about a file
from datetime import datetime
# print(os.stat('second.txt'))
# mod_time = os.stat('second.txt').st_mtime -> will get the timestamp when file modified
# print(datetime.fromtimestamp(mod_time)) # to convert timestamp into human-readable format


# to getting a directory-name,modules inside directory and files inside

# for dirpath,dirnames,filenames in os.walk('/C/Users/Default'):
#     print(f"Directory Path: {dirpath}, Module Name: {dirnames},File Names: {filenames}")

# os.walk() -> will get tuple of three values -> dir-path,modules/directory inside and files inside that path

# to get environment variables

# print(os.environ.get('JAVA_HOME')) #-> to get environment variables  JAVA_HOME 
# os.environ.get('JAVA_HOME') tries to fetch an environment variable named "JAVA_HOME".
# If it’s not set, Python returns None.


# print(os.environ.get('HOME'))
home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
# print(home)

# file_path = os.path.join(home,'test.txt') -> to join path and file
# print(file_path)

print(os.path.basename('/tmp/test.txt')) # -> basename is test.txt
print(os.path.dirname('/tmp/test.txt')) # -> will print dir-name
print(os.path.split('/tmp/test.txt'))  # -> will get tuple of directory and file name
print(os.path.exists('/tmp/test.txt')) # will check if path 

# os.isdir() -> to check if is this a directory
# os.isfile() -> to check if it is a file
# os.path.splittext('/tmp/test.txt) -> split into root and extention ->o/p ('/tmp/test','.txt')