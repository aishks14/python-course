# Recursion in python
# Recursion is when a function calls itself.
# It’s used to solve problems that can be broken down into smaller, similar subproblems.
# Every recursive function must have:
# A base case – the condition under which the function stops calling itself.
# A recursive case – where the function calls itself with a smaller input.

# ----------------------------------------------------------------------------------------
# Structure of a Recursive Function
# def recursive_function(parameters):
#    if base_case_condition:
#        return base_case_result
#    else:
#        return recursive_function(smaller_problem)

# ----------------------------------------------------------------------------------------

# Example 1 of recursion - Factorial of a number
print("\nFunction in python to get the factorial of a number:")
print("----------------------------------------------------")
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

input_factorial_number = int(input("Enter a number for which factorial would be calculated: "))
print(f"Factorial of number {input_factorial_number}: {factorial(input_factorial_number)}")

# Example 2 of recursion - Recursive sum of digits
print("\nFunction in python for recursive sum of digits:")
print("-----------------------------------------------")
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

input_num = int(input("Enter a number whose digit sum would be calculated recursively: "))
print(f"Sum of digits of number {input_num}: {sum_of_digits(input_num)}")

# IMPORTANT
# Recursive functions can be elegant but inefficient if not optimized.
# Too many recursive calls can lead to a RecursionError