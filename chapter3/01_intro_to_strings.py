# Introduction to strings in Python
# Strings are sequences of characters enclosed in quotes

# Single quotes
single_quote_string = 'Hello, World!'

# Double quotes
double_quote_string = "Hello, World!"

# Triple quotes for multi-line strings
triple_quote_string = """\nThis is a multi-line string.
It can span multiple lines.\n"""

# Escape characters
escaped_string = 'He said, "Hello, World!"'

# Raw strings (ignores escape characters)
raw_string = r'This is a raw string. \n It does not interpret escape characters.'

# String concatenation
concatenated_string = single_quote_string + ' ' + double_quote_string

# String repetition
repeated_string = single_quote_string * 3

# String indexing and slicing
first_character = single_quote_string[0]  # 'H'
last_character = single_quote_string[-1]  # '!'
substring = single_quote_string[0:5]  # 'Hello'

# String length
string_length = len(single_quote_string)  # 13

# String methods
upper_case_string = single_quote_string.upper()  # 'HELLO, WORLD!'
lower_case_string = single_quote_string.lower()  # 'hello, world!'
title_case_string = single_quote_string.title()  # 'Hello, World!'

# String replacement
replaced_string = single_quote_string.replace('World', 'Python')  # 'Hello, Python!'

# String splitting
split_string = single_quote_string.split(', ')  # ['Hello', 'World!']

# String joining
joined_string = ', '.join(split_string)  # 'Hello, World!'

# String formatting
formatted_string = f'{single_quote_string} - {double_quote_string}'  # 'Hello, World! - Hello, World!'

# Print all results
print("\nIntroduction to strings:")
print("--------------------------")
print("Single Quote String:", single_quote_string)
print("Double Quote String:", double_quote_string)
print("Triple Quote String:", triple_quote_string)
print("Escaped String:", escaped_string)
print("Raw String:", raw_string)
print("Concatenated String:", concatenated_string)
print("Repeated String:", repeated_string)
print("First Character:", first_character)
print("Last Character:", last_character)
print("Substring:", substring)
print("String Length:", string_length)
print("Upper Case String:", upper_case_string)
print("Lower Case String:", lower_case_string)
print("Title Case String:", title_case_string)
print("Replaced String:", replaced_string)
print("Split String:", split_string)
print("Joined String:", joined_string)
print("Formatted String:", formatted_string)
# This code snippet introduces various string operations in Python.
# It covers string creation, concatenation, repetition, indexing, slicing,
# length calculation, and common string methods such as upper, lower, title,
# replace, split, join, and formatting.