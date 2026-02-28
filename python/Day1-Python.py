        # 1- write a program which takes 3 inputs from user as principle amount (int) and rate of annual interest (float) and 
        #  tenure (in years). write a program to print total amount value at the end fo the tenure

# principle_amount = int(input("Enter the principle amount: "))
# rate_of_interest = float(input("Enter the rate of interest: "))
# tenure = int(input("Enter the tenure in years: "))

# total_amount = principle_amount * ((1 + rate_of_interest / 100) ** tenure)

# print(f"The total amount after {tenure} years is: {total_amount:.2f}")  

# print(f"the final total amount after {tenure} is :{total_amount:.2f}")
# print("the final total amount after" , str(tenure) , "is" ,f"{total_amount:.2f}")
# example : principle : 100 , interest percent 8 , tenure = 2  then amount will be : 100*1.08*1.08 = 116.64

        # 2- Odd or Even : Ask the user to enter a number. Print whether the number is even or odd.
# number = int(input("Enter a number:"))
# if number % 2 == 0:
#     print(f"number {number} is even")
# else:
#     print(f"number {number} is odd")

        # 3- Ask the user to enter their age. If age is:

        # less than 13 → print "Child"

        # between 13 and 19 → print "Teenager"

        # 20 or more → print "Adult"
# age = int(input("Enter your Age"))

# if age < 13:
#     print("child")
# elif age >=13 and age <=19:
#     print("Teenager")
# else:
#     print("Adult")

        # 4- Create two variables: username = "admin" and password = "1234".

        # Ask the user to input username and password.

        # If both match, print “Login successful”, else “Invalid credentials”.

# usernm = 'admin'
# pwd = "1234"
# username = input("enter your username: ")
# password = input("enter your password: ")

# if username == usernm and password == pwd:
#     print("Login successful")
# else:
#     print("Invalid credentials")

        # 5- Assignment 6: Find the Largest Number. Ask the user to enter three numbers a, b ,c with 3 inputs
        # Print the largest among them.

# a = int(input("enter the first number a:"))
# b = int(input("enter the second number b:"))
# c = int(input("enter the third number c:"))

# if a >= b and a >= c:
#     print(f"{a} is the largest number")
# elif b >=a and b >= c:
#     print( b , "is the largest number")
# else:
#     print(f"{c} is the largest number")

# 6- Assignment 8: Temperature Converter : Ask the user to enter temperature in Celsius

# Convert it to Fahrenheit using the formula:
# Fahrenheit = (Celsius × 9/5) + 32

        # Print the result in a user-friendly format, like:
        # "37°C is equal to 98.6°F"

# celsius = float(input("enter the celsius temperature: "))

# fahrenheit = float((celsius * 9/5) + 32)  # converting celsius to
                   
# # fahrenheit = float((celsius * 9/5) + 32

# print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")


        # 7- Number Type Checker : Ask the user to input a number.

        # Print whether it is:

        # Positive

        # Negative

        # Zero

# number = float(input("enter the number: "))

# if number > 0:
#     print(f"{number:.0f} is positive")
# elif number == 0:
#     print(f"{number:.0f} is zero")
# else:
#     print(f"{number:.0f} is negative")


        # 8- Password Strength Checker (Basic): Ask the user to enter a password.

        # If the password is:

        # Less than 6 characters → print "Weak Password"

        # 6–10 characters → print "Moderate Password"

        # More than 10 characters → print "Strong Password"
        
        # ps: you can use len function to check the string length ex len(password)

# password = input("enter your password: ")
# password_len = len(password)
# if password_len < 6:
#     print("Weak Password")
# elif password_len >= 6 and password_len <= 10:
#     print("Moderate Password")  
# else:
#     print("Strong Password")

        # 9- Leap Year Checker : Ask the user to enter a year.

        # Print whether it is a leap year or not.

        # Rules:

        # A year is a leap year if:

        # It is divisible by 4 and

        # Not divisible by 100 unless it's also divisible by 400

        # Example:

        # 2000 → Leap year

        # 1900 → Not a leap year

        # 2024 → Leap year

# year = int(input("enter the year: "))
# if(year % 4 ==0  and year % 100 != 0 ) or (year % 400 ==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# 10 - Bill Splitter with Tip: Ask the user to input:
# Total bill amount
# Tip percentage (e.g., 10 for 10%)
# Number of people
# Calculate:
# Tip amount = (bill × tip %) / 100
# Total amount = bill + tip
# Per person share = total amount / number of people
# Print all three values clearly.
# example output :
# Tip: ₹100.0
# Total Bill (with tip): ₹1100.0
# Each person should pay: ₹275.0

total_bill = float(input("Enter the total bill amount : "))

tip_percentage = float(input("Enter the tip percentage (e.g., 10 for 10%): "))

No_of_people = int(input("Enter the number of people: "))

tip_amount = (total_bill * tip_percentage) / 100  

total_amount = total_bill + tip_amount

per_person_share = total_amount / No_of_people

print(f"Tip : ₹{tip_amount:.2f}")
print(f"Total Bill ( with tip ): ₹{total_amount:.2f}")
print(f"Each person should pay : ₹{per_person_share:.2f}")


