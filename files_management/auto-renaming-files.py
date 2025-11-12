import os

# change directory
# Prefix the string with r to tell Python not to interpret backslashes:
os.chdir(r'C:\Users\Dell\Downloads\images_files_download')
# print(os.getcwd()) # -> to check current working directory

# to list everything in the directory

for l in enumerate(os.listdir()):
    # print(l)
    file_name,file_ext = os.path.splitext(l)
    # print(file_name,file_ext)
    # print(file_name.split(' '))
    file_title,file_number = file_name.split(' ')
    # print(file_title)
    new_name = f"{file_title}{file_ext}"
    os.rename(l,new_name)