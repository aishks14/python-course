# WAP in python to create a class named `Programmer`for storing few programmers details working in an organization.
class Programmer:
    company = "XYZ Pvt Ltd"
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.language}")
print("-----------------------------------")
print("Programmer - 1")
print("-----------------------------------")       
Programmer1 = Programmer("Alice", 30, "Python")
Programmer1.display_details()  
print("\n")

print("-----------------------------------")
print("Programmer - 2")
print("-----------------------------------")
Programmer2 = Programmer("Bob", 25, "Java")
Programmer2.display_details()
print("\n") 