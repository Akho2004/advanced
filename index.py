
import math


a = 5
b = 10
c = 7

a += 3
b *= 2  
c %= 4
#calculate the square root of the sum of their squares
result = math.sqrt(a**2 + b**2 + c**2)
print("the valueof a:",a)
print("the valueof b:",b)
print("the valueof c:",c)
print("the square of the sum of thier squares:", result)
#Print the final result rounded to 2 decimal places
print("the final result rounded to 2 decimal places:", round(result, 2))
# Ask the user to input three integers (x, y, z).
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
z = int(input("Enter the third integer (z): "))
# Then evaluate and print whether
is_even = (x % 2 == 0)  
is_positive = (y > 0)
is_in_range = (10 <= z <= 50)
# Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range
# Print final_condition
print("Is x even?", is_even)
print("Is y positive?", is_positive)
print("Is z between 10 and 50?", is_in_range)
print("Final condition (x is even AND y is positive AND z is in range):",
    final_condition
)
# Ask the user for their base score, then apply:
base_score = int(input("Enter your base score: "))
# Apply bonus points (+5) and late penalty (-10)
adjusted_score = base_score + 5 - 10
# Final score must not exceed 100 or drop below 0.
final_score = max(0, min(adjusted_score, 100))
# Then assign a grade.
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"
# Print the final score and grade
print("Final Score:", final_score)
print("Grade:", grade)  
 
# Input score from user
base_score = int(input("Enter your base score: "))
# Apply adjustments
adjusted_score = base_score + 5 - 10
# Clamp score between 0 and 100
final_score = max(0, min(adjusted_score, 100))
# Use if-elif-else to determine grade and print it
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"
    
print("Final Score:", final_score)
print("Grade:", grade)  
# Ask the user to input two numbers and an operation (add, subtract, multiply, divide, modulus)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide, modulus): ")

# Perform the selected operation
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    result = num1 / num2
elif operation == "modulus":
    result = num1 % num2
else:
    print("Invalid operation.")
    result = None

# Print the result
if result is not None:
    print("Result:", result)
   # Handle division/modulus by zero with error checking.
try:   
    if operation == "divide" and num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    elif operation == "modulus" and num2 == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
except ZeroDivisionError as e:
    print(e)
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide, modulus): ")
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    elif operation == "modulus":
        result = num1 % num2
    else:
        print("Invalid operation.")
        result = None
