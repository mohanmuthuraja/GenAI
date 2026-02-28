# Simple Calculator

print("Basic Calculator")
print("Operations: +  -  *  /")

# Take input
num1 = float(input("Enter first number: "))

op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Calculate
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operator"

# Output
print("Result:", result)