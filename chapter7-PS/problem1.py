# WAP in python print a multiplication table of a given numer using for loop
number = int(input("Enter a number for which you want table to print:"))
print("\nTable of the entered number:")
print("----------------------------")
for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")