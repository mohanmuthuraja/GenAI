#1. Function : without class
# this is a function to add two numbers
# def add(a,b):
#     return a + b

# add_result = add(2, 3)
# print(add_result)

#******************************************8
# 2. function with *args and **kwargs
#******************************************8
# def add1(*args):
#     name = ""
#     for names in args:
#         name = name + names + " "
#     return name

# result = input("Enter the names with space: ")
# print("print1" + result)
# add1_result = add1(result)
# print("function output print2" + add1_result)

# #Convert string value to list : store the value of result in a list
# result_list = add1_result.split(" ")
# print(result_list)
# print(type(result_list))
# if "" in result_list:
#     result_list.remove("")  

# print(result_list)

# #convert list into string : we can use join function to convert list into string
# result_string = " ".join(result_list)  # this " " is used to join the list with space
# print(result_string)

#******************************************8
#3. function with kworgs
#******************************************8
# key value pair : key is the name of the parameter and value is the value of the parameter
#******************************************8
# with tuple
#******************************************8
# def teams(**kwargs):
#     list_key = set()
#     for key, value in kwargs.items():
#         key1 = key.upper()
#         value1 = value.lower()
#         list_key.add((key1, value1))
#     return list_key

# key_list = teams(team1 = "CSK", team2 = "RCB", team3 = "MI", team4 = "KKR", team5 = "SRH")

# print(key_list)           #output : {('TEAM1', 'csk'), ('TEAM2', 'rcb'), ('TEAM3', 'mi'), ('TEAM4', 'kkr'), ('TEAM5', 'srh')}
#******************************************8
#with set
#******************************************8
# def teams(**kwargs):
#     list_key = []
#     list_value = []
#     for key, value in kwargs.items():
#         key1 = key.upper()
#         value1 = value.lower()
#         list_key.append(key1)
#         list_value.append(value1)
#     return list_key, list_value

# key_list, value_list = teams(team1 = "CSK", team2 = "RCB", team3 = "MI", team4 = "KKR", team5 = "SRH")

# print(key_list)             #output : ['TEAM1', 'TEAM2', 'TEAM3', 'TEAM4', 'TEAM5']
# print(value_list)           #output : ['csk', 'rcb', 'mi', 'kkr', 'srh']  