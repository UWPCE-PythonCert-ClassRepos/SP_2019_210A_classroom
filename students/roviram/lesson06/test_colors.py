"""
Tests for the color module
"""
import pytest
from colors import colors, colors2


def test_defaults():
    result = colors()
    assert result == ('black', 'red', 'blue', 'pink')


def test_all_set():
    """
    Test that it works if you pass in all four parameters as positional arguments
    :return:
    """
    result = colors('red', 'blue', 'yellow', 'chartreuse')
    assert result == ('red', 'blue', 'yellow', 'chartreuse')


def test_all_two_keywords():
    result = colors(link_color='red', back_color='blue')
    assert result == ('black', 'blue', 'red', 'pink')


def test_combo():
    result = colors('purple', link_color='red', back_color='blue')
    print("Results: ", result)
    assert result == ('purple', 'blue', 'red', 'pink')
    # assert False
    print("test_combo passed")


def test_dict_params():
    colors_dict = {"fore_color": "Purple",
                   "back_color": "Green",
                   "link_color": "Red",
                   "visited_color": "Magenta"}
    result = colors(**colors_dict)
    assert result == ("Purple", "Green", "Red", "Magenta")


def test_tup_params():
    colors_dict = ("Purple",
                   "Green",
                   "Red",
                   "Magenta")
    result = colors(*colors_dict)
    assert result == ("Purple", "Green", "Red", "Magenta")


def test_dict_tupe_params():
    colors_dict = {# "fore_color": "Purple",
                    "link_color": "Red",
                    "visited_color": "Magenta"
                   }

    with pytest.raises(TypeError):
        result = colors("blue", **colors_dict)

    assert result == ("Blue", "Red", "Red", "Magenta")


def test_args_kwargs_empty():
    result = colors2()
    assert result == ((), {})


def test_args_kwargs():
    result = colors2("Purple", link_color="Red", back_color="Blue")
    assert result == ((45, ), {"Link_Color": "Red",
                               "Back_Color": "Blue"})






