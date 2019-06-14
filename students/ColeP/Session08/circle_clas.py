import math


class Circle(object):
    tag = 'its a circle'

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @classmethod
    def from_diameter(cls, di):
        di = di/2
        return cls(di)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return self.radius + other.radius

    def __mul__(self, other):
        return self.radius * other

    def __lt__(self, other):
        if self.radius < other:
            return True
        return False

    def __gt__(self, other):
        if self.radius > other:
            return True
        return False

    def __eq__(self, other):
        if self.radius == other:
            return True
        return False


class Sphere(Circle):
    def volume(self):
        return (4/3) * math.pi * self.radius**3

    @property
    def area(self):
        return 4 * math.pi * self.radius**2

    def __str__(self):
        return 'Sphere with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)


