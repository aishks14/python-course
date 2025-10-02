# WAP in python to chekc the type of created data type
my_set = {1, 2, 3, 4, 5}
print("\n")
print("Checking the type of created data type:")
print("---------------------------------------")
# Check the type of the set
set_type = type(my_set)
# Display the type
print("\nType of the created data type:", set_type)  # Output: <class 'set'>
# Display the set for reference
print("\nSet elements:", my_set)  # Output: {1, 2, 3, 4, 5}

# Empty data type
empty_set = {}
# Display the type of data type
print("\nType of empty data type:", type(empty_set))  # Output: <class 'dict'>
# The empty_set is not created using {} as it creates an empty dictionary, not a set.

# To create an empty set, use the set() constructor
empty_set = set()
# Display the type of empty set
print("\nType of empty set:", type(empty_set))  # Output: <class 'set'>