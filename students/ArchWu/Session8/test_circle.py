"""
tests for circle
"""

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
    c.radius = 15
    assert c.diameter == 30

def test_diameter_change():
    c = Circle(10)
    c.diameter = 10
    assert c.radius == 5

def test_area():
    c = Circle(10)
    assert c.area == 100 * math.pi
    assert math.isclose(c.area, 314, rel_tol = 1e-0)

def test_from_diameter():
    c = Circle.from_diameter(10)
    assert isinstance(c, Circle)

def test_sphere():
    s = Sphere.from_diameter(10)
    s.radius = 5
    assert isinstance(s, Sphere)

def test_print():
    c = Circle(10)
    assert print(c) == None

def test_add():
    c = Circle(10)
    c2 = Circle(20)
    assert c + c2 == 30

def test_repr():
    c = Circle(10)
    d = eval(repr(c))
    assert d.radius == 10