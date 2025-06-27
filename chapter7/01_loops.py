# Loops in python
# Loops are used to iterate over a sequence (like a list, tuple, or string) or to repeat a block of code multiple times.
# There are two main types of loops in Python: `for` loops and `while` loops.

# 1. For Loop
# A `for` loop is used to iterate over a sequence (like a list, tuple, or string).
# It allows you to execute a block of code for each item in the sequence.

# Example to print number from 1 to 5 without loop
print(1)
print(2)
print(3)
print(4)
print(5)

# Same above code can be done using loop
# Example of a for loop to print numbers from 1 to 5
print("\nFor loop example in a range:")
for i in range(1, 6):
    print(i)

# Example of a for loop
my_list = [1, 2, 3, 4, 5]
print("For loop example in a list:")
for item in my_list:
    print(item)
# -----------------------------------------------------------------------------
# 2. While Loop
# A `while` loop is used to repeat a block of code as long as a specified condition is true.
# It continues to execute until the condition becomes false.
count = 0
print("\nWhile loop example:")
while count < 5:
    print(count)
    count += 1

# The loop stops when count reaches 5, as the condition `count < 5` becomes false.
# This is a simple example of a while loop that counts from 0 to 4.
# The loop will continue to execute as long as the condition is true.
# The `count` variable is incremented by 1 in each iteration, ensuring that the loop will eventually terminate.
# If the condition is never met, the loop will run indefinitely, which can lead to an infinite loop.

# -----------------------------------------------------------------------------
# 3. Range Function
# note: The range function generates a sequence of numbers, which is commonly used in for loops.
# It can take one, two, or three arguments: start, stop, and step.
# Example of using range in a for loop