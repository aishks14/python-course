# Dictionary methods
# Dictionary methods in Python

# Dictionary methods in Python
# Dictionaries have several built-in methods that allow you to manipulate and access data efficiently.
# Here are some common dictionary methods:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing keys and values
print("\nAccessing keys and values:")
print("----------------------------")
# Get all keys in the dictionary
keys = my_dict.keys()
print("Keys:", keys)  # Output: dict_keys(['name', 'age', 'city'])

# Get all values in the dictionary
values = my_dict.values()
print("Values:", values)  # Output: dict_values(['Alice', 30, 'New York'])

# Get all key-value pairs in the dictionary
items = my_dict.items()
print("Items:", items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Adding a new key-value pair
print("\nAdding a new key-value pair:")
print("------------------------------")
my_dict["country"] = "USA"
print("\nUpdated dictionary first time:", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'} 

# Removing a key-value pair
print("\nRemoving a key-value pair:")
print("----------------------------")
del my_dict["city"]
print("\nDictionary after removing 'city':", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'country': 'USA'}

# Using pop() to remove a key-value pair and return its value
popped_value = my_dict.pop("age")
print("\nPopped value:", popped_value)  # Output: 30
print("\nDictionary after popping 'age':", my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

# Using popitem() to remove and return the last inserted key-value pair
popped_item = my_dict.popitem()
print("\nPopped item:", popped_item)  # Output: ('country', 'USA')
print("\nDictionary after popping the last item:", my_dict)  # Output: {'name': 'Alice'}

# Clearing the dictionary
print("\nClearing the dictionary:")
print("--------------------------")
my_dict.clear()
print("Dictionary after clearing:", my_dict)  # Output: {}

# Re-creating the dictionary for further operations
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New Delhi"
}   

# Copying the dictionary
print("\nCopying the dictionary:")
print("-------------------------")
my_dict_copy = my_dict.copy()
print("\nOriginal dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New Delhi'}
print("\nCopied dictionary:", my_dict_copy)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New Delhi'}

# Updating the dictionary with another dictionary
print("\nUpdating the dictionary with another dictionary:")
print("--------------------------------------------------")
update_dict = {"country": "India", "age": 31}
print("\nupdate_dict:", update_dict)
my_dict.update(update_dict)
print("\nUpdated dictionary second time:", my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New Delhi', 'country': 'India'}

# Checking if a key exists in the dictionary
print("\nChecking if a key exists in the dictionary:")
print("---------------------------------------------")
if "name" in my_dict:
    print("\nKey 'name' exists in the dictionary")  # Output: Key 'name' exists in the dictionary 
else:
    print("\nKey 'name' does not exist in the dictionary")

# Checking if a value exists in the dictionary
print("\nChecking if a value exists in the dictionary:")
print("-----------------------------------------------")
if "Alice" in my_dict.values():
    print("\nValue 'Alice' exists in the dictionary")  # Output: Value 'Alice' exists in the dictionary   
else:
    print("\nValue 'Alice' does not exist in the dictionary")

# Getting the length of the dictionary
print("\nGetting the length of the dictionary:")
print("---------------------------------------")
length = len(my_dict)
print("\nLength of the dictionary:", length)  # Output: Length of the dictionary: 4

# Iterating over keys, values, and items
print("\nIterating over keys, values, and items:")
print("-----------------------------------------")
for key in my_dict.keys():
    print("Key:", key)  # Output: Key: name, Key: age, Key: city, Key: country
for value in my_dict.values():
    print("Value in dictionary:", value)  # Output: Value: Alice, Value: 31, Value: New Delhi, Value: India
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Output: Key: name, Value: Alice
# Key: age, Value: 31
# Key: city, Value: New Delhi
# Key: country, Value: India

# Dictionary comprehension
print("\nDictionary comprehension:")
print("---------------------------")
# Creating a new dictionary with squares of numbers from 1 to 5
squares_dict = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  

# Creating a dictionary with mixed data types
mixed_dict = {
    "integer": 42,
    "string": "Hello",
    "float": 3.14,
    "boolean": True
}
print("\nMixed data types dictionary:")
print("\nMixed dictionary:", mixed_dict)  # Output: {'integer': 42, 'string': 'Hello', 'float': 3.14, 'boolean': True}

# Accessing elements in a mixed data types dictionary
print("\nAccessing elements in a mixed data types dictionary:")
print("\nInteger value in mixed data types dictionary:", mixed_dict["integer"])  # Output: 42
print("\nString value in mixed data types dictionary:", mixed_dict["string"])    # Output: Hello
print("\nFloat value in mixed data types dictionary:", mixed_dict["float"])      # Output: 3.14
print("\nBoolean value in mixed data types dictionary:", mixed_dict["boolean"])  # Output: True

# Modifying elements in a mixed data types dictionary
mixed_dict["string"] = "World"
print("Modified mixed dictionary:", mixed_dict)  # Output: {'integer': 42, 'string': 'World', 'float': 3.14, 'boolean': True}

# Nested dictionaries
print("\nNested dictionaries:")
print("----------------------")
nested_dict = {
    "person": {
        "name": "Alice",
        "age": 30
    },
    "address": {
        "city": "New York",
        "country": "USA"
    }
}
print("\nNested dictionary:", nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 30}, 'address': {'city': 'New York', 'country': 'USA'}}

# Accessing elements in a nested dictionary
print("\nAccessing elements in a nested dictionary:")
print("--------------------------------------------")
print("\nPerson's name:", nested_dict["person"]["name"])  # Output: Alice
print("\nPerson's age:", nested_dict["person"]["age"])    # Output: 30
print("\nAddress city:", nested_dict["address"]["city"])  # Output: New York
print("\nAddress country:", nested_dict["address"]["country"])  # Output: USA

# Modifying elements in a nested dictionary
nested_dict["person"]["age"] = 31
print("\nModified nested dictionary:", nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 31}, 'address': {'city': 'New York', 'country': 'USA'}}

# Adding a new key-value pair in a nested dictionary
nested_dict["address"]["zip"] = "10001"
print("\nNested dictionary after adding zip code:", nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 31}, 'address': {'city': 'New York', 'country': 'USA', 'zip': '10001'}}

# Removing a key-value pair from a nested dictionary
del nested_dict["address"]["country"]
print("\nNested dictionary after removing country:", nested_dict)  # Output: {'person': {'name': 'Alice', 'age': 31}, 'address': {'city': 'New York', 'zip': '10001'}}

# Checking if a key exists in a nested dictionary
print("\nChecking if a key exists in a nested dictionary:")
print("--------------------------------------------------")
if "city" in nested_dict["address"]:
    print("\nKey 'city' exists in the address dictionary")  # Output: Key 'city' exists in the address dictionary 
else:
    print("\nKey 'city' does not exist in the address dictionary")

# Checking if a value exists in a nested dictionary
print("\nChecking if a value exists in a nested dictionary:")
print("----------------------------------------------------")
if "Alice" in nested_dict["person"].values():
    print("\nValue 'Alice' exists in the person dictionary")  # Output: Value 'Alice' exists in the person dictionary 
else:
    print("\nValue 'Alice' does not exist in the person dictionary")

# Getting the length of a nested dictionary
print("\nGetting the length of a nested dictionary:")
print("--------------------------------------------")
length_nested = len(nested_dict)
print("\nLength of the nested dictionary:", length_nested)  # Output: Length of the nested dictionary: 2

# Iterating over keys, values, and items in a nested dictionary
print("\nIterating over keys, values, and items in a nested dictionary:")
print("----------------------------------------------------------------")
for key in nested_dict.keys():
    print("\nKey:", key)  # Output: Key: person, Key: address
for value in nested_dict.values():
    print("\nValue:", value)  # Output: Value: {'name': 'Alice', 'age': 31}, Value: {'city': 'New York', 'zip': '10001'}
for key, value in nested_dict.items():
    print(f"\nKey: {key}, Value: {value}")

# Output: Key: person, Value: {'name': 'Alice', 'age': 31}
# Key: address, Value: {'city': 'New York', 'zip': '10001'}

# Dictionary comprehension with nested dictionaries
print("\nDictionary comprehension with nested dictionaries:")
print("----------------------------------------------------")

# Creating a nested dictionary with squares of numbers from 1 to 3
nested_squares_dict = {x: {"square": x**2, "cube": x**3} for x in range(1, 4)}
print("\nNested squares dictionary:", nested_squares_dict)
# Output: {1: {'square': 1, 'cube': 1}, 2: {'square': 4, 'cube': 8}, 3: {'square': 9, 'cube': 27}}

# Creating a dictionary with mixed data types
mixed_nested_dict = {
    "integer": 42,
    "string": "Hello",
    "float": 3.14,
    "boolean": True,
    "nested": {
        "list": [1, 2, 3],
        "tuple": (4, 5, 6)
    }
}
print("\nMixed nested data types dictionary:")
print("-------------------------------------")
print("\nMixed nested dictionary:", mixed_nested_dict)
# Output: {'integer': 42, 'string': 'Hello', 'float': 3.14, 'boolean': True, 'nested': {'list': [1, 2, 3], 'tuple': (4, 5, 6)}}

# Accessing elements in a mixed nested data types dictionary
print("\nAccessing elements in a mixed nested data types dictionary:")
print("-------------------------------------------------------------")
print("\nInteger value:", mixed_nested_dict["integer"])  # Output: 42
print("\nString value:", mixed_nested_dict["string"])    # Output: Hello
print("\nFloat value:", mixed_nested_dict["float"])      # Output: 3.14
print("\nBoolean value:", mixed_nested_dict["boolean"])  # Output: True
print("\nNested list:", mixed_nested_dict["nested"]["list"])  # Output: [1, 2, 3]
print("\nNested tuple:", mixed_nested_dict["nested"]["tuple"])  # Output: (4, 5, 6)

# Modifying elements in a mixed nested data types dictionary
mixed_nested_dict["string"] = "World"
print("\nModified mixed nested dictionary:", mixed_nested_dict)
# Output: {'integer': 42, 'string': 'World', 'float': 3.14, 'boolean': True, 'nested': {'list': [1, 2, 3], 'tuple': (4, 5, 6)}}

# Modifying nested elements
mixed_nested_dict["nested"]["list"].append(4)
print("\nModified nested list:", mixed_nested_dict["nested"]["list"])  # Output: [1, 2, 3, 4]
mixed_nested_dict["nested"]["tuple"] = (4, 5, 6, 7)
print("\nModified nested tuple:", mixed_nested_dict["nested"]["tuple"])  # Output: (4, 5, 6, 7)

# Adding a new key-value pair in a mixed nested data types dictionary
mixed_nested_dict["nested"]["new_key"] = "New Value"
print("\nMixed nested dictionary after adding new key:", mixed_nested_dict)
# Output: {'integer': 42, 'string': 'World', 'float': 3.14, 'boolean': True, 'nested': {'list': [1, 2, 3, 4], 'tuple': (4, 5, 6, 7), 'new_key': 'New Value'}}

# Removing a key-value pair from a mixed nested data types dictionary
del mixed_nested_dict["boolean"]
print("\nMixed nested dictionary after removing boolean:", mixed_nested_dict)
# Output: {'integer': 42, 'string': 'World', 'float': 3.14, 'nested': {'list': [1, 2, 3, 4], 'tuple': (4, 5, 6, 7), 'new_key': 'New Value'}}

# Checking if a key exists in a mixed nested data types dictionary
print("\nChecking if a key exists in a mixed nested data types dictionary:")
print("-------------------------------------------------------------------")
if "nested" in mixed_nested_dict:
    print("\nKey 'nested' exists in the mixed nested dictionary")  # Output: Key 'nested' exists in the mixed nested dictionary
else:
    print("\nKey 'nested' does not exist in the mixed nested dictionary")

# Checking if a value exists in a mixed nested data types dictionary
print("\nChecking if a value exists in a mixed nested data types dictionary:")
print("---------------------------------------------------------------------")
if "World" in mixed_nested_dict.values():
    print("\nValue 'World' exists in the mixed nested dictionary")  # Output: Value 'World' exists in the mixed nested dictionary
else:
    print("\nValue 'World' does not exist in the mixed nested dictionary")

# Getting the length of a mixed nested data types dictionary
print("\nGetting the length of a mixed nested data types dictionary:")
print("-------------------------------------------------------------")
length_mixed_nested = len(mixed_nested_dict)
print("\nLength of the mixed nested dictionary:", length_mixed_nested)  # Output: Length of the mixed nested dictionary: 4

# Iterating over keys, values, and items in a mixed nested data types dictionary
print("\nIterating over keys, values, and items in a mixed nested data types dictionary:")
print("---------------------------------------------------------------------------------")
for key in mixed_nested_dict.keys():
    print("\nKey:", key)  # Output: Key: integer, Key: string, Key: float, Key: nested
for value in mixed_nested_dict.values():
    print("\nValue:", value)  # Output: Value: 42, Value: World, Value: 3.14, Value: {'list': [1, 2, 3, 4], 'tuple': (4, 5, 6, 7), 'new_key': 'New Value'}
for key, value in mixed_nested_dict.items():
    print(f"\nKey: {key}, Value: {value}")
# Output: Key: integer, Value: 42
# Key: string, Value: World
# Key: float, Value: 3.14
# Key: nested, Value: {'list': [1, 2, 3, 4], 'tuple': (4, 5, 6, 7), 'new_key': 'New Value'}

# Dictionary comprehension with mixed nested dictionaries
print("\nDictionary comprehension with mixed nested dictionaries:")
print("----------------------------------------------------------")
# Creating a mixed nested dictionary with squares and cubes of numbers from 1 to 3
mixed_nested_squares_dict = {x: {"square": x**2, "cube": x**3} for x in range(1, 4)}    
print("\nMixed nested squares dictionary:", mixed_nested_squares_dict)
# Output: {1: {'square': 1, 'cube': 1}, 2: {'square': 4, 'cube': 8}, 3: {'square': 9, 'cube': 27}}