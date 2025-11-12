# import os

# # change directory
# # Prefix the string with r to tell Python not to interpret backslashes:
# os.chdir(r'C:\Users\Dell\Downloads\images_files_download')
# # print(os.getcwd()) # -> to check current working directory

# # to list everything in the directory

# for l in enumerate(os.listdir()):
#     # print(l)
#     file_name,file_ext = os.path.splitext(l)
#     # print(file_name,file_ext)
#     # print(file_name.split(' '))
#     file_title,file_number = file_name.split(' ')
#     # print(file_title)
#     new_name = f"{file_title}{file_ext}"
#     os.rename(l,new_name)


import os

file_path = r'C:\Users\Dell\Downloads\images_files_download'

# change directory

os.chdir(file_path) # -> to get current working directory

files = os.listdir() # -> list all modules and files in the path

# sort files to rename it into consistent order
files.sort()


# loop through each file to rename

for index,f in enumerate(files,start=1):
    file_ext = os.path.splitext(f)[1] # -> get extension from the file
    
    if file_ext.lower() not in ['.jpg','.jpeg','.png','.webp']:
        continue
    
    # Build New file Name
    new_file_name = f"Walpaper-img-{index}{file_ext}"
    
    # rename file to new name
    os.rename(f,new_file_name)

