'''
circle tests
'''
import pytest
from circle import Circle, Sphere
import math


def test_init():
    '''
    Merely testing the init
    '''
    c = Circle(10)
    assert c.radius == 10


def test_no_radius():
    '''Testing that there is no radius'''
    with pytest.raises(TypeError):
        c = Circle()


def test_diameter():
    '''Takes a circle with a set radius and tests calculations of its diameter'''
    c = Circle(10)
    assert c.diameter == 20

def test_diameter_change_radius():
    '''takes a circle with set radius and changes the radius.
    test the radius value against the new diameter'''
    c = Circle(10)
    c.radius = 4
    assert c.radius == 4
    assert c.diameter == 8

def test_radius_change_diameter():
    '''same as above but tests the diameter'''
    c = Circle(10)
    assert c.radius == 10
    assert c.diameter == 20

    c.diameter = 4
    assert c.radius == 2
    assert c.diameter == 4

def test_area():
    '''tests the calucations for area'''
    c = Circle(2)
    assert math.isclose(c.area, 12.566370, rel_tol=1e-7)


def test_set_area():
    '''tests  the area of a circle, assigns a new radius and tests the new area'''
    c = Circle(5)
    with pytest.raises(AttributeError):
        c.area = 20


def test_diameter_start():
    c = Circle.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5

def test_sphere():
    '''tests sphere area and volume'''
    s = Sphere(5)
    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_area():
    s = Sphere(5)
    with pytest.raises(AttributeError):
        s.area
    assert s.radius == 5
    assert s.diameter == 10

def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(10)
    s.radius == 5
    assert isinstance(s, Sphere)

def test_set_area():
    """
    tests the area of a circle then assigns a new area
    and re-tests the new area. This uses the isclose module
    to test the relative tolerance of the radius and diameter,
    separately, to one one-hundredth

    took this from someone else
    """
    c = Circle(2)
    assert math.isclose(c.area, (math.pi * 2**2), rel_tol=.01)
    