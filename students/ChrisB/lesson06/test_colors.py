"""
tests for the colors module
"""
import pytest

from colors import colors, colors2


def test_defaults():
    result = colors()

    assert result == ('black','red','blue','pink')


def test_all_set():
    """
    test that it works if you pass in all four parameters as
    positional arguments
    """

    result = colors('red', 'blue', 'yellow', 'chartreuse')
    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_all_two_keywords():
    """
    test that it works if you pass in all four parameters as
    positional arguments
    """

    result = colors(link_color='red', back_color='blue')
    assert result == ('black', 'blue', 'red', 'pink')


def test_combo():
    result = colors('purple', link_color='red', back_color='blue')

    print("result:", result)
    assert result == ('purple', 'blue', 'red', 'pink')


def test_dict_params():
    colors_dict = {"fore_color": 'purple',
                   "link_color": 'red',
                   "back_color": 'green',
                   "visited_color": 'magenta'}

    result = colors(**colors_dict)

    assert result == ('purple', 'green', 'red', 'magenta')


def test_tup_params():
    colors_tup = ('purple',
                  'green',
                  'red',
                  'magenta')

    result = colors(*colors_tup)

    assert result == ('purple', 'green', 'red', 'magenta')


def test_dict_duplicate_param():
    colors_dict = {"fore_color": 'purple',
                   "link_color": 'red'}
    #                   "back_color": 'green',
    #               "visited_color": 'magenta'}

    with pytest.raises(TypeError):
        result = colors('blue', **colors_dict)



def test_dict_tup_params():
    colors_dict = {#"fore_color": 'purple',
                   "link_color": 'red',
    #              "back_color": 'green',
                   "visited_color": 'magenta',
                   }

    result = colors('blue', **colors_dict)

    assert result == ('blue', 'red', 'red', 'magenta')


def test_args_kwargs_empty():
    result = colors2()

    assert result == ((), {})


def test_args_kwargs():
    result = colors2(link_color='red', back_color='blue')

    assert result == ((), {'link_color': 'red',
                                    'back_color': 'blue'})


