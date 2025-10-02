#WAP in python to input eight numbers from the user and display all the unique numbers (once)

# WAP in python to input eight numbers from the user and display all the unique numbers (once)

numbers = set()  # Using a set to store unique numbers
print("Enter 8 numbers (duplicates will be ignored):")
for i in range(8):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.add(num)  # Add the number to the set (duplicates are ignored)
print("Unique numbers entered:", numbers)
# Display the unique numbers
print("Unique numbers in the order they were entered:")
for num in numbers:
    print(num, end=' ') # This prints each unique number on the same line
print()  # Print a newline for better formatting
