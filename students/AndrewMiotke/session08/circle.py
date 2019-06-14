import math

class Circle:
    def __init__(self, radius):
        self.radius = radius


    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


    # Turns diameter into a property to be used as a property of the class Circle
    @property
    def diameter(self):
        return self.radius * 2


    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


    @property
    def area(self):
        return math.pi * self.radius ** 2


class Sphere(Circle):
    @property
    def area(self):
        raise AttributeError("sphere does not have an area defined")