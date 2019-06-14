# Dev: Miguel Rovira-Gonzalez
# Lesson08: Circle Assignment

import pytest
import math
from circle_class import Circle, Sphere


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
    assert c.diameter == 20
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


def test_area():
    c = Circle(2)
    assert math.isclose(c.area, 12.566370, rel_tol=1e-7)


def test_str():
    c = Circle(20)
    assert str(c) == "Circle with radius: 20"


def test_rep():
    c = Circle(10)
    assert repr(c) == "Circle10"


def test_set_area():
    c = Circle(5)
    with pytest.raises(AttributeError):
        c.area = 20


def test_add_circle():
    c1 = Circle(10)
    c2 = Circle(20)
    assert c1 + c2 == 30


def test_multiply_circle():
    c1 = Circle(10)
    assert c1 * 5 == 50


def test_left_operand_multi():
    c1 = Circle(10)
    assert 2 * c1 == 20


def test_greater_than():
    c1 = Circle(30)
    c2 = Circle(20)
    assert c1 > c2


def test_less_than():
    c1 = Circle(30)
    c2 = Circle(40)
    assert c1 < c2


def test_equality():
    c1 = Circle(10)
    c2 = Circle(10)
    with pytest.raises(AssertionError):
        assert c1 is c2


def test_instance_equality():
    c1 = Circle(10)
    c2 = c1
    assert c1 == c2


def test_sort():
    circle_list = [Circle(20), Circle(10), Circle(15), Circle(5)]
    circle_list.sort(key=Circle.sort_key)
    assert circle_list[0] == Circle(5)
    assert circle_list[0] < circle_list[1] < circle_list[2] < circle_list[3]


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
    with pytest.raises(AttributeError):
        s.area


def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(10)
    s.radius == 5
    assert isinstance(s, Sphere)


def test_add_sphere():
    c1 = Sphere(10)
    c2 = Sphere(20)
    assert c1 + c2 == 30


def test_sort_sphere():
    sphere_list = [Sphere(20), Sphere(10), Sphere(15), Sphere(5)]
    sphere_list.sort(key=Sphere.sort_key)
    assert sphere_list[0] == Sphere(5)
    assert sphere_list[0] < sphere_list[1] < sphere_list[2] < sphere_list[3]


def test_sphere_volume():
    s = Sphere(4)
    assert s.volume() == 268.082573106329
