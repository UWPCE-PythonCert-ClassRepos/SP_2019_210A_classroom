'''
test circle
'''

import pytest
import math

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
    assert  c.diameter == 20
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


def test_are():
    c = Circle(2)
    assert math.isclose(c.area, 12.566370, rel_tol=1e-6)

# def test_set_area():
#     c = Circle(5)
#     with pytest.raises(AttributeError):
#         c.area = 20

def test_from_diameter_type():
    c = Circle.from_diameter(10)

    assert isinstance(c, Circle)

def test_init_diameter():
    c = Circle.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5

def test_sphere():
    s = Sphere(5)
    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_area():
    s = Sphere(5)

    with pytest.raises(NotImplementedError):
       s.area

def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(10)
    assert 5 == s.radius

def test_str():
    s = Circle(4)
    assert "Circle with radius: 4.000000" == str(s)

def test_repr():
    s = Circle(4)
    assert "Circle(4)" == repr(s)

def test_add():
    a = Circle(2)
    b = Circle(4)
    output = a + b
    assert 6 == output.radius

def test_comparison():
    a = Circle(2)
    b = Circle(4)
    c = Circle(2)

    assert a < b
    assert a == c
    assert b > c

def test_sort():
    input = [Circle(6), Circle(2), Circle(4), Circle(2)]
    input.sort()
    assert 2 == input[0].radius
    assert 2 == input[1].radius
    assert 4 == input[2].radius
    assert 6 == input[3].radius

def test_multiply_by_int():
    a = Circle(2)
    amul = a * 2
    armul = 2 * a
    assert 4 == amul.radius
    assert 4 == armul.radius
    assert amul == armul

def test_operation_equal():
    a = Circle(3)
    a += Circle(1)
    assert 4 == a.radius

    a *= 2
    assert 8 == a.radius

def test_sphere_str():
    a = Sphere(2)
    assert "Sphere with radius: 2.000000" == str(a)
    assert "Sphere(2)" == repr(a)

def test_sphere_volume():
    a = Sphere(4)
    assert math.isclose(268.08, a.volume, rel_tol=1e-4)
