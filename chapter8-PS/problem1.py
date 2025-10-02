# WAP in python to find the greatest of three numbers using functions

print("\nGreatest of three numbers:")
print("--------------------------")
for i in range(3):
    num_input = float(input(f"Enter number {i+1}: "))
    if i == 0:
        num1 = num_input
    elif i == 1:
        num2 = num_input
    elif i == 2:
        num3 = num_input

# Define a function to get the greatest of three numbers
def greatest_num(x, y, z):
    if (x>y and x>z):
        return x
    elif (y>x and y>z):
        return y
    else:
        return z

# Call the function and print the result
greatest = greatest_num(num1, num2, num3)
print(f"\nGreatest of three: {greatest}")