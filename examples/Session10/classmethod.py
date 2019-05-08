

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"

    def __add__(self, other):
        radius = self.radius + other.radius
        return self.__class__(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @classmethod
    def from_diameter(cls, diam):

        return cls(diam / 2)


class Sphere(Circle):
    pass

    # def __repr__(self):
    #     return f"Sphere({self.radius})"

