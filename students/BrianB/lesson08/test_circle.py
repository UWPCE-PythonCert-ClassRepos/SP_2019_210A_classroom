#!usr/bin/env python3
from circle import Circle, Sphere
from math import isclose, pi


def test_radius():
    """
    takes a circle with set radius and tests
    its radius value is correct
    :return:
    """
    c = Circle(5)
    assert c.radius == 5


def test_diameter():
    """
    takes a circle with set radius and tests
    calculation of its diameter
    :return: None
    """
    c = Circle(7)
    assert c.diameter == 14


def test_set_diameter():
    """
    takes a circle with set radius and tests
    calculation of the diameter, changes the
    diameter and tests calculation of the new
    diameter
    :return: None
    """
    c = Circle(7)
    assert c.diameter == 14
    c.diameter = 10
    assert c.diameter == 10


def test_change_radius_diameter():
    """
    takes a circle with set radius and changes the diameter.
    test the radius value against the new diameter
    :return: None
    """
    c = Circle(9)
    c.diameter = 50
    assert c.radius == 25


def test_set_area():
    """
    tests the area of a circle then assigns a new area
    and re-tests the new area. This uses the isclose module
    to test the relative tolerance of the radius and diameter,
    separately, to one one-hundredth
    :return: None
    """
    c = Circle(2)
    assert isclose(c.area, (pi * 2**2), rel_tol=.01)
    c.area = 500
    assert isclose(c.area, 500, rel_tol=.01)


def test_change_values_area():
    """
    tests changing the assigned radius of a circle
    by assigning a new area for the circle and testing
    the resultant radius and diameter with the math, isclose
    module.  This isclose module tests the relative tolerance
    of the radius and diameter, separately, to one one-hundredth
    :return: None
    """
    c = Circle(13)
    c.area = 6
    assert isclose(c.radius, 1.38, rel_tol=.01)
    assert isclose(c.diameter, c.radius * 2, rel_tol=.01)


def test_from_diameter():
    """
    tests calculating the correct circle radius when
    given a circle's diameter
    :return: None
    """
    c = Circle.from_diameter(16)
    assert c.diameter == 16
    assert c.radius == 8


def test_str():
    """
    tests string conversion of the circle's radius as
    well as representing the printable method with
    assigned radius as a string
    :return: None
    """
    c = Circle(15)
    assert str(c) == "Circle with radius: 15.000000"
    assert repr(c) == "Circle(15)"


def test_math():
    """
    tests multiplication and addition of two assigned
    circle radii.  tests reverse multiplication of each
    circles radii
    :return: None
    """
    c1 = Circle(13)
    c2 = Circle(17)
    assert c1 + c2 == "Circle(30)"
    assert c1 * 2 == "Circle(26)"
    assert 2 * c1 == "Circle(26)"
    assert c2 * 3 == "Circle(51)"


def test_relationship():
    """
    tests assigning radii to 2 circles and testing
    whether one is greater than, less than or equal
    to the other.  changes radii for one circle and
    continues testing against the original radius
    :return: None
    """
    c1 = Circle(17)
    c2 = Circle(33)
    print(c1)
    print(c2)
    assert not c1 > c2
    assert c1 < c2
    assert not c1 == c2
    c2 = Circle(18)
    assert c1 < c2
    c2 = Circle(17)
    assert c1 == c2


def test_sort():
    """
    tests adding circle.py results to a list, sorts
    the list and tests teh sort function works properly
    :return: None
    """
    circle_list = [
                   Circle(9),
                   Circle(10),
                   Circle(4),
                   Circle(7),
                   Circle(5),
                   Circle(2),
                   Circle(3),
                   Circle(6),
                   Circle(1),
                   Circle(8),
                   ]

    circle_list.sort()
    assert circle_list == [
                           Circle(1),
                           Circle(2),
                           Circle(3),
                           Circle(4),
                           Circle(5),
                           Circle(6),
                           Circle(7),
                           Circle(8),
                           Circle(9),
                           Circle(10),
                           ]


def test_sphere():
    """
    tests sphere area and volume to a relative tolerance
    to one one-hundredth. tests ability to change sphere
    volume and calculate correct resulting volume and radius.
    :return: None
    """
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
