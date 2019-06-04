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

def test_mul():
    c = Circle(10)
    assert (c * 2).radius == 20

def test_reverse_mul():
    pytest.skip()
    c = Circle(10)
    assert (2 * c).radius == 20

def test_sort():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    assert sorted(circles)[0].radius == 0

def test_sphere_init():
    c = Sphere(10)
    assert c.radius == 10

def test_sphere_no_radius():
    with pytest.raises(TypeError):
        c = Sphere()

def test_sphere_diameter():
    c = Sphere(10)
    assert c.diameter == 20
    c.radius = 15
    assert c.diameter == 30

def test_sphere_diameter_change():
    c = Sphere(10)
    c.diameter = 10
    assert c.radius == 5

def test_sphere_area():
    c = Sphere(10)
    assert c.area == 400 * math.pi
    assert math.isclose(c.area, 314, rel_tol = 1e-0)

def test_sphere_volume():
    c = Sphere(10)
    assert c.volume == 1000 * 4 / 3 * math.pi
    assert math.isclose(c.area, 314, rel_tol = 1e-0)

def test_sphere_from_diameter():
    c = Sphere.from_diameter(10)
    assert isinstance(c, Sphere)

def test_sphere_print():
    c = Sphere(10)
    assert print(c) == None

def test_sphere_add():
    c = Sphere(10)
    c2 = Sphere(20)
    assert c + c2 == 30

def test_sphere_repr():
    c = Sphere(10)
    d = eval(repr(c))
    assert d.radius == 10

def test_sphere_mul():
    c = Sphere(10)
    assert (c * 2).radius == 20

def test_sphere_reverse_mul():
    pytest.skip()
    c = Sphere(10)
    assert (2 * c).radius == 20

def test_sphere_sort():
    circles = [Sphere(6), Sphere(7), Sphere(8), Sphere(4), Sphere(0), Sphere(2), Sphere(3), Sphere(5), Sphere(9), Sphere(1)]
    assert sorted(circles)[0].radius == 0