# WAP in python print a multiplication table of a given numer using while loop
number = int(input("Enter a number for which you want table to print:"))
print("\nTable of the entered number:")
print("----------------------------")
i = 1
while i < 11:
    print(f"{number} x {i} = {number*i}")
    i+=1