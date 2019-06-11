"""
tests for color module
"""
import pytest
from color import color, color2

def test_defaults():
    result = color()
    assert result == ('a', 'b', 'c')


def test_all_set():
    result = color('c', 'b', 'a')
    #assert result == ('a', 'b', 'c')


def test_tup_params():
    dic = {"a":'a', "c": 'c'}
    with pytest.raises(TypeError):
        result = color('a', **dic)
        assert result == ('a', 'b', 'c')

def test_args_kwargs():
    result = color2('apple', 'banana')
    print(result)
