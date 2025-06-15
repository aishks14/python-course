# Skip in slicing a long string
# Skip in slicing allows you to access elements at regular intervals in a list or string.
# It uses a step value in the slicing syntax, which can be positive or negative.
# Skip in Slicing Example:
name = "Python Programming"
# Accessing every second character
every_second_character = name[::2]  # 'Pto rgamn'

# Accessing every third character
every_third_character = name[::3]  # 'Ph oai'

# Accessing every fourth character
every_fourth_character = name[::4]  # 'Poran'

# Accessing every second character in reverse order
every_second_character_reversed = name[::-2]  # 'gimroPnhy'

# Accessing every third character in reverse order
every_third_character_reversed = name[::-3]  # 'gmrrnt'

# Accessing every fourth character in reverse order
every_fourth_character_reversed = name[::-4]  # 'gmony'

# Accessing every second character from the end
every_second_character_from_end = name[-1::-2]  # 'gimroPnhy'

# Accessing every third character from the end
every_third_character_from_end = name[-1::-3]  # 'gmrrnt'

# Accessing every fourth character from the end
every_fourth_character_from_end = name[-1::-4]  # 'gmony'

# Accessing every second character starting from index 1
every_second_character_from_index_1 = name[1::2]  # 'yhnPormig'

# Accessing every third character starting from index 1
every_third_character_from_index_1 = name[1::3]  # 'yoPgmn'

# Accessing every fourth character starting from index 1
every_fourth_character_from_index_1 = name[1::4]  # 'ynomg'

# Print all results:
print("\nSkip in Slicing Example:")
print("--------------------------")
print("Every Second Character:", every_second_character)
print("Every Third Character:", every_third_character)
print("Every Fourth Character:", every_fourth_character)
print("Every Second Character Reversed:", every_second_character_reversed)
print("Every Third Character Reversed:", every_third_character_reversed)
print("Every Fourth Character Reversed:", every_fourth_character_reversed)
print("Every Second Character from End:", every_second_character_from_end)
print("Every Third Character from End:", every_third_character_from_end)
print("Every Fourth Character from End:", every_fourth_character_from_end)
print("Every Second Character from Index 1:", every_second_character_from_index_1)
print("Every Third Character from Index 1:", every_third_character_from_index_1)
print("Every Fourth Character from Index 1:", every_fourth_character_from_index_1)