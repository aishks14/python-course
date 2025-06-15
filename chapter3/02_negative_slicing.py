# Negative Slicing
# Negative slicing allows you to access elements from the end of a list or string.  
# It uses negative indices, where -1 refers to the last element, -2 to the second last, and so on.

# Negative Slicing Example:
name = "Python Programming"

# Accessing the last character
last_character = name[-1]  # 'g'

# Accessing the second last character
second_last_character = name[-2]  # 'n'

# Accessing a substring from the end
substring_from_end = name[-11:]  # 'Programming'

# Accessing a substring using negative indices
substring_negative_indices = name[-16:-11]  # 'Pytho'   

# Accessing the last three characters
last_three_characters = name[-3:]  # 'ing'

# Accessing the first three characters using negative indices
first_three_characters = name[:-16]  # 'Pyt'

# Accessing the middle part of the string using negative indices
middle_part = name[-16:-3]  # 'Python Progra'

# Accessing the entire string using negative indices
entire_string = name[:]  # 'Python Programming'

# Accessing the string in reverse order
reversed_string = name[::-1]  # 'gnimmargorP nohtyP'

# Accessing every second character in reverse order
every_second_character_reversed = name[::-2]  # 'gmr ohtyP'

# Accessing every second character from the end
every_second_character_from_end = name[-1::-2]  # 'gmr ohtyP'

# Accessing the first five characters using negative indices
first_five_characters = name[:-16]  # 'Pyt'

# Accessing the last five characters using negative indices
last_five_characters = name[-5:]  # 'ming'

# Accessing the first eleven characters using negative indices
first_eleven_characters = name[:-7]  # 'Python Pro'

# Accessing the last eleven characters using negative indices
last_eleven_characters = name[-11:]  # 'Programming'

# Print all results:
print("\nNegative Slicing Example:")
print("--------------------------")
print("Last Character:", last_character)
print("Second Last Character:", second_last_character)
print("Substring from End:", substring_from_end)
print("Substring using Negative Indices:", substring_negative_indices)
print("Last Three Characters:", last_three_characters)
print("First Three Characters using Negative Indices:", first_three_characters)
print("Middle Part using Negative Indices:", middle_part)
print("Entire String using Negative Indices:", entire_string)
print("Reversed String:", reversed_string)
print("Every Second Character in Reverse Order:", every_second_character_reversed)
print("Every Second Character from End:", every_second_character_from_end)
print("First Five Characters using Negative Indices:", first_five_characters)
print("Last Five Characters using Negative Indices:", last_five_characters)
print("First Eleven Characters using Negative Indices:", first_eleven_characters)
print("Last Eleven Characters using Negative Indices:", last_eleven_characters)


