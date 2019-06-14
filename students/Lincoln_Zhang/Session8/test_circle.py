#!/usr/bin/env python3

from circle import circle
from circle import sphere

c1 = circle(3)
c2 = circle(5)
c3 = circle.from_diameter(10)
c4 = circle(10)
s1 = sphere(3)
s2 = sphere.from_diameter(6)

circles = [c4,c2,c1,c3]



def test_repr():
    result = c1.__repr__()
    assert result == "A circle with radius 3"

def test_init_():
    result = c1.radius
    assert result == 3

def test_lt_():
    assert c2 > c1
    assert c1 < c2
    assert c1 != c2

def test_add_():
    result = c1 + c2
    assert result == 8

def test_mul_():
    result = c1 * c2
    assert result == 15

def test_classmethod():
    assert c3.radius == 5
    assert c3.area == c2.area

def test_property():
    assert c1.radius == 3
    assert c1.diameter == 6
    assert c2.radius == 5
    assert c2.diameter == 10

def test_sort():
    circles.sort()
    assert circles[0] < circles[1]
    assert circles[2] < circles[3]

def test_inheritance():
    assert s2.radius == 3
    assert s1.volume == s2.volume

def test_subclass():
    assert isinstance(s1,sphere)
    assert issubclass(sphere,circle)
