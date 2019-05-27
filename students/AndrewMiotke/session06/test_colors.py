"""tests for colors module"""
import pytest
from colors import colors, colors_two

def test_defaults():
    result = colors()

    assert result == ('black', 'red', 'blue', 'purple')


def test_all_set():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_keyword_argument():
    result = colors(link_color='red', back_color='blue')

    assert result == ('black', 'blue', 'red', 'purple')


def test_combo():
    result = colors('purple', link_color='red', back_color='blue')

    assert result == ('purple', 'blue', 'red', 'purple')


def test_dict_parameters():
    colors_dict = {"fore_color": "purple",
                   "back_color": "green",
                   "link_color": "red",
                   "visited_color": "magenta"}

    result = colors(*colors_dict.values())
    assert result == ("purple", "green", "red", "magenta")


def test_tup_parameters():
    colors_tup = ("purple",
                   "green",
                   "red",
                   "magenta")

    result = colors(*colors_tup)
    assert result == ("purple", "green", "red", "magenta")


def test_dict_tup_parameters():
    colors_dict = {"fore_color": "purple",
                   "back_color": "green",
                   "link_color": "red",
                   "visited_color": "magenta"}

    with pytest.raises(TypeError):
        result = colors('blue', **colors_dict)

        assert result == ('purple', 'green', 'red', 'magenta')


def test_args_kwards_empty():
    result = colors_two()

    assert result == ((), {})


def test_args_kwargs():
    result = colors_two('purple', link_color='red', back_color='blue')

    assert result == (('purple',), {'link_color':'red', "back_color":'blue'})