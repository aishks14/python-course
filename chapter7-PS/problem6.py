# WAP in python to calculate the factorial of a number using for loop
number = int(input("\nEnter a number:"))
factorial = number # assigning number to factorial to keep original number as intact which helps in printing the comment or message for the factorial of the number
for i in range(number-1, 0, -1):
    factorial = factorial*i
print(f"\nFactorial of number {number} is:", factorial)

# ---------------------------------------------------------------------------------
# Alternate way to do it
fact = 1
for i in range(1, number+1):
    fact = fact*i
print(f"\nFactorial of number {number} with alternate way is:", fact, "\n")

