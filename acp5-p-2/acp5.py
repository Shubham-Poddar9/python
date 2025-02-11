import math

class Polygon:
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

def calculate_area(polygon):
    return polygon.area()

triangle = Triangle(10, 5)
rectangle = Rectangle(6, 4)
circle = Circle(7)

print(f"Area of Triangle: {calculate_area(triangle)}")
print(f"Area of Rectangle: {calculate_area(rectangle)}")
print(f"Area of Circle: {calculate_area(circle)}")
