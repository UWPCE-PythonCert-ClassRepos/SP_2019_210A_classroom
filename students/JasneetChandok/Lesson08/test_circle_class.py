#!usr/bin/env python3

''' Lesson 8 : Circle Excercise Test'''

from circle_class import Circle, Sphere
from math import isclose, pi


def test_radius():
    c = Circle(5)
    assert c.radius == 5


def test_diameter():
    c = Circle(7)
    assert c.diameter == 14


def test_set_diameter():
    c = Circle(7)
    assert c.diameter == 14
    c.diameter = 10
    assert c.diameter == 10


def test_change_radius_diameter():
    c = Circle(9)
    c.diameter = 50
    assert c.radius == 25


def test_set_area():
    c = Circle(2)
    assert isclose(c.area, (pi * 2**2), rel_tol=.01)
    c.area = 500
    assert isclose(c.area, 500, rel_tol=.01)


def test_change_values_area():
    c = Circle(13)
    c.area = 6
    assert isclose(c.radius, 1.38, rel_tol=.01)
    assert isclose(c.diameter, c.radius * 2, rel_tol=.01)


def test_from_diameter():
    c = Circle.from_diameter(16)
    assert c.diameter == 16
    assert c.radius == 8


def test_str():
    c = Circle(15)
    assert str(c) == "Circle with radius: 15.000000"
    assert repr(c) == "Circle(15)"


def test_sphere():
    s1 = Sphere(15)
    assert str(s1) == "Sphere with radius: 15.000000"
    assert repr(s1) == "Sphere(15)"
    assert isclose(s1.volume, 943, rel_tol=.01)
    assert isclose(s1.area, 2827.43, rel_tol=.01)
    s1.volume = 7
    assert isclose(s1.volume, 7, rel_tol=.01)
    assert isclose(s1.radius, 1.29, rel_tol=.01)
    s2 = Sphere.from_diameter(18)
    assert s2.radius == 9
