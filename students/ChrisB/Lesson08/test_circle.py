"""
tests for Circle class
"""
import math
import pytest

from circle import Circle, Sphere


def test_init():
    c = Circle(10)
    assert c.radius == 10


def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()


def test_diameter():
    c = Circle(10)
    assert c.diameter == 20


def test_diameter_change_radius():
    c = Circle(10)
    assert c.diameter == 20
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8


def test_diameter_change_diameter():
    c = Circle(10)
    assert c.radius == 10
    assert c.diameter == 20

    c.diameter = 4
    assert c.radius == 2
    assert c.diameter == 4


def test_area():
    c = Circle(2)
    assert math.isclose(c.area, 12.56637061, rel_tol=1e-8)


def test_set_area():
    c = Circle(5)
    with pytest.raises(AttributeError):
        c.area = 20

def test_from_diameter_type():
    c = Circle.from_diameter(10)

    assert isinstance(c, Circle)

def test_init_diameter():
    c = Circle.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5


def test_static_class():
    assert Circle.something() == "this worked"


def test_static_instance():
    c = Circle(2)
    assert c.something() == "this worked"


def test_square():
    assert Circle.square(10) == 100


def test_square_sphere():
    assert Sphere.square(10) == 100


def test_sphere():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10


def test_sphere_area():
    s = Sphere(5)

    with pytest.raises(AttributeError):
        s.area


def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(10)
    s.radius == 5
    # is this an instance of a Sphere?
    assert isinstance(s, Sphere)
    # it is also a Circle because it's a subclass of Circle
    # with subclassing, it is *both* a Circle and a Sphere
    #  (and an object)
    assert isinstance(s, Circle)
    assert isinstance(s, object)

    # checks if it is exactly this type
    assert type(s) is Sphere
    # but not exactly a Circle
    assert not type(s) is Circle





