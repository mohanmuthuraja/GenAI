

# lv_list = ["Apple", "banana", "cherry"]

# lv_list.append("orange")

# print(lv_list)

# # lv_list.pop(1)

# # print(lv_list)  

# lv_list.remove("banana")

# print(lv_list)

# lv_list = ["mango","strawberry"] + lv_list

# print(lv_list)

# sentence = " ".join(lv_list)

# print(sentence)

# print(sentence.split(" "))

# print(len(lv_list))

# print(type(lv_list))
# lv_list.sort()

# print(lv_list)


# name = "mohan"

# name = list(name)

# print(name)

# name = "".join(name)

# print(name)

# name = name.upper()

# print(name*2 + 20 * " "+"a")

# print("Length of name is:", len(name))

# print(f"length of name is :{len(name)}")    
# print("lenght of name is" + str(len(name)))


# FOR LOOP 

# IPL = ["CSK@gmail.com", "RCB@gmail.com", "MI@gmail.com", "KKR@gmail.com", "SRH2@gmail.com"]

# print(len(IPL))
# for teams in IPL:
#     team_length = len(teams)
#     for i in range(team_length):
#         print(i)
#     print(teams)

# team_length = len(teams)
# for i in range(team_length):
#     print(i)

# for teams in IPL[2]:
    # print(teams)

# print("**********")
# TEAMS = IPL[2]

# for i in TEAMS:
#     print(i) 


# list append

my_sorted_list = [10,20,30,55]

n = 35

my_sorted_list.append(n)

print(my_sorted_list)
# [10, 20, 30, 55, 35]

# my_sorted_list.sort()

# print(my_sorted_list)

for i in range(len(my_sorted_list)):
    if my_sorted_list[i] > n:
        my_sorted_list.insert(i, n)
    

print(my_sorted_list)