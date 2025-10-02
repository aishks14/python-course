# Functions:
# A function is a reusable block of code that performs a specific task.
# It helps organize code, avoid repetition, and improve readability.
# Function is defined using the keyword 'def'

# Example of a function
print("\nFuntion in python:")
print("------------------")
def greet():
    print("Hello!")

# Calling of a function is done by using its name followed by the paranthesis
# Example
greet() # Output: Hello!

# Functions with parameters
# Functions can accept the inputs(parameters) to work with the functionality for which it is defined.
# Example of function with parameter(s)

print("\nFuntion in python with parameter(s):")
print("------------------------------------")
def greet(name):
    print(f"Hello {name}") 

greet("Python")

# Another Example to calculate the average of numbers
print("\nFuntion in python to calculate the average of three numbers:")
print("------------------------------------------------------------")
def avg_num():
    total = 0
    for i in range(3):
        num_input = float(input(f"Enter number {i+1}: "))
        total += num_input
    average = total/3
    print("\nAverage: ", average)

avg_num()

# Another Example to calculate the average of numbers
print("\nFuntion in python with parameter(s) to calculate the average of three numbers:")
print("------------------------------------------------------------------------------")
for i in range(3):
    num_input = float(input(f"Enter number {i+1}: "))
    if i == 0:
        a = num_input
    elif i == 1:
        b = num_input
    elif i == 2:
        c = num_input

# Define a function to calculate average
def calculate_average(x, y, z):
    return (x + y + z) / 3

# Call the function and print the result
average = calculate_average(a, b, c)
print("\nAverage: ", average)


# Note: Function(s) can be called any number of times, anywhere in the program