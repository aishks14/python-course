# WAP in python to find the greatest of four numbers entered by the user using conditional statements.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Find the greatest number using conditional statements
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest = num3
elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    greatest = num4
else:
    greatest = None
# Display the greatest number
if greatest is not None:
    print("The greatest number is:", greatest) 
else:
    print("There was an error determining the greatest number.")
    
