import math

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def yeea():
        return "this worked"
    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
    
    @property
    def area(self):
        return self.radius ** 2 * math.pi
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

class Sphere(Circle):
    @property
    def area(self):
        pass