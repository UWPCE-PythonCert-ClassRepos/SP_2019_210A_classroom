#! /usr/bin/env python3

"""Simple args testing function"""
def colors(fore_color='black',
           back_color='white',
           link_color='yellow',
           visited_color='blue'):
    """Return input colors or their defaults"""

    return (fore_color, back_color, link_color, visited_color)
