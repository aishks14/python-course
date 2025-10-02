# WAP in python to create a class with a class attribute `a` and create an object from it and set `a`
# directly using object.a = 0. Check if this changes the class attribute

class MyClass:
    a = 10  # Class attribute       
obj = MyClass()  # Creating an object of MyClass
print("Initial value of class attribute 'a':", MyClass.a)  # Output: 10
obj.a = 0  # Setting 'a' directly using the object
print("Value of 'a' after setting it using the object:", obj.a)  # Output: 0
print("Value of class attribute 'a' after setting it using the object:", MyClass.a )

# So, changing obj.a does not change MyClass.a