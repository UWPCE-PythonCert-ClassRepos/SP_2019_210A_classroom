def colors(fore_color='black',
           back_color='red',
           link_color='blue',
           visited_color='pink'
           ):

    # print("back_color:", back_color)

    return (fore_color,
            back_color,
            link_color,
            visited_color)



def colors2(*foo, **kwargs):

    # print("back_color:", back_color)
    print("args:", foo)
    print("kwargs:", kwargs)
    return foo, kwargs
