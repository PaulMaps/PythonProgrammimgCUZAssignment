import math

# Base class
class Shape:
    def calculate_area(self):
        pass  # To be implemented by subclasses

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Function that uses polymorphism
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.calculate_area()
    return total

# Test the function
shapes = [
    Circle(3),
    Rectangle(4, 5),
    Circle(1.5),
    Rectangle(2, 3)
]

print("Total area of all shapes:", total_area(shapes))
