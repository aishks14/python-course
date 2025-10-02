class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()


# Dog is the class.
# my_dog is the object created from that class.
# __init__ is a special method(or constructor) called when the object is created.

# ------------------------------------------------------------------
class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = Parrot("Polly", 2)
parrot2 = Parrot("Rio", 4)

print(parrot1.name)
print(parrot2.age)

# -------------------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Honda", "Civic")
car2 = Car("Tesla", "Model 3")

print(car1.brand)
print(car2.model)

# -------------------------------------------------------------------
class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

clock1 = Clock(10, 30)
clock2 = Clock(3, 45)

print(f"Time: {clock1.hour}:{clock1.minute}")