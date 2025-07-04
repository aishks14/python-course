# Built in functions in Python
# Built-in functions are functions that are predefined in Python and available for immediate use without needing to import any module.
# These functions usually don't require definition(s)

# Examples
# 01. print() - Displays out on the screen
print("\nprint() function in python:")
print("---------------------------")
numbers = [10, 20, 30]
print("Total:", sum(numbers))

# 02. len() - Returns the length of a sequence
print("\nlen() function in python:")
print("-------------------------")
text = "Python"
print(f"Length of text '{text}':", len(text))

# 03. type() - Returns the data type of a variable
print("\ntype() function in python:")
print("--------------------------")
number = 42
print("Type of number:", type(number))

numbers = [10, 5, 8, 2, 1, 15, 20, 25]

# 04. sum() - Return the sum of elements in an iterable
print("\nsum() function in python:")
print("-------------------------")
print("Sum:", sum(numbers))

# 05. max() - Returns the largest item
print("\nmax() function in python:")
print("-------------------------")
print("Max:", max(numbers))

# 06. min() - Returns the smallest item
print("\nmin() function in python:")
print("-------------------------")
print("Min:", min(numbers))

# 07. range() - Generates a sequence of numbers
print("\nrange() function in python:")
print("---------------------------")
print("Range output:", list(range(9)))

#08. sorted() - Returns a sorted list
print("\nsorted() function in python:")
print("----------------------------")
print("Sorted list:", sorted(numbers))

#09 input() - Takes input from the user
print("\ninput() function in python:")
print("--------------------------")
name = input("Enter your name:")
print(f"Welcome {name}")