""" Tests for circle.py """

from circle import Circle, Sphere
import pytest
import math

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

    assert math.isclose(c.area, 12.566370, rel_tol=1e-7)


def test_set_area():
    c = Circle(5)
    with pytest.raises(AttributeError):
        c.area = 20


def test_from_diameter_type():
    c = Circle.from_diameter(5)

    assert isinstance(c, Circle)


def test_init_diamater():
    c = Circle.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5


def test_sphere():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10


def test_sphere_area():
    s = Sphere(5)

    with pytest.raises(AttributeError):
        s.area


def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(5)
    s.radius == 5

    assert isinstance(s, Sphere)