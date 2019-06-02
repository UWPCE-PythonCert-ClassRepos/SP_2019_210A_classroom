#! /usr/bin/env python3

from colors import colors
import pytest

def test_colors():
    assert(colors() == ('black', 'white', 'yellow', 'blue'))

def test_colors_parameterized():
    color = 'blue'
    assert(colors(fore_color=color)[0] == color)

def test_colors_args():
    colrs = ("blue", "red", "red", "yellow")
    assert(colors(*colrs) == colrs)

def test_colors_kwargs():
    colrs = {'fore_color': 'red', 'back_color': 'blue', 'link_color': 'purple', 'visited_color': 'green'}
    assert(colors(**colrs) == tuple(colrs.values()))


def test_colors_typeerror():
    colrs = {'fore_color': 'red', 'back_color': 'blue', 'link_color': 'purple', 'visited_color': 'green'}

    with pytest.raises(TypeError):
        assert(colors('blue', **colrs) == tuple(colrs.values()))


def test_colors_args_kwargs():
    colrs = {'link_color': 'red', 'back_color': 'blue', 'visited_color': 'green'}
    colr = 'yellow'
    assert(colors(colr, **colrs) == ('yellow', 'blue', 'red', 'green'))


def test_colors_args_kwargs_tup():
    colrs = {'link_color': 'red', 'back_color': 'blue', 'visited_color': 'green'}
    colr = ('yellow')
    assert(colors(colr, **colrs) == ('yellow', 'blue', 'red', 'green'))