'''
args and kwags lab
'''
def colors(fore_color = 'black',
            back_color = 'red',
            link_color = 'blue',
            visited_color = 'pink'):
    return (fore_color, back_color, link_color, visited_color)

def colors2(*args, **kwargs):

    return args, kwargs
