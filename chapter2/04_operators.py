#Operators
# ---------------------------------------------------------------------------
# Arithmetic Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of various arithmetic operators in Python.
a = 10
b = 5   
## Addition
addition = a + b

# Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b  

# Division
division = a / b    

# Modulus
modulus = a % b 

# Exponentiation
exponentiation = a ** b

# Floor Division
floor_division = a // b     

# Print results
print("\nArithmetic Operators:")
print("----------------------------------")
print("Addition:", addition)    
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)


# ---------------------------------------------------------------------------
# Comparison Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of various comparison operators in Python.
# Comparison operators are used to compare two values and return a boolean result.  
x = 10
y = 5   

# Equal to
equal_to = (x == y) 

# Not equal to
not_equal_to = (x != y)

# Greater than
greater_than = (x > y)

# Less than
less_than = (x < y)

# Greater than or equal to
greater_than_or_equal_to = (x >= y)

# Less than or equal to
less_than_or_equal_to = (x <= y)

# Print results
print("\nComparison Operators:")
print("----------------------------------")
print("Equal to:", equal_to)
print("Not equal to:", not_equal_to)
print("Greater than:", greater_than)
print("Less than:", less_than)
print("Greater than or equal to:", greater_than_or_equal_to)
print("Less than or equal to:", less_than_or_equal_to)


# ---------------------------------------------------------------------------
# Logical Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of various logical operators in Python.
# Logical operators are used to combine conditional statements.
a = True
b = False   
# Logical AND
logical_and = a and b

# Logical OR
logical_or = a or b

# Logical NOT
logical_not = not a

# Logical XOR (exclusive OR) is not a built-in operator in Python, but can be simulated
def logical_xor(x, y):
    """Returns True if exactly one of x or y is True."""
    return (x and not y) or (not x and y)
logical_xor_result = logical_xor(a, b)

# Print results
print("\nLogical Operators:")
print("----------------------------------") 
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)
# Logical XOR (simulated): This is not a built-in operator in Python, but can be simulated
print("Logical XOR (simulated):", logical_xor_result)


# ---------------------------------------------------------------------------
# Assignment Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of various assignment operators in Python.
# Assignment operators are used to assign values to variables.

# Basic assignment
x = 10

# Add and assign
x += 5  # Equivalent to x = x + 5

# Subtract and assign
x -= 3  # Equivalent to x = x - 3

# Multiply and assign
x *= 2  # Equivalent to x = x * 2

# Divide and assign
x /= 4  # Equivalent to x = x / 4

# Modulus and assign
x %= 3  # Equivalent to x = x % 3

# Exponentiation and assign
x **= 2  # Equivalent to x = x ** 2

# Floor division and assign
x //= 2  # Equivalent to x = x // 2

# Print result
print("\nAssignment Operators:")
print("----------------------------------")
print("Final value of x:", x)

# ---------------------------------------------------------------------------
# Bitwise Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of various bitwise operators in Python.
# Bitwise operators are used to perform operations on binary representations of integers. 

# Bitwise AND
a = 10  # Binary: 1010
b = 4   # Binary: 0100
bitwise_and = a & b  # Result: 0 (Binary: 0000)

# Bitwise OR
bitwise_or = a | b  # Result: 14 (Binary: 1110)

# Bitwise XOR
bitwise_xor = a ^ b  # Result: 10 (Binary: 1010)

# Bitwise NOT
bitwise_not = ~a  # Result: -11 (Binary: ...11110101, two's complement representation)

# Left Shift
left_shift = a << 2  # Result: 40 (Binary: 101000)

# Right Shift
right_shift = a >> 2  # Result: 2 (Binary: 0010)

# Bitwise NOT is a unary operator, so it only requires one operand.
# Note: The results of bitwise operations are in decimal, but they can be represented in binary as well.
# Bitwise NOT is not a built-in operator in Python, but can be simulated
# Note: Bitwise operations are performed on the binary representations of integers.
# Bitwise NOT is a unary operator, so it only requires one operand.
# Note: The results of bitwise operations are in decimal, but they can be represented in binary as well.

# Print results
print("\nBitwise Operators:")
print("----------------------------------")
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT:", bitwise_not)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)


# ---------------------------------------------------------------------------
# Identity Operators
# ---------------------------------------------------------------------------
# This script demonstrates the use of identity operators in Python.
# Identity operators are used to compare the memory locations of two objects.

a = [1, 2, 3]
b = a            # b references the same object as a
c = [1, 2, 3]    # c is a different object with the same contents as a

# 'is' operator: True if both variables point to the same object (same memory location)
is_operator = (a is b)  # True, because b and a refer to the same object in memory

# 'is not' operator: True if variables point to different objects (different memory locations)
is_not_operator = (a is not c)  # True, because a and c are different objects in memory

print("\nIdentity Operators:")
print("----------------------------------")
print("a is b:", is_operator)
print("a is not c:", is_not_operator)
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))

# ---------------------------------------------------------------------------
# Membership Operators      
# ---------------------------------------------------------------------------
# This script demonstrates the use of membership operators in Python.
# Membership operators are used to test if a value is a member of a sequence (like a list, tuple, or string).
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_string = "Hello, World!"
# 'in' operator: True if the value is found in the sequence
in_operator_list = 3 in my_list  # True, because 3 is in my_list
in_operator_tuple = 4 in my_tuple  # False, because 4 is not in my_tuple
in_operator_string = "Hello" in my_string  # True, because "Hello" is in my_string
# 'not in' operator: True if the value is not found in the sequence
not_in_operator_list = 6 not in my_list  # True, because 6 is not in my_list
not_in_operator_tuple = 0 not in my_tuple  # True, because 0 is not in my_tuple
not_in_operator_string = "World" not in my_string  # False, because "World" is in my_string
print("\nMembership Operators:")
print("----------------------------------")
print("3 in my_list:", in_operator_list)
print("4 in my_tuple:", in_operator_tuple)
print('"Hello" in my_string:', in_operator_string)
print("6 not in my_list:", not_in_operator_list)
print("0 not in my_tuple:", not_in_operator_tuple)
print('"World" not in my_string:', not_in_operator_string)
# End of the script
# Note: The output of the script will vary based on the values assigned to the variables.
# The script demonstrates the use of various operators in Python, including arithmetic, comparison, logical, assignment, bitwise, identity, and membership operators.
# The script also includes examples of how to use these operators with different data types.