# WAP in python to check if `self` can be named something else other than self. 
class MyClass:
    def __init__(this, value):  # Using 'this' instead of 'self'
        this.value = value

    def display(this):
        print(f"Value: {this.value}")

print("----------------------------------------------")
print("Checking if `self` can be named something else")
print("----------------------------------------------")        
obj = MyClass(10)
obj.display()  # Output: Value: 10
# Yes, it can be named something else, but using 'self' is a strong convention in Python.
print("Yes, it can be named something else, but using 'self' is a strong convention in Python.")