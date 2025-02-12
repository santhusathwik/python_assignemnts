#use file path to open if it is not in the same folder

# file=open("example.txt","w")
# file.write("Hi, this is an example text")
# file.close()

#--------------------------------------------------------------------------
# file=open("example.txt","a")
# file.write("Hi, this is appended")
# file.close()
#--------------------------------------------------------------------------

# file=open("example.txt","r")
# content=file.read()
# print(content)
# file.close()

#--------------------------------------------------------------------------
#create a file exclusively ('x' mode- raises error if file exists)
# try:
#     file=open("example1.txt","x")
#     file.write("Exclusive file creation")
#     file.close()
# except FileExistsError:
#     print("File already exists")
#--------------------------------------------------------------------------

#methods to read a file-read(), readline(), readlines()

# with open("example.txt","w") as file:
#     file.write("Line1 \nLine2 \nLine3 \nLine4 \n")

#--------------------------------------------------------------------------
#reads oneline at a time

# with open("example.txt","r") as file:
#     print(file.readline())
#--------------------------------------------------------------------------

#reads content into a list

# with open("example.txt","r") as file:
#     lines=file.readlines()
#     print(lines)
#--------------------------------------------------------------------------

#using writelines()
# lines=["1Line","\n2Line"]
# with open('example1.txt',"w") as file:
#     file.writelines(lines)

#--------------------------------------------------------------------------
#create a temporary file
# with open("delete_me.txt","w") as file:
#     file.write("This file will be deleted")
#--------------------------------------------------------------------------

# import os
# if os.path.exists('delete_me.txt'):
#     os.remove('delete_me.txt')
#     print('File deleted successfully')
# else:
#     print("File not found")

#--------------------------------------------------------------------------

# try-except - Handles file-related errors gracefully
# try:
#     with open("non_existent.txt", "p") as file:
#         content=file.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file does not exist.")
# except PermissionError:
#     print("Error: Permission denied.")
# except Exception as e:
#     print(f"An unexpected error occurred: (e)")

#--------------------------------------------------------------------------