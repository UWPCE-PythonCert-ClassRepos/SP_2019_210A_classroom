
"""
nifty circle class
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)


    @property
    def diameter(self):
        return self.radius * 2.0


    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0


    @property
    def area(self):
        return math.pi * self.radius ** 2.0


    def __str__(self):
        return f'Circle with radius: {self.radius:g}'


    def __repr__(self):
        return f"Circle ({self.radius!r})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return self.radius * other

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @staticmethod
    def sort_key(c_circle):
        return c_circle.radius


    

class Sphere(Circle):

    def __str__(self):
        return f'Sphere radius is: {self.radius}'

    def __repr__(self):
        return f"Sphere ({self.radius!r})"
    
    @property
    def area(self):
        return math.pi * 4 * self.radius ** 2
    
    
    def volume(self):
        return 4/3 * math.pi * self.radius ** 3




s = Sphere(4)
print(s.area)