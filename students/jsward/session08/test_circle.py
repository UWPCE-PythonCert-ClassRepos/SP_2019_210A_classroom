"""
Tests for circle_class
"""
from circle import Circle, Sphere
import math
import pytest


def test_init():
    radius = 12
    new_circle = Circle(radius)
    assert new_circle.radius == radius


def test_no_radius():
    with pytest.raises(TypeError):
        new_circle = Circle()


def test_diameter():
    new_circle = Circle(10)
    assert new_circle.diameter == 20


def test_diameter_change_radius():
    c = Circle(10)
    assert c.diameter == 20

    c.radius = 5
    assert c.diameter == 10
    assert c.radius == 5

    c.diameter = 14
    assert c.diameter == 14
    assert c.radius == 7


def test_area():
    c = Circle(2)
    assert math.isclose(c.area, 12.566370, rel_tol=1e-7)


def test_set_area():
    with pytest.raises(AttributeError):
        c = Circle(5)
        c.area = 20


def test_from_diameter_type():
    c = Circle.from_diameter(12)
    assert isinstance(c, Circle)
    assert c.radius == 6
    assert c.diameter == 12


def test_circle_from_diameter():
    c = Circle.from_diameter(10)
    assert c.diameter == 10
    assert c.radius == 5


def test_circle_str():
    c = Circle(4)
    assert str(c) == 'Circle with radius: 4.000000'


def test_add_circles():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = c1 + c2
    assert c3.radius == 10


def test_multiply_circle():
    c1 = Circle(10)
    c2 = c1 * 2
    assert c2.radius == 20


def test_equals():
    c1 = Circle(10)
    c2 = Circle(10)
    assert c1 == c2
    c3 = Circle(7)
    assert c1 != c3


def test_gt():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = Circle(7)
    assert c2 > c1
    assert not c2 > c3


def test_le():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = Circle(7)
    assert c1 < c2
    assert not c3 < c2


def test_sort():
    c1 = Circle(4)
    c2 = Circle(6)
    c3 = Circle(7)
    c4 = Circle(1)
    circles = [c1, c2, c3, c4]
    circles.sort()
    assert circles == [c4, c1, c2, c3]


######################
# TEST SPHERE SUBCLASS
######################


def test_sphere_r_d():
    s = Sphere(5)
    assert s.radius == 5
    assert s.diameter == 10


def test_sphere_volume():
    s = Sphere(4)
    assert s.volume == 268.082573106329


def test_sphere_area():
    s = Sphere(4)
    with pytest.raises(NotImplementedError):
        s.area


def test_sphere_from_diameter():
    s = Sphere.from_diameter(8)
    assert s.radius == 4
