#! /usr/bin/env python3

"""
Goal:

The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the
diameter, and the user can query the circle for either its radius
or diameter.

Other abilities of a Circle instance:

        Compute the circle’s area.
        Print the circle and get something nice.
        Be able to add two circles together.
        Be able to compare two circles to see which is bigger.
        Be able to compare to see if they are are equal.
        (follows from above) be able to put them in a list and sort them.

You will use:

        properties.
        a bunch of “magic methods”.
        a classmethod (after you’ve learned about them…).

General Instructions:

    For each step, write a couple of unit tests that test the new features.
    Run these tests (and they will fail the first time)
    Add the code required for your tests to pass.
"""
import math

class Circle:
    """
    The circle class
    """
    def __init__(self, radius):
        self.radius = radius


    @property
    def diameter(self):
        """get the diameter or the circle"""
        return self.radius * 2


    @diameter.setter
    def diameter(self, val):
        """set the diameter or the circle via the radius"""
        self.radius = val / 2


    @property
    def area(self):
        """get the area or the circle"""
        return math.pi * (self.radius * self.radius)


    @classmethod
    def from_diameter(cls, diameter):
        """initialize a circle using diameter"""
        return cls(diameter / 2)


    def harmonize_types(self, other):
        """function to deal with non-circle comparison inputs"""
        if isinstance(self, Circle) and isinstance(other, Circle):
            return (self.radius, other.radius)
        elif isinstance(self, Circle) and not isinstance(other, Circle):
            return (self.radius, other)
        elif not isinstance(self, Circle) and isinstance(other, Circle):
            return (self, other.radius)
        else:
            return (self, other)


    def __str__(self):
        """get the details of the circle"""
        return 'Circle with radius: {:.5f}'.format(self.radius)


    def __repr__(self):
        """get the representation of the circle"""
        return '{}({})'.format(self.__class__.__name__, self.radius)

    # Basic Math Operations
    def __add__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self + new_other)

    def __sub__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        if new_self >= new_other:
            return Circle(new_self - new_other)
        else:
            return Circle(0)

    def __mul__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self * new_other)

    def __truediv__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self / new_other)

    def __floordiv__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self // new_other)

    def __mod__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self % new_other)

    def __pow__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self ** new_other)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rpow__(self, other):
        return self.__pow__(other)

    # Comparison Operations
    def __lt__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self < new_other

    def __gt__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self > new_other

    def __eq__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self == new_other

    def __le__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self <= new_other

    def __ge__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self >= new_other

    def __ne__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self != new_other

    # Assignment Operations
    def __iadd__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self + new_other)

    def __isub__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        if new_self > new_other:
            return Circle(new_self - new_other)
        else:
            return Circle(0)

    def __imul__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return Circle(new_self * new_other)

    def __idiv__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        new_radius = new_self / new_other
        if new_radius > 0:
            return Circle(new_radius)

        return Circle(0)

    def __ifloordiv__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        new_radius = new_self // new_other
        if new_radius > 0:
            return Circle(new_radius)

        return Circle(0)

    def __imod__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self % new_other

    def __ipow__(self, other):
        (new_self, new_other) = self.harmonize_types(other)
        return new_self ** new_other



class Sphere(Circle):
    """
    The sphere class
    """
    def volume_to_radius(self):
        return self.volume / (4.0/3.0 * math.pi) ** (1./3.)

    @property
    def area(self):
        raise AttributeError("Invalid attribute for Sphere")

    @property
    def volume(self):
        """return the volume of a sphere calculated from radius"""
        return (4.0/3.0 * math.pi) * (self.radius ** 3)

    @volume.setter
    def volume(self, val):
        self.volume = val
        self.radius = self.volume_to_radius()

    def __str__(self):
        return 'Sphere with radius: {:.5f} and volume {:.10f}'.format(self.radius, self.volume)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.radius)
