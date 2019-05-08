import pytest
from fraction import Fraction


def test_fraction_init():
    Fraction(1, 2)
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)
    with pytest.raises(TypeError):
        Fraction(1.5, 2.0)


def test_fraction_str():
    assert str(Fraction(1, 2)) == '1/2'


def test_fraction_eq():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(2, 3) != Fraction(3, 4)


def test_fraction_lt():
    assert Fraction(1, 2) < Fraction(2, 3)


def test_fraction_add():
    assert Fraction(1, 2) + Fraction(2, 3) == Fraction(7, 6)
    assert str(Fraction(1, 3) + Fraction(1, 6)) == '1/2'
