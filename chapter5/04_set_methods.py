# Set methods
# Adding elements to a set
my_set = {1, 2, 3, 4, 5}

# Add a single element to the set
my_set.add(6)
print("Set after adding 6:", my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Add multiple elements to the set
my_set.update([7, 8, 9])   
print("Set after adding 7, 8, 9:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Adding elements from another set
another_set = {10, 11}
my_set.update(another_set)
print("Set after adding elements from another set:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Adding elements from a tuple
my_set.update((12, 13))
print("Set after adding elements from a tuple:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# Adding elements from a list
my_set.update([14, 15])
print("Set after adding elements from a list:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}  

# Adding elements from a string
my_set.update("abc")
print("Set after adding elements from a string:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'a', 'b', 'c'}

# Removing elements from a set
my_set.remove(3)  # Removes the element 3 from the set
print("Set after removing 3:", my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'a', 'b', 'c'}
# Removing an element that may not exist
# my_set.remove(20)  # This will raise a KeyError if 20 is not in the set

# Using discard to remove an element that may not exist
my_set.discard(20)  # This will not raise an error if 20 is not in the set
print("Set after discarding 20 (not present):", my_set)  # Output: {1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'a', 'b', 'c'}

# Popping an element from a set
popped_element = my_set.pop()  # Removes and returns an arbitrary element from the set
print("Popped element:", popped_element)  # Output: An arbitrary element from the set
print("Set after popping an element:", my_set)  # Output: Set without the popped element

# Clearing a set
my_set.clear()  # Removes all elements from the set
print("Set after clearing:", my_set)  # Output: set() (an empty set)

# Set operations
# Union of two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)  # Output: {3}

# Difference of two sets
# set_a - set_b (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)  # Output: {1, 2}

# Symmetric difference of two sets
# Elements in either set_a or set_b but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Subset and superset checks
# Check if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print("Is set_a a subset of set_b?", is_subset)  # Output: False

# Check if set_b is a superset of set_a
is_superset = set_b.issuperset(set_a)
print("Is set_b a superset of set_a?", is_superset)  # Output: False

# Disjoint sets check
# Check if set_a and set_b are disjoint (no common elements)
is_disjoint = set_a.isdisjoint(set_b)
print("Are set_a and set_b disjoint?", is_disjoint)  # Output: False

# Set comprehension
# Creating a set of squares of numbers from 1 to 5
squares_set = {x**2 for x in range(1, 6)}
print("Set of squares from 1 to 5:", squares_set)  # Output: {1, 4, 9, 16, 25}

# Set of strings
string_set = {"apple", "banana", "cherry"}

# Accessing elements in a string set
print("First string in string set:", next(iter(string_set)))  # Output: An arbitrary string from the set

# Modifying elements in a string set is not allowed, but you can create a new set with modified values  
new_string_set = {"orange", "banana", "cherry"}  # Create a new set with modified values
print("New string set with modified first element:", new_string_set)  # Output: {'orange', 'banana', 'cherry'}

# Set of mixed data types
mixed_set = {5, "apple", 3.14, True}

# Accessing elements in a mixed set
print("First element in mixed set:", next(iter(mixed_set)))  # Output: An arbitrary element from the set

# Modifying elements in a mixed set is not allowed, but you can create a new set with modified values
new_mixed_set = {1, "banana", 3.14, False}  # Create a new set with modified values
print("New mixed set with modified first element:", new_mixed_set)  # Output: {1, 'banana', 3.14, False}

# Set of sets (nested sets)
# Note: Sets cannot contain other sets directly, but you can use frozensets (immutable sets) to achieve this.
# Regular sets cannot contain other sets directly because sets are mutable
nested_set = {frozenset({1, 2, 3}), frozenset({"apple", "banana"}), frozenset({True, False})}

# Accessing elements in a nested set
print("First element of first set in nested set:", next(iter(nested_set)))  # Output: An arbitrary frozenset from the nested set

# Modifying elements in a nested set is not allowed, but you can create a new nested set
new_nested_set = {frozenset({1, 20, 3}), frozenset({"apple", "banana"}), frozenset({True, False})}  # Create a new nested set with modified values
print("New nested set with modified first element of first set:", new_nested_set)  # Output: {frozenset({1, 20, 3}), frozenset({'apple', 'banana'}), frozenset({True, False})}

