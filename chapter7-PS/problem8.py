# WAP in python to print the following star pattern for 4 levels, for n = 4
'''
*
* * 
* * * 
* * * *
'''

number = int(input("\nEnter a number:"))
for i in range(1, number+1):
    # Print spaces
    print('*' * (i))