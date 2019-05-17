#!/usr/bin/env python3

def colors(fore_color='black', back_color='red', link_color='blue', visited_color='purple'):
    return (fore_color, back_color, link_color, visited_color)


def colors_two(*args, **kwargs):
    return args, kwargs