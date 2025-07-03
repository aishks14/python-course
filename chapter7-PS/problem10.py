# WAP in pyhton to print multiplication table of n using for loop in reverse order
number = int(input("\nEnter a number:"))
print("\nTable of a given number in reverse order:")
print("-----------------------------------------")
for i in range(10, 0, -1):
    print(f"{number} x {i} = {number*i}")

# ---------------------------------------------------------------------------------
# Alternate way to do this table printing in reverse order
print("\nAlternate way to do this table printing in reverse order:")
print("----------------------------------------------------------")
for i in range(1, 11):
    print(f"{number} x {11 - i} = {number*(11-i)}")