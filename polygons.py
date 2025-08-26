import math

class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height

class Circle(Polygon):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

shapes = [
    Rectangle(10, 5),
    Triangle(6, 4),
    Circle(3),
    Square(7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
