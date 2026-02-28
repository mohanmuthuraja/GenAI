print("Hello, World!")
 
 
a = [1,24,5,6,"Mohan"]  # List : 0->1, 1->24, 2->5, 3->6, 4->"Mohan"
                        # List : -5->1, -4->24, -3->5, -2->6, -1->"Mohan"
 
# when list grows the step should be 1 and when list goes backwards the step should be -1
#for ex: [1:3:1] -> start is 1, end is 3 and step is 1; this is true and give result as [24, 5]
#for ex : [3:1:1] --> start is 3, end is 1 and step is 1; this is false and give result as []; because it goes forward and end is less than start
#for ex : [3:1:-1] --> start is 3, end is 1 and step is -1; this is true and give result as [6, 5]; because it goes backward and end is less than start
# print(a[2])             #output: 5
# print(a[1:2])           #output: [24]  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[1:3])           #output: [24, 5]  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[-1:-3])         #output: []  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[-3:-1])         #output: [5, 6]  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[-3:])           #output: [5, 6, 'Mohan']  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[:3])            #output: [1, 24, 5]  # List slicing : a[start:end] -> start is inclusive and end is exclusive  
# print(a[:])             #output: [1, 24, 5, 6, 'Mohan']  # List slicing : a[start:end] -> start is inclusive and end is exclusive
# print(a[::2])          #output: [1, 5, 'Mohan']  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[1::2])         #output: [24, 6]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[::3])          #output: [1, 6]  # List  slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[::-1])         #output: ['Mohan', 6, 5, 24, 1]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[1:4:2])        #output: [24, 6]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-1:0:-1])       #output: ['Mohan', 6, 5, 24]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-1:0:-2])       #output: ['Mohan', 5]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-2::1])        #output: [6, 'Mohan']  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-2::-1])       #output: [6, 5, 24, 1]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-1::-1])       #output: ['Mohan', 6, 5, 24, 1]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-2::-2])       #output: [6, 24]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
# print(a[-3:-1:-1])       #output: [6, 5]  # List slicing : a[start:end:step] -> start is inclusive and end is exclusive and step is the step size
 
#***********************
#List
#***********************
fruit = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
# print(fruit)  #output: ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
# print(fruit.append("Pineapple"))  #output: None; because append method does not return anything
# print(fruit)  #output: ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange', 'Pineapple']
# print(fruit[2])  #output: Mango
# print(fruit[1:4])  #output: ['Banana', 'Mango', 'Grapes']  
 
# fruit[2]= "Watermelon"  # List is mutable; we can change the value of the list
# print(fruit)  #output: ['Apple', 'Banana', 'Watermelon', 'Grapes', 'Orange', 'Pineapple']
# print(fruit.remove("Grapes"))  #output: None; because remove method does not return anything
# print(fruit)  #output: ['Apple', 'Banana', 'Watermelon', 'Orange', 'Pineapple']
# print(fruit.pop(2))  #output: Watermelon; because pop method returns the element at index 2
# print(fruit)  #output: ['Apple', 'Banana', 'Orange', 'Pineapple']
# print(fruit.append("Strawberry"))  #output: None; because add method does not return anything
# print(fruit)  #output: {'Apple', 'Banana', 'Orange', 'Pineapple', 'Strawberry'}; because fruit is a set and set does not allow duplicate elements; so it will not add "Strawberry" to the set because it is already present in the set
 
#***********************
#tuples are immutable; we cannot change the value of the tuple; we cannot add or remove elements from the tuple
#***********************
# colors = ("Red", "Green", "Blue")  # Tuple : 0->Red, 1->Green, 2->Blue
# print(colors[1])  #output: Green
# print(type(colors))  #output: <class 'tuple'>; because colors is a tuple
 
#***********************
#set is mutable; we can add or remove elements from the set; but set is unordered; we cannot access the elements of the set by index; set does not allow duplicate elements
#***********************
# numbers = {1, 2, 3, 4, 5}  # Set : 1, 2, 3, 4, 5
# print(numbers)  #output: {1, 2, 3, 4, 5}
# print(type(numbers))  #output: <class 'set'>; because numbers is a set
# numbers.add(6)  # Set is mutable; we can add elements to the set
# print(numbers)  #output: {1, 2, 3, 4, 5, 6}
# numbers.remove(3)  # Set is mutable; we can remove elements from the set
# print(numbers)  #output: {1, 2, 4, 5, 6}
# # print(numbers[3])  #output: TypeError: 'set' object is not subscriptable; because set is unordered and we cannot access the elements of the set by index
 
#***********************
#Dictionary is mutable; we can add or remove elements from the dictionary; but dictionary is unordered; we cannot access the elements of the dictionary by index; dictionary does not allow duplicate keys; but dictionary allows duplicate values
#***********************
student = {"name": ["Mohan","Rahul"], "age": 20, "city": "Delhi"}  # Dictionary : key->value; name->Mohan, age->20, city->Delhi
print(student)  #output: {'name': 'Mohan', 'age': 20, 'city': 'Delhi'}
# print(type(student))  #output: <class 'dict'>; because student is a dictionary
# print(student["name"])  #output: Mohan; because we can access the value of the dictionary by using the key
# student["age"] = 21  # Dictionary is mutable; we can change the value of the dictionary
# print(student)  #output: {'name': 'Mohan', 'age': 21, 'city': 'Delhi'}
# student["name"] = "Rahul"  # Dictionary is mutable; we can change the value of the dictionary
# print(student)  #output: {'name': 'Rahul', 'age': 21, 'city': 'Delhi'}
# print(student["name"][0])  #output: R; because student["name"] is a string and we can access the characters of the string by index
# print(student["name"][1])  #output: a; because student["name"] is  
student["name"].append("Mohan")  # Dictionary is mutable; we can change the value of the dictionary; but student["name"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': 'Rahul', 'age': 21
student["name"].remove("Mohan")  # Dictionary is mutable; we can change the value of the dictionary; but student["name"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': 'Rahul', 'age': 21, 'city': 'Delhi'}  
#how to remove all Mohan from student["name"] list
student["name"] = [name for name in student["name"] if name != "Mohan"]  
# List comprehension; it will create a new list with all the elements of student["name"] except "Mohan"
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi'}; because we have removed all the "Mohan" from student["name"] list
 
student["State"] = "Telangana"
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi', 'State': '[Telangana]'}; because we have added a new key-value pair to the dictionary
#how to insert one more State in the dictionary; but we cannot have duplicate keys in the dictionary; so we will change the value of the key "State" to a list and add the new state to the list
student["State"] = [student["State"], "Maharashtra"]  # Dictionary is mutable; we can change the value of the dictionary; but student["State"] is a string and string is immutable; so it will give an error
student["State"].append("Karnataka")  # Dictionary is mutable; we can change the value of the dictionary; but student["State"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi', 'State': ['Telangana', 'Maharashtra']}; because we have changed the value of the key "State" to a list and added the new state to the list
#how to remove State from the dictionary; we can use pop method to remove the key-value pair from the dictionary
#student.pop("State")  # Dictionary is mutable; we can remove elements from the dictionary
#print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi', 'State': 'Maharashtra'}; because we have changed the value of the key "State" in the dictionary
student["state1"] = "Tamilnadu"  # Dictionary is mutable; we can add new key-value pairs to the dictionary
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi', 'State': 'Maharashtra', 'state1': 'Tamilnadu'}; because we have added a new key-value pair to the dictionary
student.pop("state1")  # Dictionary is mutable; we can remove elements from the dictionary
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'city': 'Delhi', 'State': 'Maharashtra'}; because we have removed the key-value pair with key "state1" from the dictionary
student["State"].remove("Maharashtra")  # Dictionary is mutable; we can change the value of the dictionary; but student["State"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': ['Rahul'], 'age': 21
student.pop("State")  # Dictionary is mutable; we can remove elements from the dictionary
student["State2"] = "Kerala"  # Dictionary is mutable; we can add new key-value pairs to the dictionary; but student is a dictionary and we cannot add a new key-value pair to the dictionary with the same key; so it will give an error
print(student)  #output: {'name': ['Rahul'], 'age': 21
student["State2"] = "Tamilnadu"  # Dictionary is mutable; we can change the value of the dictionary; but student["State2"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': ['Rahul'], 'age': 21  
student["State2"] = [student["State2"], "Kerala"]  # Dictionary is mutable; we can change the value of the dictionary; but student["State2"] is a string and string is immutable; so it will give an error
print(student)  #output: {'name': ['Rahul'], 'age': 21, 'State2': ['Tamilnadu', 'Kerala']}; because we have changed the value of the key "State2" to a list and added the new state to the list
student.update({"State2": "Karnataka"})  # Dictionary is mutable; we can change the value of the dictionary; but student["State2"] is a string and string is immutable; so it will give an error
print(student.keys())  # Dictionary is mutable; we can access the values of the dictionary by using the values method
print(student.values())  # Dictionary is mutable; we can access the values of the dictionary by using the values method
print(student.items())  # Dictionary is mutable; we can access the key-value pairs of the dictionary by using the items method
print(student)  #output: {'name': ['Rahul'], 'age': 21}; because we have removed the key-value pair with key "State2" from the dictionary
student["name"] = "welcome"
print(student)  #output: {'name': 'welcome', 'age': 21}; because we have changed the value of the key "name" in the dictionary
student.pop("name")  # Dictionary is mutable; we can remove elements from the dictionary
print(student)  #output: {'age': 21}; because we have removed the key
student["name"] = "Mohan"
print(student)  #output: {'age': 21, 'name': 'Mohan'}; because we have added a new key-value pair to the dictionary
student["name"] = {student["name"],"Rahul"}  # Dictionary is mutable; we can change the value of the dictionary; but student["name"] is a string and string is immutable; so it will give an error
print(student)  #output: {'age': 21, 'name': 'Mohan', 'Rahul'}; because we have changed the value of the key "name" to a set and added the new name to the set
