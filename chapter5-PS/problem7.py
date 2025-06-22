# WAP to check the entries in the dictionaries if keys are same and values are different.

dict_data = {}
for i in range(5):
    name = input(f"\nEnter {i + 1} friend's name: ")
    language = input(f"Enter {name}'s favourite language: ")
    dict_data[name] = language


print("\nDictionary data after loop: ", dict_data)
# Display the final dictionary
print("\nFinal Dictionary data: ", dict_data)

#Note: The code above will update the dictionary with last entered key which was already present in the dictionary. It will consider the last entry of same element key.