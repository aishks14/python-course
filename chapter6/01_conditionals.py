# Conditional statements in python
# are used to perform different actions based on different conditions.
# The most common conditional statements are `if`, `elif`, and `else`.
# The `if` statement evaluates a condition and executes a block of code if the condition is true.
# The `elif` statement allows you to check multiple conditions, and the `else` statement executes a block of code if none of the previous conditions are true.

# Example of using conditional statements in Python
# WAP in python to check if a number is positive, negative, or zero

print("\nCheck if a number is positive, negative, or zero:")
print("--------------------------------------------------")
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# WAP in python to check if a number is even or odd
print("\nCheck if a number is even, or odd:")
print("----------------------------------")
number = float(input("\Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
elif number % 2 != 0:
    print("The number is odd.")

# WAP in python to check if a number is prime or not
print("\nCheck if a number is prime or not:")
print("----------------------------------")
number = int(input("Enter a number: "))
if number <= 1:
    print("The number is not prime (it must be greater than 1).")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")   

# WAP in python to check if a year is a leap year or not
print("\nCheck if a year is a leap year or not:")
print("---------------------------------------")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")   
else:
    print("The year is not a leap year.")

# WAP in python to check if a character is a vowel or consonant
print("\nCheck if a character is a vowel or consonant:")
print("------------------------------------------------")
char = input("Enter a character: ").lower()  # Convert to lowercase for uniformity  
if char in 'aeiou':
    print("The character is a vowel.")
elif char.isalpha():
    print("The character is a consonant.")
else:
    print("The input is not a valid alphabet character.")

# WAP in python to check if a person is minor, adult, senior citizen, or invalid age
print("\nCheck if a person is minor, adult, senior citizen, or invalid age:")
print("--------------------------------------------------------------------")
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.") 
elif 18 <= age < 60:
    print("You are an adult.")
elif 60 <= age < 100:
    print("You are a senior citizen.")
else:
    print("You have entered an invalid age.")

