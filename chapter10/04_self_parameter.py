# Self parameter
# Self parameter is a reference to the current instance of the class.
# It is used to access variables that belongs to the class.
print("-----------------------------------")
print("Self Parameter")
print("-----------------------------------")
# Example 1: Creating a class and using self parameter        
class Employee:
    language = "Python"
    designation = "Data Scientist"
    location = "Greater Noida"
    
    def inner_details(self):
        print("Inner Details:")
        print("--------------")
        print("Language:", self.language)
        print("Designation:", self.designation)
        print("Location:", self.location)
        
employee1 = Employee()
employee1.language = "JavaScript"
employee1.inner_details() #Employee.inner_details(employee1) - This is similar syntax
print("\n")