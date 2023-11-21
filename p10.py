# Name- MD YUNUS
# Branch- B.Tech ECE 1st Year

# Function to return the result of addition
def add(a, b):
    return a + b

# Function to return the result of subtraction
def subtract(a, b):
    return a - b

# Function to return the result of multiplication
def multiply(a, b):
    return a * b

# Function to return the result of division
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate results
result_addition = add(num1, num2)
result_subtraction = subtract(num1, num2)
result_multiplication = multiply(num1, num2)
result_division = divide(num1, num2)

# Display the results
print(f"Addition: {num1} + {num2} = {result_addition}")
print(f"Subtraction: {num1} - {num2} = {result_subtraction}")
print(f"Multiplication: {num1} * {num2} = {result_multiplication}")
print(f"Division: {num1} / {num2} = {result_division}")
