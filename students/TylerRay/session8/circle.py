
#!usr/bin/env python3
# ---------------------------------------------------------------------
# The goal is to create a class that represents
# a simple circle.
#
# A Circle can be defined by either specifying
# the radius or the diameter, and the user can
# query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#   Compute the circle’s area.
#   Print the circle and get something nice.
#   Be able to add two circles together.
#   Be able to compare two circles to see which is bigger.
#   Be able to compare to see if they are are equal.
#   (follows from above) be able to put them in a list and sort them.
# ---------------------------------------------------------------------

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @ classmethod
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

    def __str__(self):
        return "Circle with Radius:"


class Sphere(Circle):

    def __init__(self, radius):
        self.radius = radius

    @property
    def volume(self):
        return self.radius ** 3 * 4 / 3 * math.pi

    @property
    def area(self):
        return math.pi * 4 * self._radius**2

    def __str__(self):
        return f'Sphere with radius: {self.radius:.6f}'

    def __repr__(self):
        return "Sphere({})".format(self.radius)
