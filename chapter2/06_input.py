#Input 
a = input("Enter number 1: ")
b = input("Enter number 2: ")

print("You entered:", a, "and", b)
print("Sum of a and b:", a + b)  # This will concatenate the strings
# To perform addition, we need to convert the inputs to integers or floats

print("\nAfter type conversion:")
print("------------------------")
# This script demonstrates how to take user input and perform arithmetic operations on it.
# Convert inputs to integers before adding
# Note: The input function returns a string, so we need to convert it to an integer (or float) for arithmetic operations.


#print("Sum of a and b (after conversion to int):", int(a) + int(b))  # Convert to integers
#print("Sum of a and b (after conversion to float):", float(a) + float(b))  # Convert to floats

# Note: If the inputs are not valid numbers, this will raise a ValueError.
# To handle invalid inputs, we can use a try-except block

try:
    print("Sum of a and b (after conversion to int):", int(a) + int(b))  # Convert to integers
    print("Sum of a and b (after conversion to float):", float(a) + float(b))  # Convert to floats
except ValueError:
    print("Invalid input! Please enter valid numbers.")