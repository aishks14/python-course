# Example of a while loop in Python
# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')

# --------------------------------------------------------------------------------------------------------------
# Example of a while loop with user input
# This example demonstrates how to use a while loop to repeatedly ask the user for input until they enter 'exit'.
user = ""
while user.lower() != "exit":
    user = input("Enter a command (type 'exit' to quit): ")
    print(f"You entered: {user}")

# --------------------------------------------------------------------------------------------------------------
# Example to print 'Python' 5 times using a while loop
count = 0
while count < 5:
    print("Python")
    count += 1
# This loop will print 'Python' 5 times, incrementing the count each time until it reaches 5.
# --------------------------------------------------------------------------------------------------------------