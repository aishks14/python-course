# Inheritance 
    # It is a core concept in object-oriented programming (OOP) that allows one class (called a child or subclass) 
    # to inherit attributes and methods from another class (called a parent or superclass)
    # Types of inheritance
        # 1. Single Inheritance
        # 2. Multiple Inheritance  
        # 3. Multilevel Inheritance
        # 4. Hierarchical Inheritance
        # 5. Hybrid Inheritance
        
print("-----------------------------------")
print("Single Inheritance")
print("-----------------------------------")
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog is an animal who barks!")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog
print("\n")

print("-----------------------------------")
print("Multiple Inheritance")
print("-----------------------------------")
class Father:
    def skills(self):
        print("Father has following skills:\n01. Gardening\n02. Programming")

class Mother:
    def skills(self):
        print("Mother has following skills:\n01.Cooking\n02. Art")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Will call Father's method due to method resolution order
Mother.skills(c)  # To call Mother's method explicitly
print("\n")

print("-----------------------------------")
print("Multi Level Inheritance")
print("-----------------------------------")
class Grandparent:
    def legacy(self):
        print("Grandparents are blessings and they give us the family legacy")

class Parent(Grandparent):
    def guidance(self):
        print("Parents are like big shelters and provide parental guidance")

class Child(Parent):
    def play(self):
        print("Children are the joy of the family and they love to play")

childObj = Child()
childObj.legacy()
childObj.guidance()
childObj.play()
# Here childObj is an object that can access methods from Child, Parent, and Grandparent classes, due to multi level inheritance.
print("\n")

print("-----------------------------------")
print("Hierarchical Inheritance")
print("-----------------------------------")
class Vehicle:
    def start(self, vehicle):
        print(f"{vehicle} class method started")

class Car(Vehicle):
    def start(self, vehicle="Car"):
        Vehicle.start(self, "Car")  # Calls Vehicle's start()

class Bike(Vehicle):
    def start(self, vehicle="Bike"):
        Vehicle.start(self, "Bike")  # Calls Vehicle's start()

carObj = Car()
bikeObj = Bike()
carObj.start()
bikeObj.start()
# Above Bike and Car classess are used without `super()` function and we are calling
# Vehicle's start() method directly using class name.
print("\n") 

print("-----------------------------------")
print("Hybrid Inheritance")
print("-----------------------------------")

class A:
    def alpha(self):
        print("Method Alpha")

class B(A):
    def beta(self):
        print("Method Beta")

class C(A):
    def gamma(self):
        print("Method Gamma")

class D(B, C):
    def delta(self):
        print("Method Delta")

d = D()
d.alpha()
d.beta()
d.gamma()
d.delta()
# Here class D inherits from both B and C, which in turn inherit from A. 
# This is a hybrid inheritance structure.
print("\n")