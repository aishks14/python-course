# WAP in python to create a class `Train` which has methods to book a ticket, get status, and get 
# fare information. The class should have a class attribute `total_seats` which is initialized to a certain number.
# Each time a ticket is booked, the `total_seats` should decrease by one.
from random import randint

TRAIN_NAME = "LUCKNOW NEW DELHI AC SUPERFAST EXPRESS"

class Train:
    total_seats = 100  # Class attribute to keep track of total seats

    def __init__(self, name, train_number):
        self.name = name
        self.train_number = train_number

    def book_ticket(self):
        if Train.total_seats > 0:
            Train.total_seats -= 1
            print(f"Ticket booked successfully! Seats left: {Train.total_seats}")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Train Name: {self.name}")
        print(f"Train Number: {self.train_number}")
        print(f"Fare: {randint(500, 5000)}")  # Random fare for demonstration
        print(f"Total Seats Available: {Train.total_seats}")

    @staticmethod
    def get_fare_info():
        return "Fare information is available on the official website."

print("---------------------------------------")
print("Train Reservation System")
print("---------------------------------------")   
train = Train(TRAIN_NAME, 12429)
train.get_status()
train.book_ticket()
print(Train.get_fare_info())
print("----------------------------------------")

train = Train(TRAIN_NAME, 12429)
train.get_status()
train.book_ticket()
print(Train.get_fare_info())
print("----------------------------------------")

train = Train(TRAIN_NAME, 12429)
train.get_status()
train.book_ticket()
print(Train.get_fare_info())
print("----------------------------------------")
    
