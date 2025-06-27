# Loop Control Statements
# Loop control statements are used to change the flow of a loop.
# They can be used to skip iterations, exit loops, or continue to the next iteration.
# - `break`: Exits the loop immediately.
# - `continue`: Skips the current iteration and continues with the next iteration.
# - `pass`: Does nothing and is used as a placeholder.

# Example of break and continue
print("\nLoop control statements example:")
for i in range(2, 20):
    if i == 15:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5
    elif i % 2 == 0:
        print("Skipping even number:", i)
        continue  # Skip the rest of the loop for even numbers
    print("Current value of i:", i)  # This will only print for odd numbers before 5

# ----------------------------------------------------------------------------------
# Examle of `pass`
print("\nExample of pass:")
print("-----------------")
for i in range(600):
    pass # this will pass the execution to next part and execute the while loop

i = 0
while (i<46):
    print(i)
    i+=1
