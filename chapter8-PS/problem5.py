# WAP in python to calculate the sum of the first n natural numbers recursively
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = sum(5) = 1 + 2 + 3 + 4 + 5 + ...... + n
'''
print("\nSum of first n natural numbers recursilvely:")
print("--------------------------------------------")
def sum(n):
    if(n == 1):
        return 1
    else:
        return sum(n-1) + n
    
n = int(input("Enter the number till which the sum has to be calculated: "))
sum_n_natural_numbers = sum(n)
print(f"Sum of first {n} natural numbers is: {sum_n_natural_numbers}")