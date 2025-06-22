# WAP in python to create an empty dictionary. Allow 5 friends to enter their favourite language
# as value and use key as their names. Assume that names are unique.

dict_data ={}
name = input("\nEnter friend's name: ")
language = input("\nEnter lanuage name:")
dict_data.update({name: language})


name = input("\nEnter friend's name: ")
language = input("\nEnter lanuage name:")
dict_data.update({name: language})
 
name = input("\nEnter friend's name: ")
language = input("\nEnter lanuage name:")
dict_data.update({name: language})


name = input("\nEnter friend's name: ")
language = input("\nEnter lanuage name:")
dict_data.update({name: language})


name = input("\nEnter friend's name: ")
language = input("\nEnter lanuage name:")
dict_data.update({name: language})

print("\nDictionary data: ", dict_data)

# Write a loop to allow 5 friends to enter their favourite language
print("\nAlternate way to enter friend's name and language:")
print("---------------------------------------------------")
for i in range(5):
    name = input(f"\nEnter {i + 1} friend's name: ")
    language = input(f"Enter {name}'s favourite language: ")
    dict_data[name] = language


print("\nDictionary data after loop: ", dict_data)
# Display the final dictionary
print("\nFinal Dictionary data: ", dict_data)