# Dictionary in python
# A dictionary is a collection of key-value pairs.
# Dictionaries are mutable, meaning you can change their content.
# Dictionaries are defined using curly braces {}.

# Example of a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionary
print("\n")
print("Dictionary in Python:")
print("---------------------")
print("Created dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(my_dict))  # Output: <class 'dict'>

# Accessing values in a dictionary
print("\n")
print("Accessing values in a dictionary:")
print("---------------------------------")
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 30
print("City:", my_dict["city"])  # Output: New York

# Modifying values in a dictionary
print("\n")
print("Modifying values in a dictionary:")
print("---------------------------------")
my_dict["age"] = 31
print("Modified age:", my_dict["age"])  # Output: 31

# Adding a new key-value pair to the dictionary
print("\n")
print("Adding a new key-value pair to the dictionary:")
print("----------------------------------------------")
my_dict["country"] = "USA"
print("Added country:", my_dict["country"])  # Output: USA

# Removing a key-value pair from the dictionary
print("\n")
print("Removing a key-value pair from the dictionary:")
print("----------------------------------------------")
del my_dict["city"]
print("Removed city:", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Checking if a key exists in the dictionary
print("\n")
print("Checking if a key exists in the dictionary:")
print("-------------------------------------------")
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary

# Iterating over keys and values in a dictionary
print("\n")
print("Iterating over keys and values in a dictionary:")
print("-----------------------------------------------")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 31
# country: USA