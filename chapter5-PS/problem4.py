#WAP in python to check the length of a set and display the elements in it.
# WAP in python to check the length of a set and display the elements in it.
my_set = {1, '1', 2, '2', 3, '3', 4, '4', 5, '5', 6, '6', 7, '7'}
print("\n")
print("Set length and elements display program:")
print("--------------------------------------------------")
# Count the number of elements in the set
count_of_elements = len(my_set)

# Display the count
print("Count of elements in the set:", count_of_elements)  # Output: 10

# Display the set for reference
print("Set elements:", my_set)  # Output: {1, '1', 2, '2', 3, '3', 4, '4', 5, '5', 6, '6', 7, '7'}
print("\n")
print("Set elements one by one:")
print("--------------------------")

# Display the elements in the set one by one
for element in my_set:
    print(f"Element: {element}")