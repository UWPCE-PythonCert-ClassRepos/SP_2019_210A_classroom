from circle_clas import *
import math


def test_radius():
    a = Circle(9)
    b = Circle(1)
    c = Circle(4)

    print(a.radius)
    print(b.radius)
    print(c.radius)

    assert a.radius == 9
    assert b.radius == 1
    assert c.radius == 4


def test_diameter():
    a = Circle(9)
    b = Circle(1)
    c = Circle(4)

    print(a.diameter)
    print(b.diameter)
    print(c.diameter)

    assert a.diameter == 18
    assert b.diameter == 2
    assert c.diameter == 8


def test_diameter2():
    d = Circle(3)
    d.diameter = 3

    print(d.diameter)
    print(d.radius)

    assert d.diameter == 3
    assert d.radius == 1.5

    e = Circle(2400)
    e.diameter = 90

    print(e.diameter)
    print(e.radius)

    assert e.diameter == 90
    assert e.radius == 45


def test_area():
    a = Circle(69)
    assert a.area == math.pi * a.radius * a.radius
    assert a.area == math.pi * a.radius * (a.diameter/2)
    assert a.area == math.pi * (a.diameter/2) * (a.diameter/2)


def test_cls_mth_di():
    a = Circle.from_diameter(12)

    print(a.radius)
    print(a.diameter)

    assert a.radius == 6
    assert a.diameter == 12


def test_str():
    a = Circle(4)
    print(a)
    assert a.__str__() == 'Circle with radius: 4'

    b = Circle(69)
    print(b)
    assert b.__str__() == 'Circle with radius: 69'


def test_repr():
    a = Circle(11)
    print(repr(a))
    assert a.__repr__() == 'Circle(11)'


def test_add():
    a = Circle(10)
    b = Circle(12)
    print(a+b)
    assert a+b == 22


def test_mult():
    a = Circle(7)
    assert a * 3 == 21


def test_lt():
    a = Circle(9)
    b = Circle(1)
    assert b < a


def test_gt():
    a = Circle(9)
    b = Circle(1)
    assert a > b


def test_eq():
    a = Circle(1)
    b = Circle(1)
    assert a == b


def test_sort():
    a = [Circle(7), Circle(4), Circle(1), Circle(2)]
    print(a)
    a.sort()
    print(a)
    assert a == [Circle(1), Circle(2), Circle(4), Circle(7)]

