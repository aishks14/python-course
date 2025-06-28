# WAP in python to get all the persons' names that are stored in a list 'people_list' and start with letter 'K'
people_list = ["Aishwarya", "Kajal", "Megha", " Prashant", "Kate", "Katherine", "Kasper", "Ajay", "Bhupendra", "Himanshu", "Gautam", "Anjali", "Shivani", "Mathavan", "Amar", "Korea", "Kashish"]
names_starting_with_K = [name for name in people_list if name.startswith('K')]
print("\nPerson with starting letter of their name as 'K':")
print("-------------------------------------------------")
print(names_starting_with_K)

# Alternative way with different printing for the same problem
print("\nPerson with starting letter of their name as 'K' with prefix of greetings :")
print("---------------------------------------------------------------------------")
for name in people_list:
    if(name.startswith("A")):
        print(f"Hello {name}! You are selected")