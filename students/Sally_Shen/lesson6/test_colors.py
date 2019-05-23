'''
tests for color module
'''

import pytest
from colors import colors
from colors import colors2


def test_defaults():
    result = colors()

    assert result == ('black', 'red', 'blue', 'pink')

def test_all_sets():
    '''
    test that it works if you pass in all four paramenters as positional argusments
    '''
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_all_twokeyword():
    '''
    test that it works if you pass in all four paramenters as positional argusments
    '''
    result = colors(link_color='red', back_color='blue')

    assert result == ('black', 'blue', 'red', 'pink')


def test_combine():
    '''
    test that it works if you pass in all four paramenters as positional argusments
    '''
    result = colors('purple', link_color='red', back_color='blue')
    assert result == ('purple', 'blue', 'red', 'pink')


def test_dict_params():
    colors_dict = {"fore_color": 'purple',
                    "back_color": 'green',
                    "link_color": 'red',
                    "visited_color": 'magenta'}

    result = colors(*colors_dict.values())
    assert result == ('purple', 'green', 'red', 'magenta')


def test_tup_params():
    colors_tuple = ('purple', 'green', 'red', 'magenta')

    result = colors(*colors_tuple)

    assert result == ('purple', 'green', 'red', 'magenta')


def test_dict_tup_params():
   # colors_dict = {"fore_color": 'purple', "link_color": 'red'}

    colors_dict = {"link_color": 'red', "visited_color": 'magenta'}


#with pytest.raises(TypeError):
    result = colors('blue', **colors_dict)

    assert result == ('blue', 'red', 'red', 'magenta')


def test_args_kwags():
    print("**********This test was RUN**********")
    result = colors2('purple', link_color = 'red', back_color = 'blue')

    assert result == (('purple',), {'link_color': 'red', 'back_color': 'blue'})