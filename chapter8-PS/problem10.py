# WAP in python to print multiplication table of a given number

print("\nTable of the a number:")
print("----------------------")
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

number = int(input("Enter a number for which you want table to print:"))
multiplication_table(number)
