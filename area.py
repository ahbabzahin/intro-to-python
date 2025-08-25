from abc import ABC, abstractmethod
import math

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rect(Polygon):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Tri(Polygon):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

class Circ(Polygon):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

class Sq(Rect):
    def __init__(self, s):
        super().__init__(s, s)

if __name__ == "__main__":
    shapes = [
        Rect(10, 5),
        Tri(6, 4),
        Circ(7),
        Sq(4)
    ]

    for sh in shapes:
        print(f"{sh.__class__.__name__} Area: {sh.area():.2f}")
