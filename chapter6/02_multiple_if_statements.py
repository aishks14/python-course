# WAP in python which has multiple if statements
#     print("The character is not a valid alphabetic character.")
# WAP in python which has multiple if statements    

# WAP in python which has multiple if statements
print("\nMultiple if statements example:") 
print("---------------------------------")
# Check if a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
if number < 0:
    print("The number is negative.")
if number == 0:
    print("The number is zero.")

# Check if a number is even or odd
if number % 2 == 0:
    print("The number is even.")    
elif number % 2 != 0:
    print("The number is odd.")
else:
    print("The number is not an integer, so it cannot be classified as even or odd.")
