# Add a static method in code of problem2.py to display the total number of employees created.
class Calculator:
    employee_count = 0  # Class variable to keep track of the number of employees

    def __init__(self, number):
        self.number = number
        Calculator.employee_count += 1  # Increment the count when a new instance is created

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5  # Corrected the square root calculation

    @staticmethod # Static method decorator to tell program compiler that `self` will not be used in the code section below
    def display_employee_count():
        print(f"Total number of employees created: {Calculator.employee_count}")
        return Calculator.employee_count
        
num = float(input("Enter a number: "))    
calc = Calculator(num)
print("---------------------------------------")
print("Calculator - Instance 1 - Static Method")
print("---------------------------------------")
print(f"Number: {calc.number}")
print(f"Square: {calc.square()}")
print(f"Cube: {calc.cube()}")
print(f"Square Root: {calc.square_root()}")
print(f"Employee Count: {calc.display_employee_count()}")
print("\n")

calc = Calculator(num)
print("---------------------------------------")
print("Calculator - Instance 2 - Static Method")
print("---------------------------------------")
print(f"Number: {calc.number}")
print(f"Square: {calc.square()}")
print(f"Cube: {calc.cube()}")
print(f"Square Root: {calc.square_root()}")
print(f"Employee Count: {calc.display_employee_count()}")

# Note: Observe that static method is refered without the usage of self