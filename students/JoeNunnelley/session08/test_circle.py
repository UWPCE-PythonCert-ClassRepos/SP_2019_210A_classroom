#! /usr/bin/env python3

import math
import pytest
from circle import Circle, Sphere

"""
Step 1:

Create class called Circle – it’s signature should look like:

c = Circle(the_radius)

The radius is a required parameter (can’t have a circle without one!)

The resulting circle should have an attribute for the radius:

c.radius

So you can do:

>> c = Circle(4)
>> print(c.radius)
4

Remember: tests first!
"""
def test_basic_circle_radius():
    the_radius = 4
    circle = Circle(the_radius)
    assert circle.radius == the_radius


def test_circle_with_no_radius():
    with pytest.raises(TypeError):
        circle = Circle()


"""
Step 2:

Add a “diameter” property, so the user can get the diameter
of the circle:

>> c = Circle(4)
>> print(c.diameter)
8
"""
def test_basic_circle_diameter():
    the_radius = 4
    circle = Circle(the_radius)
    assert circle.diameter == the_radius * 2


"""
Step 3:

Set up the diameter property so that the user can set the diameter
of the circle:

>> c = Circle(4)
>> c.diameter = 2
>> print c.diameter
2
>> print c.radius
1

NOTE that the radius has changed!

Important: Do not store both the radius and the diameter as attributes!
If you do that, they could get out of sync. So store only one (the
radius), and have the other calculated “on the fly” by the property.
"""
def test_diameter_changing():
    the_diameter = 2
    the_radius = 4
    circle = Circle(the_radius)
    assert circle.diameter == 8
    circle.diameter = the_diameter
    assert circle.diameter == 2
    assert circle.radius == 1


"""
Step 4:

Add an area property so the user can get the area of the circle:

>> c = Circle(2)
>> print(c.area)
12.566370

(pi can be found in the math module).

The user should not be able to set the area:

>> c = Circle(2)
>> c.area = 42
AttributeError
"""
def test_area_of_circle():
    circle = Circle(2)
    assert math.isclose(circle.area, 12.566370, rel_tol=1e-7)

    with pytest.raises(AttributeError):
        circle.area = 42


"""
Step 5:

NOTE: wait on this one ‘till we learn about class methods..

Add an “alternate constructor” that lets the user create a
Circle directly with the diameter:

>> c = Circle.from_diameter(8)
>> print(c.diameter)
8
>> print(c.radius)
4
"""
def test_alternate_constructor_diameter():
    the_diameter = 8
    circle = Circle.from_diameter(the_diameter)
    assert circle.diameter == the_diameter
    assert circle.radius == the_diameter / 2


"""
Step 6:

Every class should have a nice way to print it out…

Add __str__ and __repr__ methods to your Circle class.

Now you can print it:

In [2]: c = Circle(4)

In [3]: print(c)
Circle with radius: 4.000000

In [4]: repr(c)
Out[4]: 'Circle(4)'

In [5]: d = eval(repr(c))

In [6]: d
Out[6]: Circle(4)
"""
def test_validate_printing():
    circle = Circle(4)
    print(circle)
    repr(circle)
    dircle = eval(repr(circle))
    assert isinstance(dircle, Circle)
    assert dircle.radius == 4


"""
Step 7:

Add some of the numeric protocol to your Circle:

You should be able to add two circles:

In [7]: c1 = Circle(2)

In [8]: c2 = Circle(4)

In [9]: c1 + c2
Out[9]: Circle(6)

and multiply one by a number:

In [16]: c2 * 3
Out[16]: Circle(12)

(what happens with 3 * c2 ? – can you fix that?)
"""
def test_adding_circles():
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle3 = circle1 + circle2
    assert circle3.radius == 6
    circle4 = circle2 * 3
    assert circle4.radius == 12

def test_rightward_additive_operations_on_circles():
    circle2 = Circle(4)
    circle5 = 3 * circle2
    assert circle5.radius == 12

    circle5 = 40 + circle2
    assert circle5.radius == 44

    circle5 = 2 ** circle2
    assert circle5.radius == 16

"""
Step 8:

Add the ability to compare two circles:

In [10]: c1 > c2
Out[10]: False

In [11]: c1 < c2
Out[11]: True

In [12]: c1 == c2
Out[12]: False

In [13]: c3 = Circle(4)

In [14]: c2 == c3
Out[14]: True

Once the comparing is done, you should be able to sort a
list of circles:

In [18]: print circles
[Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

In [19]: circles.sort()

In [20]: print circles
[Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

NOTE: make sure to write unit tests for all of this!
Ideally before writing the code.

Step 8: Optional Features:

    See if you can make “reflected” numerics do the right thing:

a_circle * 3 == 3 * a_circle

    What else makes sense: division? others?
    Add the “augmented assignment” operators, where they make sense:

a_circle += another_circle

a_circle *= 2

    Look through all the “magic methods” and see what makes sense
    for circles.
"""
def test_basic_math_operations():
    assert Circle(10) == Circle(5) + Circle(5)
    assert Circle(10) == Circle(15) - Circle(5)
    assert Circle(20) == Circle(5) * Circle(4)
    assert Circle(20) == Circle(100) / Circle(5)
    assert Circle(2) == Circle(22) // Circle(10)
    assert Circle(2) == Circle(22) % Circle(10)
    assert Circle(100) == Circle(10) ** Circle(2)

def test_comparison_operations():
    assert Circle(4) == Circle(4)
    assert Circle(5) != Circle(4)
    assert Circle(4) < Circle(5)
    assert Circle(5) <= Circle(5)
    assert Circle(6) > Circle(5)
    assert Circle(6) >= Circle(5)

def test_assignment_operators():
    circle1 = Circle(10)
    circle1 += Circle(10)
    assert circle1 == Circle(20)

    circle1 = Circle(10)
    circle1 -= Circle(5)
    assert circle1 == Circle(5)

    circle1 = Circle(10)
    circle1 *= Circle(2)
    assert circle1 == Circle(20)

    c1 = Circle(10)
    c1 /= Circle(2)
    assert c1 == Circle(5)

    circle1 = Circle(21)
    circle1 //= Circle(2)
    assert circle1 == Circle(10)

    circle1 = Circle(21)
    circle1 %= Circle(2)
    assert circle1 == Circle(1)

    circle1 = Circle(2)
    circle1 **= Circle(2)
    assert circle1 == Circle(4)

def test_circle_sorting():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4),
               Circle(0), Circle(2), Circle(3), Circle(5),
               Circle(9), Circle(1)]
    circles.sort()
    assert circles[0].radius == 0


def test_reflected_numeric_operations():
    circle2 = Circle(2)
    assert circle2 * 4 == 4 * circle2
    assert circle2 + 5 == 5 + circle2
    # this power operation seems questionable mathematically but it works.
    assert circle2 ** 3 == 3 ** circle2

"""
Step 9: Subclassing!

You’ve got a circle already – what if you needed a Sphere?
They have a fair bit in common – both defined by a radius,
same relationship of radius to diameter, etc.

So we can get a pretty useful Sphere class by simply subclassing
Circle, and adding and changing a couple things.

    Create a Sphere Class that subclasses Circle.
    Override the __str__ and __repr__ methods to be appropriate
    for Spheres.
    Create a volume property that returns the volume (hint: volume
    of a sphere is: 4/3 pi r^3).
    Override the area property so that it either computes the
    surface
    area of a sphere (what’s the formula for that???), or have
    it raise an exception: maybe NotImplementedError.

Make sure to write some tests – maybe ahead of time! – that confirm
that all this works. And the other things like addition, and
sorting…

Check that the Sphere.from_diameter() alternate constructor actually
creates a Sphere! (you DO NOT have to write a new classmethod for
that!) – pretty cool, eh?
"""

def test_sphere():
    sphere = Sphere(5)

    with pytest.raises(AttributeError):
        sphere.area


def test_sphere_from_diameter_type():
    sphere = Sphere.from_diameter(5)
    assert sphere.radius == 2.5
    assert sphere.diameter == 5


def test_sphere_volume():
    radius = 20
    sphere = Sphere(radius)
    expected_volume = ((4.0/3.0 * math.pi) * (radius ** 3))
    assert sphere.volume == expected_volume
    assert sphere.radius == radius

def test_basic_math_operations_sphere():
    assert Sphere(10) == Sphere(5) + Sphere(5)
    assert Sphere(10) == Sphere(15) - Sphere(5)
    assert Sphere(20) == Sphere(5) * Sphere(4)
    assert Sphere(20) == Sphere(100) / Sphere(5)
    assert Sphere(2) == Sphere(22) // Sphere(10)
    assert Sphere(2) == Sphere(22) % Sphere(10)
    assert Sphere(100) == Sphere(10) ** Sphere(2)

def test_comparison_operations_sphere():
    assert Sphere(4) == Sphere(4)
    assert Sphere(5) != Sphere(4)
    assert Sphere(4) < Sphere(5)
    assert Sphere(5) <= Sphere(5)
    assert Sphere(6) > Sphere(5)
    assert Sphere(6) >= Sphere(5)

def test_assignment_operators_sphere():
    sphere = Sphere(10)
    sphere += Sphere(10)
    assert sphere == Sphere(20)

    sphere = Sphere(10)
    sphere -= Sphere(5)
    assert sphere == Sphere(5)

    sphere = Sphere(10)
    sphere *= Sphere(2)
    assert sphere == Sphere(20)

    sphere = Sphere(10)
    sphere /= Sphere(2)
    assert sphere == Sphere(5)

    sphere = Sphere(21)
    sphere //= Sphere(2)
    assert sphere == Sphere(10)

    sphere = Sphere(21)
    sphere %= Sphere(2)
    assert sphere == Sphere(1)

    sphere = Sphere(2)
    sphere **= Sphere(2)
    assert sphere == Sphere(4)

def test_sphere_sorting():
    spheres = [Sphere(6), Sphere(7), Sphere(8),
               Sphere(4), Sphere(0), Sphere(2), Sphere(3),
               Sphere(5), Sphere(9), Sphere(1)]
    spheres.sort()
    assert spheres[0].radius == 0
