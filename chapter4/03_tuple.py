# Tuple in python
# A tuple is a collection of items that can be of different data types.
# Tuples are immutable, meaning you cannot change their content after creation.
# Tuples are defined using parentheses ().

# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Output: 1
print("Second element:", my_tuple[1])  # Output: 2
print("Last element:", my_tuple[-1])  # Output: 5

# Modifying elements in a tuple is not allowed, so the following line will raise an error
# my_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment
# However, you can create a new tuple with modified values
new_tuple = (10,) + my_tuple[1:]  # Create a new tuple with the first element changed
print("my_tuple:", my_tuple[1:])  # Output: (1, 2, 3, 4, 5)
print("New tuple with modified first element:", new_tuple)  # Output: (10, 2, 3, 4, 5)

# Tuples can also contain mixed data types
mixed_tuple = (1, "apple", 3.14, True)

# Accessing elements in a mixed tuple
print("First element in mixed tuple:", mixed_tuple[0])  # Output: 1
print("Second element in mixed tuple:", mixed_tuple[1])  # Output: apple
print("Third element in mixed tuple:", mixed_tuple[2])  # Output: 3.14
print("Fourth element in mixed tuple:", mixed_tuple[3])  # Output: True

# Nested tuples
nested_tuple = ((1, 2, 3), ("apple", "banana"), (True, False))

# Accessing elements in a nested tuple
print("First element of first tuple in nested tuple:", nested_tuple[0][0])  # Output: 1
print("Second element of second tuple in nested tuple:", nested_tuple[1][1])  # Output: banana
print("First element of third tuple in nested tuple:", nested_tuple[2][0])  # Output: True

# Modifying elements in a nested tuple is not allowed, but you can create a new nested tuple
new_nested_tuple = ((1, 20, 3), ("apple", "banana"), (True, False))  # Create a new nested tuple with modified values
print("New nested tuple with modified first element of first tuple:", new_nested_tuple)  # Output: ((1, 20, 3), ('apple', 'banana'), (True, False))