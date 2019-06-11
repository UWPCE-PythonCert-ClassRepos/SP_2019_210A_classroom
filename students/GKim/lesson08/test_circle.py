import pytest, math
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
    assert math.isclose(c.area,12.566370, rel_tol = 1e-7)

def test_set_area():
    c = Circle(5)
    with pytest.raises(AttributeError):
        c.area = 20

def test_from_diameter_type():
    c = Circle.from_diameter(10)
    assert isinstance(c, Circle)

def test_init_diameter():
    c = Circle.from_diameter(10)

    assert c.diameter == 10
    assert c.radius == 5


def test_str():
    c = Circle(5)

    assert str(c) == "Circle with radius: 5"

def test_repr():
    c = Circle(8)

    assert repr(c) == "Circle (8)"

def test_add():
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = c1 + c2

    assert c3.radius == 15

def test_multiplication():
    # c1 = Circle(10)
    assert Circle(10) * 2 == 20


def test_equal():
    c1 = Circle(5)
    c2 = Circle(5.0)
    assert c1 == c2
    
def test_not_equal():
    c1 = Circle(3)
    c2 = Circle(2)

    assert c1 != c2

def test_greater_than():
    c1 = Circle(10)
    c2 = Circle(5)

    assert c1 > c2

def test_less_than():
    c1 = Circle(1)
    c2 = Circle(2)

    assert c1 < c2

def test_sort_circle():

    c_list = [Circle(2), Circle(7), Circle(3)]

    c_list.sort(key=Circle.sort_key)

    assert c_list[1] == Circle(3)
    assert c_list[0] < c_list[1] < c_list[2] 

# Sphere tests 
def test_sphere_area():
    s1 = Sphere(4)

    assert s1.area ==  201.06192982974676


def test_sphere():
    s = Sphere(5)

    assert s.radius == 5
    assert s.diameter == 10

# def test_sphere_area():
#     s = Sphere(5)

#     with pytest.raises(NotImplementedError):
#         s.area

def test_sphere_from_diameter_type():
    s = Sphere.from_diameter(10)
    s.radius == 5
    assert isinstance(s, Sphere)


def test_volume():
    s1 = Sphere(4)

    
    assert s1.volume() == 268.082573106329

def test_sort_sphere():

    s_list = [Sphere(2), Sphere(7), Sphere(3)]

    s_list.sort(key=Sphere.sort_key)

    assert s_list[1] == Sphere(3)
    assert s_list[0] < s_list[1] < s_list[2] 


