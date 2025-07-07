# WAP in python to print first n lines of the following pattern using recursive function:
'''
***
**
*
-for n = 3
'''

print("\nPrint first n lines of a pattern:")
print("---------------------------------")
def pattern(n):
    if n == 0:
        print("")
        return
    print("*" * n)
    pattern(n-1)

    
n = int(input("Enter the number to print first n lines of pattern: "))
number_of_pattern_lines = pattern(n)
print(f"Sum of first {n} natural numbers is: {number_of_pattern_lines}")