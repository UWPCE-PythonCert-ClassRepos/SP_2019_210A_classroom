"""
Unit testing Circle
FredBallyns
Session08
"""

import pytest, sys, os, math
from circle import Circle, Sphere


def test_init():
    c = Circle(1)


def test_radius():
    c = Circle(10)
    assert c.radius == 10


def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()


def test_diameter():
    c = Circle(11)
    assert c.diameter == 22


def test_change_radius_change_diameter():
    c = Circle(12)
    assert c.radius == 12
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8


def test_change_diameter_change_radius():
    c = Circle(11)
    assert c.radius == 11
    c.diameter = 8
    print(c.radius)
    assert c.radius == 4
    assert c.diameter == 8


def test_area():
    c = Circle(1)
    assert math.isclose(c.area, 3.1415, rel_tol=1e-4)


def test_cant_set_area():
    c = Circle(12)
    with pytest.raises(AttributeError):
        c.area = 42


def test_circle_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8

def test_str():
    c = Circle(9)
    assert str(c) == "Circle with radius: 9.000000"
    c = Circle(4.11)
    assert str(c) == "Circle with radius: 4.110000"
    c = Circle(84.11)
    assert str(c) == "Circle with radius: 84.110000"

def test_repr():
    c = Circle(9)
    assert repr(c) == "Circle(9)"
    c = Circle(4.11)
    assert repr(c) == "Circle(4.11)"
    c = Circle(84.11)
    assert repr(c) == "Circle(84.11)"

def test_add_circles():
    c1=Circle(1)
    c2=Circle(2)
    c3=c1+c2
    assert c3.radius == 3

def test_multiply_right():
    c3=Circle(3)
    c6= c3 * 2
    assert c6.radius == 6
    c6= c3 * 2.2
    assert math.isclose(c6.radius, 6.6, rel_tol=1e-4)

def test_multiply_left():
    c3=Circle(3)
    c6= 2 * c3
    assert c6.radius == 6
    c6= 2.2 * c3
    assert math.isclose(c6.radius, 6.6, rel_tol=1e-4)

def test_multiply_two_circles():
    c2=Circle(2)
    c3=Circle(3)
    c6= c2 * c3
    assert c6.radius == 6

def test_equal():
    c2 = Circle(2)
    c3 = Circle(3)
    c3.radius=2
    assert c2 == c3

def test_not_equal():
    c2=Circle(2)
    c3=Circle(3)
    assert c2 != c3

def test_less():
    c2=Circle(2)
    c3=Circle(3)
    assert c2 < c3
    assert c2 <= c3

def test_greater():
    c2=Circle(2)
    c3=Circle(3)
    assert c3 > c2
    assert c3 >= c2

def test_sort():
    c1=Circle(1)
    c2=Circle(2)
    c3=Circle(3)
    c4=Circle(4)
    group = [c4, c1, c3, c2]
    group.sort()
    assert group == [c1, c2, c3, c4]

def test_str_Sphere():
    c = Sphere(9)
    assert str(c) == "Sphere with radius: 9.000000"
    c = Sphere(4.11)
    assert str(c) == "Sphere with radius: 4.110000"
    c = Sphere(84.11)
    assert str(c) == "Sphere with radius: 84.110000"

def test_repr_Sphere():
    c = Sphere(9)
    assert repr(c) == "Sphere(9)"
    c = Sphere(4.11)
    assert repr(c) == "Sphere(4.11)"
    c = Sphere(84.11)
    assert repr(c) == "Sphere(84.11)"

def test_volume_Sphere():
    s=Sphere(10)
    assert math.isclose(s.volume, 4188.790205, rel_tol=1e-4)

def test_area_Sphere():
    s=Sphere(10)
    assert math.isclose(s.area, 1256.637061, rel_tol=1e-4)

def test_multiply_right_Sphere():
    c3=Sphere(4)
    c6= c3 * 2
    assert c6.radius == 8
    c6= c3 * 2.2
    assert math.isclose(c6.radius, 8.8, rel_tol=1e-4)

def test_add_Spheres():
    c1=Sphere(1)
    c2=Sphere(2)
    c3=c1+c2
    assert c3.radius == 3

def test_sort_Sphere():
    c1=Sphere(4)
    c2=Sphere(3)
    c3=Sphere(2)
    c4=Sphere(1)
    group = [c4, c1, c3, c2]
    group.sort()
    assert group == [c4, c3, c2, c1]

def test_Sphere_from_diameter():
    s=Sphere.from_diameter(5)
    assert s.diameter == 5