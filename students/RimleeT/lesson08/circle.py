import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

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

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(round(self.radius))

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)

    __rmul__ = __mul__
    __iadd__ = __add__
    __imul__ = __mul__


class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(round(self.radius))

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius ** 3
    @property
    def area(self):
        raise NotImplementedError("sphere doesnt have an area")
