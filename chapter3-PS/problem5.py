# WAP in python to format a sting using escape sequence characters
# Get user input for the string
input_string = input("Enter a string: ")
# Print the original string
print("\nOriginal String:")
print("-----------------")
print(input_string)
# Format the string using escape sequence characters
formatted_string = input_string.replace(".", ".\n\t")
# Print the formatted string
print("\nFormatted String:")
print("-----------------")
print(formatted_string)
# The formatted string will show escape sequences for newline.