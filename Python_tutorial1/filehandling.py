# import os

# print(os.getcwd())

# file = open("test.txt", "w")
# file.write("Hello, this is a test file.\n")
# file.write("This file is used for demonstrating file handling in Python.\n")
# file.close()

# file=open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()
                                                                                                                                        
file = open("test.txt", "a")
file.write("This line is appended to the file.\n")
file.close()

#to use open function which package i should import?
#No need to import any package to use the open function in Python. The open function is a built-in function that is available by default in Python, so you can use it directly without importing any additional modules.

#WHAT IS THE USE OF OS packge?
#The os package in Python provides a way to interact with the operating system. It allows you to perform various tasks such as working with files and directories, managing processes, and accessing environment variables. Some common uses of the os package include:
#1. File and Directory Management: You can use os to create, delete, and manipulate files and directories. For example, you can create a new directory, list the contents of a directory, or check if a file exists.
#2. Path Manipulation: The os.path module provides functions for working with file paths, such as joining paths, splitting paths, and getting the absolute path of a file.
#3. Environment Variables: You can use os to access and modify environment variables, which are used to store configuration settings and other information for the operating system and applications.
#4. Process Management: The os module allows you to manage processes, such as creating new processes, terminating processes, and getting information about running processes.
#Overall, the os package is a powerful tool for interacting with the operating system and performing various tasks related to file handling, process management, and environment variables in Python.       

