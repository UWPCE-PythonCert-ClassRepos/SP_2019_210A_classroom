# Dev: Miguel Rovira-Gonzalez
# Lesson08: Circle Assignment

"""
nifty circle class
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle{self.radius!r}"

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @staticmethod
    def sort_key(a_circle):
        return a_circle.radius

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other

    def __rmul__(self, other):
        return other * self.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):

    def __str__(self):
        return f'This is Sphere with a radius: {self.radius}'

    def __repr__(self):
        return f'This is a more formal Sphere with a radius: {self.radius}'

    @property
    def area(self):
        raise AttributeError("sphere does not have an area defined")

    def volume(self):
        self.volume = ((4/3) * math.pi * self.radius ** 3)
        return self.volume






