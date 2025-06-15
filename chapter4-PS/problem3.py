# WAP in python to check that tuple type cannot be changed after creation.
test_tuple = (1, 2, 3, 4, 5)
# Attempting to modify an element in a tuple will raise a TypeError
print("Trying to modify the tuble and handle the exception:")
print("----------------------------------------------------")
try:
    test_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print ("Caught an exception while trying to modify a tuple:", e)

# However, you can create a new tuple with modified values
print("\n")
print("Trying to modify the tuple by creating a new tuple with modified values:")
print("------------------------------------------------------------------------")
new_test_tuple = (10,) + test_tuple[1:]  # Create a new tuple with the first element changed
print("Original tuple:", test_tuple)  # Output: (1, 2, 3, 4, 5)
print("New tuple with modified first element:", new_test_tuple)  # Output: (10, 2, 3, 4, 5)
# This demonstrates that tuples are immutable and cannot be changed after creation.