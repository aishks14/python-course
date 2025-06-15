#WAP in python to store seven fruits in a list entered by the user. Then display the list in alphabetical order.
fruits = []
f1 = input("Enter the first fruit: ")
fruits.append(f1)
f2 = input("Enter the second fruit: ")
fruits.append(f2)
f3 = input("Enter the third fruit: ")
fruits.append(f3)
f4 = input("Enter the fourth fruit: ")
fruits.append(f4)
f5 = input("Enter the fifth fruit: ")
fruits.append(f5)
f6 = input("Enter the sixth fruit: ")
fruits.append(f6)
f7 = input("Enter the seventh fruit: ")
fruits.append(f7)

# Display the list in alphabetical order
fruits.sort()
print("Fruits in alphabetical order:", fruits)

# Alternatively, you can use a loop to collect the fruits
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)
fruits.sort()
print("Fruits in alphabetical order:", fruits)

