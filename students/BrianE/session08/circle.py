import math


class Circle:
    """
    Class to store and calculate circle statistics
    """

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, val):
        if hasattr(val, "radius"):
            return Circle(self.radius + val.radius)
        else:
            return Circle(self.radius + val)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, val):
        if hasattr(val, "radius"):
            return Circle(self.radius * val.radius)
        else:
            return Circle(self.radius * val)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    @property
    def diameter(self):
        self._diameter = self.radius * 2
        return self._diameter

    @diameter.setter
    def diameter(self, val):
        self._diameter = val
        self.radius = self._diameter / 2

    @property
    def area(self):
        self._area = math.pi * self.radius ** 2
        return self._area


class Sphere(Circle):
    """
    Subclass of Circle to store and calculate sphere statistics
    """

    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        self._volume = 4/3 * math.pi * self.radius ** 3
        return self._volume

    @property
    def area(self):  # surface area
        self._area = 4 * math.pi * self.radius ** 2
        return self._area
