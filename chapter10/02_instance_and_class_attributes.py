class Employee:
    language = "Python" # This is a class attribute
    designation = "Data Scientist" # This is a class attribute
    location = "Greater Noida" # This is a class attribute
    
employee1 = Employee()
employee1.language = "Java" # This is an instance attribute
employee1.designation = "Data Engineer" # This is an instance attribute
employee1.location = "Noida" # This is an instance attribute
employee1.experience = 10 # This is an instance attribute
employee1.name = "Aishwarya Kumar Singh" # This is an instance attribute
employee1.emp_id = 20496888 # This is an instance attribute

print("------------------")
print("Employee1 Details:")
print("------------------") 
print("Name:", employee1.name)
print("Emp Id", employee1.emp_id)
print("Language:", employee1.language)
print("Experience:", employee1.experience)
print("Designation:", employee1.designation)
print("Location:", employee1.location)
print("\n")

# Note: Instance attributes take prefereance over class attributes during assignment and retrieval