# WAP in python to detect double space in a string without using functions or methods.

# Get user input for the string
input_string = input("Enter a string: ")
print("\nOriginal String:")
print("-----------------")  
print(input_string)

print("\nFinding double space:")
print("---------------------")
print("Double space found at index(if any):", input_string.find("  "))
# -1 indicates no double space found