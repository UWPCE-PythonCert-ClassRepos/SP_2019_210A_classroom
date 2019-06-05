from circle_clas import *
import math


def test_radius():
    a = Sphere(9)
    b = Sphere(1)
    c = Sphere(4)

    print(a.radius)
    print(b.radius)
    print(c.radius)

    assert a.radius == 9
    assert b.radius == 1
    assert c.radius == 4


def test_diameter():
    a = Sphere(9)
    b = Sphere(1)
    c = Sphere(4)

    print(a.diameter)
    print(b.diameter)
    print(c.diameter)

    assert a.diameter == 18
    assert b.diameter == 2
    assert c.diameter == 8


def test_diameter2():
    d = Sphere(3)
    d.diameter = 3

    print(d.diameter)
    print(d.radius)

    assert d.diameter == 3
    assert d.radius == 1.5

    e = Sphere(2400)
    e.diameter = 90

    print(e.diameter)
    print(e.radius)

    assert e.diameter == 90
    assert e.radius == 45


def test_area():  # needs work!!
    a = Sphere(69)
    assert a.area == 4 * math.pi * a.radius * a.radius
    assert a.area == 4 * math.pi * a.radius * (a.diameter/2)
    assert a.area == 4 * math.pi * (a.diameter/2) * (a.diameter/2)


def test_cls_mth_di():
    a = Sphere.from_diameter(12)

    print(a.radius)
    print(a.diameter)

    assert a.radius == 6
    assert a.diameter == 12


def test_str():
    a = Sphere(4)
    print(a)
    assert a.__str__() == 'Sphere with radius: 4'

    b = Sphere(69)
    print(b)
    assert b.__str__() == 'Sphere with radius: 69'


def test_repr():
    a = Sphere(11)
    print(repr(a))
    assert a.__repr__() == 'Sphere(11)'


def test_add():
    a = Sphere(10)
    b = Sphere(12)
    print(a+b)
    assert a+b == 22


def test_mult():
    a = Sphere(7)
    assert a * 3 == 21


def test_lt():
    a = Sphere(9)
    b = Sphere(1)
    assert b < a


def test_gt():
    a = Sphere(9)
    b = Sphere(1)
    assert a > b


def test_eq():
    a = Sphere(1)
    b = Sphere(1)
    assert a == b


def test_sort():
    a = [Sphere(7), Sphere(4), Sphere(1), Sphere(2)]
    print(a)
    a.sort()
    print(a)
    assert a == [Sphere(1), Sphere(2), Sphere(4), Sphere(7)]


def test_vol():
    a = Sphere(33)
    assert a.volume() == math.pi * (4/3) * a.radius**3


