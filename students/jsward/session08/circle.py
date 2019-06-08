import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(self.radius)

    @classmethod
    def from_diameter(cls, diameter):
        # creates an instance of the class
        # since init takes radius as a parameter,
        # Passes in diameter / 2
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


class Sphere(Circle):
    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(self.radius)

    @property
    def area(self):
        raise NotImplementedError

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3
