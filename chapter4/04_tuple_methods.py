#tuple methods in python
# Tuples have fewer methods compared to lists, but they do have some useful ones.

my_tuple = (1, 2, 3, 4, 2, 7, 8, 6, 6, 5)
# Count the occurrences of an element in a tuple
count_of_2 = my_tuple.count(2)
print("Count of 2 in my_tuple:", count_of_2)  # Output: 1

# Find the index of an element in a tuple
index_of_3 = my_tuple.index(3)
print("Index of 3 in my_tuple:", index_of_3)  # Output: 2

# Length of a tuple
length_of_tuple = len(my_tuple)
print("Length of my_tuple:", length_of_tuple)  # Output: 5

# Example of a new tuple
new_tuple = (10,) + my_tuple[1:]

# Concatenating tuples
concatenated_tuple = my_tuple + new_tuple
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 10, 2, 3, 4, 5)

# Repeating a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Tuple unpacking
a, b, c, d, e, f, g, h, i, j = my_tuple
print("Unpacked values:", a, b, c, d, e, f, g, h, i , j)  # Output: Unpacked values: 1 2 3 4 5

# Tuples can also contain mixed data types
mixed_tuple = (1, "apple", 3.14, True)

# Nested tuples
nested_tuple = ((1, 2, 3), ("apple", "banana"), (True, False))

# Tuple unpacking with nested tuples
nested_a, (nested_b, nested_c), nested_d = nested_tuple
print("Unpacked nested values:", nested_a, nested_b, nested_c, nested_d)  # Output: Unpacked nested values: (1, 2, 3) apple banana True

# Tuple unpacking with mixed data types
mixed_a, mixed_b, mixed_c, mixed_d = mixed_tuple
print("Unpacked mixed values:", mixed_a, mixed_b, mixed_c, mixed_d)  # Output: Unpacked mixed values: 1 apple 3.14 True

# Tuple unpacking with nested tuples and mixed data types
nested_mixed_a, (nested_mixed_b, nested_mixed_c), nested_mixed_d = nested_tuple
print("Unpacked nested mixed values:", nested_mixed_a, nested_mixed_b, nested_mixed_c, nested_mixed_d)  # Output: Unpacked nested mixed values: (1, 2, 3) apple banana True
