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
from math import pi, sqrt

# print("hello world")


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius*2

    @diameter.setter
    def diameter(self, value):
        self._radius = value/2

    @property
    def area(self):
        return pi * self._radius**2

    @area.setter
    def area(self, value):
        self._radius = sqrt(value / pi)

    @classmethod
    def from_diameter(circle_object, value):
        """
        method taking the diameter of the circle object for calculations
        :param value: sets the circle's diameter
        :return: the radius of the circle
        """
        return circle_object(value/2)

    def __str__(self):
        """
        converts the object to a string
        :return: a circle's radius as a string
        """
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        """
        represents a printable object as a string
        :return: a string containing a printable representation of a circle
        """
        return f'Circle({self.radius})'

    def __add__(self, other):
        """
        method adding 2 radius' together
        :param other: size to the other radius
        :return: a circle with size of both radii
        """
        return f'Circle({self.radius+other.radius})'

    def __mul__(self, value):
        """
        method multiplying the radius of a circle
        :param value: sets the radius multiplier
        :return: new circle of radius (radius * value)
        """
        return f'Circle({self.radius*value})'

    def __rmul__(self, value):
        """
        method reverse multiplying the radius of a circle
        :param value: sets the radius multiplier
        :return: new circle of radius (value * radius)
        """
        return f'Circle({self.radius*value})'

    def __gt__(self, other):
        """
        method to determine which if 2 radius' is greater than
        :param other: size of other.radius
        :return: determination that self.radius is greater
        """
        return self.radius > other.radius

    def __lt__(self, other):
        """
        method to determine which if 2 radius' is lesser than
        :param other: size of other.radius
        :return: determination that self.radius is lesser
        """
        return self.radius < other.radius

    def __eq__(self, other):
        """
        method to determine which if 2 radius' are equal
        :param other: size of other.radius
        :return: determination that self.radius is same size as other.radius
        """
        return self.radius == other.radius


class Sphere(Circle):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Sphere with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        return (4/3)*pi*self._radius**2

    @volume.setter
    def volume(self, value):
        self._radius = sqrt((3 * value)/(4 * pi))

    @property
    def area(self):
        return 4 * pi * self._radius**2

    @area.setter
    def area(self, value):
        self._radius = sqrt(value/(4 * pi))
