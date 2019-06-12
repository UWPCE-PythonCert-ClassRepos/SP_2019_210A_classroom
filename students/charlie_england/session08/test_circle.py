#!/usr/bin/env python

from circle import Circle as C
from circle import Sphere
import pytest
import math
#Step 1
def test_circle():
    cyrc = C(10)
    assert cyrc.radius == 10

def test_no_radius():
    with pytest.raises(TypeError):
        cyrc = C()
#Step2
def test_diameter():
    c = C(10)
    assert c.diameter == 20

def test_diameter_change_radius():
    c = C(10)
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8
#Step 3
def test_diameter_change_diameter():
    c = C(10)
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8

    c.diameter = 4 #fails because we have defined a getter but not a setter
    c.radius == 2
    c.diameter == 4
#Step 4
def test_area():
    c = C(2)
    assert math.isclose(c.area,12.56637,rel_tol = 1e-7)

def test_no_area_set():
    c = C(2)
    assert math.isclose(c.area,12.56637,rel_tol = 1e-7)
    with pytest.raises(AttributeError):
        c.area = 20

# def test_area_settable():
#     c = C(1)
#     c.area = 10
#     assert c.radius == 5

#Step 5
def test_from_diameter_type():
    c = C.from_diameter(10)
    assert isinstance(c,C)

def test_init_diameter():
    c = C.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5

def test_sphere():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_area():
    s = Sphere(5)

    assert math.isclose(314.16,s.area,rel_tol=1e5)

def test_sphere_from_diamter_type():
    s = Sphere.from_diameter(10)
    c = C.from_diameter(10)
    assert isinstance(s, Sphere)
    assert isinstance(s, C)
    
def test_static_class():
    assert C.something() == "this worked"

def test_add():
    c1 = C(2)
    c2 = C(4)
    assert c1+c2 == 6

def test_mult():
    c1 = C(2)
    c2 = C(4)
    assert c1*2 == 4
    assert c2*4 == 16

def test_less_greater_than():
    c1 = C(2)
    c2 = C(4)
    assert c1 < c2
    assert not c1 > c2
    assert not c2 < c1
    assert c2 > c1

def test_sort():
    circles_unsorted = [C(3),C(1),C(2)]
    circles_sorted = [C(3),C(1),C(2)]
    circles_sorted.sort()
    assert circles_sorted[0].radius == circles_unsorted[1].radius
    assert circles_sorted[1].radius == circles_unsorted[2].radius
    assert circles_sorted[2].radius == circles_unsorted[0].radius

def test_sphere_vol():
    s = Sphere(5)
    assert math.isclose(523.6,s.volume,rel_tol=1e1)
    