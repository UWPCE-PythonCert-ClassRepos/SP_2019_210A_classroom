#!/usr/bin/env python3

def colors(fore_color="red",
           back_color='blue',
           link_color='green',
           visited_color='lavender'
           ):

    return fore_color, back_color, link_color, visited_color


def colors2(*args,
            **kwargs,
            ):

    return (args, kwargs)

