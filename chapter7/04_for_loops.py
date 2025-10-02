# Example to prnt number in range from 1 to 10 using for loop
# Using a for loop to print numbers from 1 to 10
print("\nPrint range of numbers in a single line:")
print("------------------------------------------")
for i in range(1, 11):
    print(i, end=' ') # This prints numbers from 1 to 10 in a single line

print("\n\nPrint range of numbers in multiple lines:")
print("-------------------------------------------")
for i in range(1, 11):
    print(i)  # This prints each number on a new line

# Example to print range of numbers using step size
print("\nPrint range of numbers with step size:")
print("----------------------------------------")   
for i in range(1, 101, 2):  # Step size of 2
    print(i)  # This prints odd numbers from 1 to 100
# Step size can be used to control the increment of the loop variable.
