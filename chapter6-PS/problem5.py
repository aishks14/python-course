# WAP in python to find out whether a given name is present in a list or not. If present, display the index of the name in the list; otherwise, display an error message.
names = ["Aishwarya", "Himanshu", "Ajay", "David", "Eve", "Frank", "Grace", "Kajal", "Megha", "Prashant", "Ravi", "Sita", "Tina", "Vikram", "Zara"]
name_to_find = input("Enter a name to search in the list: ")

if name_to_find in names:
    index = names.index(name_to_find)
    print(f"The name '{name_to_find}' is present in the list at index {index}.")
else:
    print(f"Error: The name '{name_to_find}' is not present in the list.")