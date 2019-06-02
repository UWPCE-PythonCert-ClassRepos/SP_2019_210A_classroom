"""
We are going to do this as test driven development: Your first task for each step below is to write a
test that will ensure your code does whatvwe are telling you it should do.

Keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)

Call it with a couple different parameters set. That is, write tests that verify that all of the 
following work as advertised:

Using just positional arguments:
func('red', 'blue', 'yellow', 'chartreuse')

Using just keyword arguments:
func(link_color='red', back_color='blue')

using a combination of positional and keyword
``func('purple', link_color='red', back_color='blue')

using *some_tuple and/or **some_dict
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, **links)

Generic parameters:

Write a new function with the parameters as:
*args and **kwargs

Have it return the colors (use strings for the colors again)
Call it with the same various combinations of arguments used above.
Also have it print args and kwargs directly, so you can be sure you understand what’s going on.
Note that in general, you can’t know what will get passed into **kwargs So maybe adapt your function 
to be able to do something reasonable with any keywords.

"""

def color_parameters(fore_color = "red", 
                    back_color = "blue", 
                    link_color = "yellow", 
                    visited_color = "green"):
    
    # regular = ('red', 'blue')
    # links = {'link_color': 'chartreuse'}
    return (fore_color,
            back_color,
            link_color,
            visited_color)

def color_parameters2(*args, **kwargs):

    print("args", args)
    print("kwargs", kwargs)
    return args, kwargs


def main():
    color_parameters("purple" )
    # color_parameters(fore_color = "red", regular, links)


if __name__ == "__main__":
    main()