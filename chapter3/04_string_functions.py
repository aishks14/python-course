# String functions
# String to work with:

sample_string = "Hello, World!"

# Convert to uppercase
upper_string = sample_string.upper()

# Convert to lowercase
lower_string = sample_string.lower()

# Capitalize the first letter
capitalized_string = sample_string.capitalize()

# Title case
title_string = sample_string.title()

# Swap case
swapped_case_string = sample_string.swapcase()

# Check if string starts with a substring
starts_with_hello = sample_string.startswith("Hello")

# Check if string ends with a substring
ends_with_world = sample_string.endswith("World!")

# Find the index of a substring
index_of_world = sample_string.find("World")

# Count occurrences of a substring
count_of_o = sample_string.count("o")

# Split the string into a list
split_string = sample_string.split(", ")

# Join a list into a string
joined_string = " - ".join(split_string)

# Strip whitespace from both ends
stripped_string = "   Hello, World!   ".strip()

# Length of the string
string_length = len(sample_string)  # 13

# Replace a string with another
replaced_string = sample_string.replace("World", "Python")  # 'Hello, Python!'

# String formatting
formatted_string = f'{sample_string} - {replaced_string}'  # 'Hello, World! - Hello, Python!'

# Print all results
print("\nString Functions:")
print("------------------")
print("Uppercase:", upper_string)
print("Lowercase:", lower_string)
print("Capitalized:", capitalized_string)
print("Title Case:", title_string)
print("Swapped Case:", swapped_case_string)
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'World!':", ends_with_world)
print("Index of 'World':", index_of_world)
print("Count of 'o':", count_of_o)
print("Split String:", split_string)
print("Joined String:", joined_string)
print("Stripped String:", stripped_string)
print("String Length:", string_length)
print("Replaced String:", replaced_string)
print("Formatted String:", formatted_string)
