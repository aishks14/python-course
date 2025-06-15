# WAP in python to sum a list with 5 numbers entered by the user.
number_list = []
print("Enter and sum 5 numbers of a list:")
print("----------------------------------")
num1 = float(input("Enter first number: "))
number_list.append(num1)
num2 = float(input("Enter second number: "))
number_list.append(num2)
num3 = float(input("Enter third number: "))
number_list.append(num3)
num4 = float(input("Enter fourth number: "))
number_list.append(num4)
num5 = float(input("Enter fifth number: "))
number_list.append(num5)
sum_of_numbers = sum(number_list)
print("The number list is:", number_list)
print("The sum of the numbers is:", sum_of_numbers)

# Alternatively, you can use a loop to collect the numbers
print("\n")
print("Alternate way to enter and sum 5 numbers in a list:")
print("---------------------------------------------------")
number_list = []
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    number_list.append(number)
sum_of_numbers = sum(number_list)
print("The number list is:", number_list)
print("The sum of the numbers is:", sum_of_numbers)