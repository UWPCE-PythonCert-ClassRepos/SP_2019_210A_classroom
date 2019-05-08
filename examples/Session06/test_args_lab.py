"""
tests for args_lab
"""

import pytest

from args_lab import colors, colors2


def test_pos():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    print(result)
    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_key():
    result = colors(link_color='red', back_color='blue')

    print(result)
    assert result == ('red', 'blue', 'red', 'lavender')


def test_pos_key():
    result = colors('purple', link_color='red', back_color='blue')

    print(result)
    assert result == ('purple', 'blue', 'red', 'lavender')


def test_pos_key_error():
    with pytest.raises(TypeError):
        result = colors('purple', link_color='red', fore_color='blue')


def test_defaults():
    result = colors()
    assert result == ('red', 'blue', 'green', 'lavender')


def test_defaults_empty():
    result = colors("")
    assert result == ('', 'blue', 'green', 'lavender')


def test_dict():
    cols = dict(fore_color="pink",
                back_color='yellow',
                link_color='green',
                visited_color='lavender'
                )
    print(cols)
    result = colors(**cols)

    assert result == ('pink', 'yellow', 'green', 'lavender')

def test_dict2():
    cols = dict(fore_color="pink",
                back_color='yellow',
                )
    print(cols)
    result = colors(**cols)

    assert result == ('pink', 'yellow', 'green', 'lavender')

def test_tuple():
    cols = ("pink",
            'yellow',
            'green',
            'lavender'
            )
    print(cols)
    result = colors(*cols)

    assert result == ('pink', 'yellow', 'green', 'lavender')


def test_dict():
    cols = dict(#fore_color="pink",
                #back_color='yellow',
                link_color='green',
                visited_color='lavender'
                )
    cols_t = ('green',
              'lavender'
              )

    print(cols)
    result = colors(*cols_t, **cols)

    assert result == ('green', 'lavender', 'green', 'lavender')


def test_cols2_pos():
    args, kwargs = colors2('green', 'lavender')

    assert args == ('green', 'lavender')
    assert kwargs == {}


def test_cols2_pos2():
    args, kwargs = colors2('green', fred='lavender')

    assert args == ('green',)
    assert kwargs == {'fred': 'lavender'}
