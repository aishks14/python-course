# User-defined Functions in Python
# User-defined functions are functions that you create yourself to perform specific tasks and promote code reuse.
# These functions require definition(s)

#Examples
# 01. Greet a user
def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))

#02. Get the square of a number
print("\nFunction in python to calculate the square of a number:")
print("-------------------------------------------------------")
def square(num):
    return num ** 2

result = square(5)
print("Square:", result)

#03. Calculate the average of a numbers
print("\nFunction in python to calculate the average of a numbers:")
print("---------------------------------------------------------")
def average(a, b, c):
    return (a + b + c) / 3

avg = average(10, 20, 30)
print("Average:", avg)

#04. Check if a number is even or odd
print("\nFunction in python to check if a number is even or odd:")
print("-------------------------------------------------------")
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

# 05. Print a multiplication table
print("\nFunction in python to print a multiplication table:")
print("---------------------------------------------------")
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(5)

# 06. Count vowels in a string
print("\nFunction in python to count vowels in a string:")
print("-----------------------------------------------")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World! We are learning python here."))

# 07. Default argument
# This is used when by default python adds an argument in case user doesn't provides the argument. 
print("\nFunction in python with default argument:")
print("-----------------------------------------")
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()
greet("Python")

# 08. Calculate the factorial of a number
print("\nFunction in python to check if a word is palindrome or not:")
print("-----------------------------------------------------------")
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))