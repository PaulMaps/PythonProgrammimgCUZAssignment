# Base class Shape
class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Shape initialized with name: {self.name}")

    def calculate_area(self):
        pass  # Base class doesn't implement it

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # Call the constructor of Shape
        self.width = width
        self.height = height

    def calculate_area(self):
        # Optionally call the parent method (even if it does nothing)
        super().calculate_area()
        return self.width * self.height

# Using the Rectangle class
rect = Rectangle("My Rectangle", 5, 3)
print(f"Area of {rect.name}: {rect.calculate_area()}")
