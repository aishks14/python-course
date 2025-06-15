# WAP in python to replace the string with single space wherever double spaces are found in a user entered string.
# Get user input for the string
input_string = input("Enter a string: ")
print("\nOriginal String:")
print("-----------------")
print(input_string)
# Replace double spaces with single space
replaced_string = input_string.replace("  ", " ")
# Print the modified string
print("\nModified String:")
print("-----------------")
print(replaced_string)

# input_string is immutable, so it will not change.
print("\nOriginal String after replacement:")
print("------------------------------------")
print(input_string)
# The original string remains unchanged after the replacement operation.