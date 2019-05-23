"""
test code for test_args_kwargs
"""
from args_kwargs import color_parameters, color_parameters2

def test_color_parameters():
    result = color_parameters()
    assert result == ('red', 'blue', 'yellow', 'green')

def test_all_sets():
    result = color_parameters(link_color="red", back_color="blue")
    assert result == ('red', 'blue', 'red', 'green')
    

def test_combo():
    result = color_parameters("purple", link_color="red", back_color="blue")
    print("result", result)
    assert result == ("purple", "blue", "red", "green")
    

def test_tup_params():
    colors_tup = ("red", 
                  "blue", 
                  "yellow", 
                  "green")
    result = color_parameters(*colors_tup)
    assert result == ('red', 'blue', 'yellow', 'green')

def test_dict_tup_params():
    colors_dict = {"link_color": "red",
                "visited_color": "magenta"}

    
    result = color_parameters("blue", **colors_dict)
    assert result == ("blue", "blue","red", "magenta")

def test_color_parameters2_empty():
    result = color_parameters2()

    assert result == ((),{})

def test_color_parameters2():

    result = color_parameters2(45, link_color = "red", back_color = "blue")
    assert result == ((45,),{"link_color": "red", "back_color": "blue"})

    # assert False
