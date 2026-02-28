# class and methods
# class math:
    
#     def add(self,a, b):
        
#         return a + b
    

# obj = math()


# result = obj.add(2, 3)
# print(result)

# def sub(a, b):
    
#     return a - b

# a = input("Enter two numbers with space: ")
# a_list = a.split(" ")
# print(a_list)
# v1 = int(a_list[0])
# v2 = int(a_list[1])
# sub_result = sub(v1, v2)
# print(sub_result)

# 2 . Class : Constructor
# from os import name


# EMPLOYEE, ENTER OFFICE, BANK ACOCUNT  INPUT ( NAME, AADHAR )
class EMPLOYEE:
    
    def __init__(self,name, aadhar):
        self.name = name
        self.aadhar = aadhar
        
    def officeentry(self):
        print(f"{self.name} has entered the office")
        

obj1 = EMPLOYEE("mohan", 1234567890)
obj1.officeentry()