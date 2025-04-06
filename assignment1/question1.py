# Base class
class Vehicle:
    def describe(self):
        print("This is a vehicle.")

# Subclass 1
class Car(Vehicle):
    def describe(self):
        print("This is a car. It has 4 wheels.")

# Subclass 2
class Bike(Vehicle):
    def describe(self):
        print("This is a bike. It has 2 wheels.")

# Test the classes
v = Vehicle()
c = Car()
b = Bike()

v.describe()  # Output: This is a vehicle.
c.describe()  # Output: This is a car. It has 4 wheels.
b.describe()  # Output: This is a bike. It has 2 wheels.
