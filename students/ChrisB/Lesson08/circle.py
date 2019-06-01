#!/usr/bin/env python

"""
nifty Circle class
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def something():
        return "this worked"

    @staticmethod
    def square(x):
        return x * x



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
        return math.pi * self.square(self.radius)


class Sphere(Circle):
    @property
    def area(self):
        raise AttributeError("sphere does not have an area defined")

