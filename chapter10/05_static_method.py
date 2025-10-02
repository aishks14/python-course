# Self Method
# Static method is a method that belongs to the class rather than the instance of the class.
# It does not require a self parameter.
print("-----------------------------------")
print("Static Method")
print("-----------------------------------")
# Example 1: Creating a class and using self parameter        
class Employee:
    language = "Python"
    designation = "Data Scientist"
    location = "Greater Noida"
    
    @staticmethod
    def greet():
        print("Hello, welcome to my python learning journey!\n") # Static method, no self parameter
    
    def inner_details(self):
        print("Inner Details:")
        print("--------------")
        print("Language:", self.language)
        print("Designation:", self.designation)
        print("Location:", self.location)
        
employee1 = Employee()
employee1.language = "JavaScript"
employee1.greet()
employee1.inner_details() #Employee.inner_details(employee1) - This is similar syntax
print("\n")