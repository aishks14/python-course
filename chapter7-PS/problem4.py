# WAP in python to find whether a number is prime or not
number = int(input("Enrter a number:"))

for i in range(2, number):
    if(number%i) == 0:
        print(f"The number {number} is not prime")
        break
else: 
    print(f"The number {number} is prime")
