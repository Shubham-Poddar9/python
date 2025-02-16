import math

class Polygon:
    def __init__(self):
        self._area = 0 

    def area(self):
        return self._area

    def calculate_area(self):  
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__()
        self._base = base
        self._height = height

    def calculate_area(self):  
        self._area = 0.5 * self._base * self._height

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width

    def calculate_area(self):  
        self._area = self._length * self._width

class Circle(Polygon):
    def __init__(self, radius):
        super().__init__()
        self._radius = radius

    def calculate_area(self):  
        self._area = math.pi * self._radius * self._radius

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  

class Pentagon(Polygon):
    def __init__(self, side):
        super().__init__()
        self._side = side

    def calculate_area(self):  
        self._area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self._side ** 2

class Hexagon(Polygon):
    def __init__(self, side):
        super().__init__()
        self._side = side

    def calculate_area(self): 
        self._area = (3 * math.sqrt(3) * self._side ** 2) / 2

def display_area(polygon):
    polygon.calculate_area()
    print(f"Area: {polygon.area()}")

# Testing the classes
triangle = Triangle(10, 5)
rectangle = Rectangle(6, 4)
circle = Circle(7)
square = Square(4)
pentagon = Pentagon(6)
hexagon = Hexagon(5)

display_area(triangle)
display_area(rectangle)
display_area(circle)
display_area(square)
display_area(pentagon)
display_area(hexagon)
