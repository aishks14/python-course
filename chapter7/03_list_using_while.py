# Exxample to print the content of a list using while loop
# This code demonstrates how to print the content of a list using a while loop.
# It initializes a list with some elements and then uses a while loop to iterate through the list,
# printing each element until it reaches the end of the list.

my_list = [1, True, "Python", "Programming", 2, 3, 4, 5]
index = 0
print("\nPrinting the content of a list using a while loop:")
print("----------------------------------------------------")
while index < len(my_list):
    print(my_list[index])
    index += 1