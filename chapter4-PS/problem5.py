# WAP to count the number of elements in a tuple and display the count.
my_tuple = (1, 2, 3, 4, 5, 6, 7, 0,0, 4, 5, 6, 7, 8, 9, 8, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("\n")
print("Tuple element counting program:")
print("--------------------------------------------------")
# Count the number of elements in the tuple
count_of_elements = len(my_tuple)

# Display the count
print("Count of elements in the tuple:", count_of_elements)  # Output: 25

# Display the tuple for reference
print("Tuple:", my_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 0, 0, 4, 5, 6, 7, 8, 9, 8, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("\n")
print("Count of each element in the tuple in dictionary form with key-value pair of element and their count:")
print("-----------------------------------------------------------------------------------------------------")
# Count the occurrences of each element in the tuple
element_count = {}
for element in my_tuple:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

print("Element counts:", element_count)

# Display the count of each element
print("\n")
print("Element counts one by one:")
print("--------------------------")
print("Element counts:")
for element, count in element_count.items():
    print(f"Element {element}: {count} time(s)")



 