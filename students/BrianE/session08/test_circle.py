from circle import Circle, Sphere
import pytest
import math


def test_circle_init():
    """ Verify circle init functions properly """
    a_circle = Circle(5)
    assert isinstance(a_circle, Circle)
    assert a_circle.radius == 5


def test_circle_diameter():
    """ Verify circle diameter is set to 2x radius """
    a_circle = Circle(5)
    assert a_circle.diameter == 5 * 2


def test_circle_diameter_radius_sync():
    """ Verify updating diameter and radius maintain sync when updating either value """
    a_circle = Circle(5)

    # changing diameter results in updated radius
    a_circle.diameter = 20
    assert a_circle.radius == 10

    # changing radius results in updated diameter
    a_circle.radius = 7
    assert a_circle.diameter == 14


def test_circle_area_calculation():
    """ Verify circle area calculation """
    a_circle = Circle(5)
    assert a_circle.area == math.pi * 5 ** 2


def test_circle_area_set():
    """ Verify circle area cannot be set by user """
    a_circle = Circle(5)
    with pytest.raises(AttributeError):
        a_circle.area = 25


def test_circle_str():
    """ Verify circle __str__ output """
    radius = 5
    a_circle = Circle(radius)
    assert a_circle.__str__() == f"Circle with radius: {radius}"


def test_circle_repr():
    """ Verify circle __repr__ output """
    a_circle = Circle(5)
    assert a_circle.__repr__() == f"Circle(5)"


def test_circle_add():
    """ Verify adding two circles together functions properly """
    a_circle = Circle(5)
    b_circle = Circle(8)
    c_circle = a_circle + b_circle
    assert isinstance(c_circle, Circle)
    assert c_circle.radius == 13


def test_circle_radd():
    """ Verify adding an integer value to a circle's radius """
    a_circle = Circle(5)
    assert 3 + a_circle == Circle(8)


def test_circle_multiply():
    """ Verify multiplying a circle functions properly """
    a_circle = Circle(5)
    b_circle = a_circle * 2
    assert b_circle.radius == 10
    assert a_circle * b_circle == Circle(50)


def test_circle_rmul():
    """ Verify multiplying an integer value to a circle's radius """
    a_circle = Circle(5)
    assert 3 * a_circle == Circle(15)


def test_circle_compare_greater_than():
    """ Verify greater than comparison of two circles """
    a_circle = Circle(5)
    b_circle = Circle(6)
    assert b_circle > a_circle
    with pytest.raises(AssertionError):
        assert a_circle >= b_circle


def test_circle_compare_less_than():
    """ Verify less than comparison of two circles """
    a_circle = Circle(5)
    b_circle = Circle(6)
    assert a_circle < b_circle
    with pytest.raises(AssertionError):
        assert b_circle <= a_circle


def test_circle_compare_equal_to():
    """ Verify equal to (==) comparison of two circles """
    a_circle = Circle(5)
    b_circle = Circle(5)
    c_circle = Circle(6)
    assert a_circle == a_circle
    assert a_circle == b_circle
    with pytest.raises(AssertionError):
        assert c_circle <= a_circle


def test_circle_compare_less_than_or_equal():
    """ Verify less than or equal to (<=) comparison of two circles """
    a_circle = Circle(5)
    b_circle = Circle(5)
    c_circle = Circle(6)
    assert a_circle <= b_circle
    assert a_circle <= c_circle
    with pytest.raises(AssertionError):
        assert c_circle <= a_circle


def test_circle_compare_greater_than_or_equal():
    """ Verify greater than or equal to (>=) comparison of two circles """
    a_circle = Circle(5)
    b_circle = Circle(5)
    c_circle = Circle(6)
    assert a_circle >= b_circle
    assert c_circle >= a_circle
    with pytest.raises(AssertionError):
        assert a_circle >= c_circle


def test_circle_init_by_diameter():
    """ Verify a circle can be initialized using a diameter """
    a_circle = Circle.from_diameter(10)
    assert a_circle.radius == 5


def test_sphere_str():
    """ Verify sphere __str__ output """
    radius = 5
    a_sphere = Sphere(radius)
    assert a_sphere.__str__() == f"Sphere with radius: {radius}"


def test_sphere_repr():
    """ Verify sphere __repr__ output """
    a_sphere = Sphere(5)
    assert a_sphere.__repr__() == f"Sphere(5)"


def test_sphere_volume_calculation():
    """ Verify volume calculation is correct """
    a_sphere = Sphere(5)
    assert a_sphere.volume == 523.5987755982989


def test_sphere_volume_sync_after_radius_update():
    """ Verify volume maintains sync when radius is updated """
    a_sphere = Sphere(5)
    assert a_sphere.volume == 523.5987755982989
    a_sphere.radius = 6
    assert a_sphere.volume == 904.7786842338603


def test_sphere_area_calculation():
    """ Verify surface area calculation is correct """
    a_sphere = Sphere(5)
    assert a_sphere.area == 314.1592653589793


def test_sphere_area_sync_after_radius_update():
    """ Verify volume maintains sync when radius is updated """
    a_sphere = Sphere(5)
    assert a_sphere.area == 314.1592653589793
    a_sphere.radius = 6
    assert a_sphere.area == 452.3893421169302


def test_sphere_init_by_diameter():
    """ Verify a sphere can be initialized using a diameter """
    a_sphere = Sphere.from_diameter(20)
    assert a_sphere.radius == 10
    assert a_sphere.volume == 4188.790204786391
    assert isinstance(a_sphere, Sphere)


def test_sphere_volume_set():
    """ Verify sphere volume cannot be set by user """
    a_sphere = Sphere(5)
    with pytest.raises(AttributeError):
        a_sphere.area = 25
