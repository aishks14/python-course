#integer variables
a = 5 
b = 10

# String variable
name = "Aish" 

# Float variable
d = 8.85

# Boolean variable
e = True

# NoneType variable
f = None

#=====================================

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3)

# Dictionary
my_dict = {"name": "Aish", "age": 25}


# Function to add two numbers
def add_numbers(x, y):
    """Returns the sum of two numbers."""
    return x + y   

# Function to multiply two numbers 
def multiply_numbers(x, y):
    """Returns the product of two numbers."""
    return x * y

# Main function to demonstrate variable and function usage
def main():
    c = a + b
    print("Name:", name)
    print("Sum of a and b:", c)
    print("Sum of 3 and 4:", add_numbers(3, 4))
    print("Product of 2 and 5:", multiply_numbers(2, 5))

# Call the main function
main()