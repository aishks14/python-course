# WAP in python to add two entries in the set with string and integer of same identity(Example - '35' and 35

set_with_elements = set()  # Create an empty set
print("Enter two entries (one string and one integer with the same identity):")
string_entry = input("Enter a string (e.g., '35'): ")
integer_entry = int(input("Enter an integer (e.g., 35): "))

# Add both entries to the set
set_with_elements.add(string_entry)
set_with_elements.add(integer_entry)

# Display the set
print("Set with string and integer entries:", set_with_elements)
# Note: The set will only keep one of the entries if they are considered equal.
# In Python, '35' (string) and 35 (integer) are considered different types,
# so both will be stored in the set.


# If you want to check the identity, you can do so:
if string_entry == str(integer_entry):
    print("The string and integer entries have the same identity.")
else:
    print("The string and integer entries do not have the same identity.")

# Display the type of each entry
print("Type of string entry:", type(string_entry))
print("Type of integer entry:", type(integer_entry))

# Display the type of the set
print("Type of the set:", type(set_with_elements))

# Display the contents of the set
print("Contents of the set:", set_with_elements)
