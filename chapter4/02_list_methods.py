# List operations/ methods in Python
# Adding elements to a list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Adds 6 to the end of the list
print("List after appending 6:", my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Inserting elements at a specific position
my_list.insert(1, 15)  # Inserts 15 at index 1
print("List after inserting 15 at index 1:", my_list)  # Output: [10, 15, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(3)  # Removes the first occurrence of 3
print("List after removing 3:", my_list)  # Output: [10, 15, 2, 4, 5, 6]

# Popping elements from a list
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)  # Output: 6
print("List after popping the last element:", my_list)  # Output: [10, 15, 2, 4, 5]

# Slicing a list
slicing_list = my_list[1:4]  # Gets elements from index 1 to 3
print("Sliced list from index 1 to 3:", slicing_list)  # Output: [15, 2, 4]

# Reversing a list
my_list.reverse()  # Reverses the list in place
print("Reversed list:", my_list)  # Output: [5, 4, 2, 15, 10]

# Sorting a list
my_list.sort()  # Sorts the list in ascending order
print("Sorted list:", my_list)  # Output: [2, 4, 5, 10, 15]

# List comprehension
# Creating a new list with squares of numbers from 1 to 5
squares_list = [x**2 for x in range(1, 6)]
print("List of squares from 1 to 5:", squares_list)  # Output: [1, 4, 9, 16, 25]

# List of strings
string_list = ["apple", "banana", "cherry"]

# Accessing elements in a string list
print("First string:", string_list[0])  # Output: apple
print("Second string:", string_list[1])  # Output: banana
print("Last string:", string_list[-1])  # Output: cherry

# Modifying elements in a string list
string_list[0] = "orange"
print("Modified string list:", string_list)  # Output: ['orange', 'banana', 'cherry']   

# List of mixed data types
mixed_list = [1, "apple", 3.14, True]

# Accessing elements in a mixed list
print("First element in mixed list:", mixed_list[0])  # Output: 1
print("Second element in mixed list:", mixed_list[1])  # Output: apple
print("Third element in mixed list:", mixed_list[2])  # Output: 3.14
print("Fourth element in mixed list:", mixed_list[3])  # Output: True

# Modifying elements in a mixed list
mixed_list[1] = "banana"
print("Modified mixed list:", mixed_list)  # Output: [1, 'banana', 3.14, True]

# List of lists (nested lists)
nested_list = [[1, 2, 3], ["apple", "banana"], [True, False]]

# Accessing elements in a nested list
print("First element of first list in nested list:", nested_list[0][0])  # Output: 1
print("Second element of second list in nested list:", nested_list[1][1])  # Output: banana
print("First element of third list in nested list:", nested_list[2][0])  # Output: True

# Modifying elements in a nested list
nested_list[0][1] = 20
print("Modified nested list:", nested_list)  # Output: [[1, 20, 3], ['apple', 'banana'], [True, False]]
