# WAP in python to create a class `Calculator` which is capable of calculating square, cube, and, square root of a number
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 1/2   

num = float(input("Enter a number: "))    
calc = Calculator(num)
print("-----------------------------------")
print("Calculator")
print("-----------------------------------")
print(f"Number: {calc.number}")
print(f"Square: {calc.square()}")
print(f"Cube: {calc.cube()}")
print(f"Square Root: {calc.square_root()}")