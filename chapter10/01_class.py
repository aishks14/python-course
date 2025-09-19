# Classes and Objects
# A class is a blueprint for creating objects. An object is an instance of a class.

# Example 1: Creating a class
print("-----------------------------------")
print("Classes and Objects - 1")
print("-----------------------------------")
class Employee:
    language = "Python"
    experience = 10
    designation = "Data Scientist"
    location = "Greater Noida"

# Employee 1 using the class
employee1 = Employee()
employee1.name = "Aishwarya Kumar Singh"
employee1.emp_id = 20496824
employee1.salary = 2500000
print("Employee1 Details:")
print("------------------")
print("Name:", employee1.name)
print("Emp ID:", employee1.emp_id)
print("Language:", employee1.language)
print("Experience:", employee1.experience)
print("Designation:", employee1.designation)
print("Salary(appx):", employee1.salary)
print("Location:", employee1.location)
print("\n")

# Employee 2 using the class
employee2 = Employee()
employee2.name = "Prashant Singh"
employee2.emp_id = 20496892
employee2.salary = 2200000
print("Employee2 Details:")
print("------------------")
print("Name:", employee2.name)
print("Emp Id:", employee2.emp_id)
print("Language:", employee2.language)
print("Experience:", employee2.experience)
print("Designation:", employee2.designation)
print("Salary(appx):", employee2.salary)
print("Location:", employee2.location)
print("\n")

# Example 2: Creating a class and using it through methods
print("-----------------------------------")
print("Classes and Objects - 2")
print("-----------------------------------")
# The __init__ method(or constructor) is a special method that is called when an object is created from a class.
# It initializes the object's attributes.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")
        
my_dog = Dog("Joy", 3)
my_dog.bark()
print("\n")
