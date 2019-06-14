#!/usr/bin/env python

"""
nifty circle
"""


import math



class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, value):
        self.radius = value/2

    @property
    def area(self):
        return math.pi*self.radius**2

    def __str__(self):
        return "Circle with radius: "+'{0:f}'.format(self.radius)

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if (type(other) == Circle) and (type(self) == Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __rmul__(self, other):
        if (type(other) == Circle) and (type(self) == Circle):
            return Circle(self.radius * other.radius)
        else:
            return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    @staticmethod
    def sort_key(a_circle):
        return a_circle.radius

class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: "+'{0:f}'.format(self.radius)

    def __repr__(self):
        return f"Sphere({self.radius})"

    @property
    def volume(self):
        return 4/3*math.pi*self.radius**3

    @property
    def area(self):
        return 4*math.pi*self.radius**2