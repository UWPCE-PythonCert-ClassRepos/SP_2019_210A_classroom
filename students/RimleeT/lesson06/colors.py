def colors(fore_color='black',
            back_color='red',
            link_color='blue',
            visited_color='pink'):
        output = ("The colors are:\n"
              "  fore_color={fore_color}\n"
              "  back_color={back_color}\n"
              "  link_color={link_color}\n"
              "  visited_color={visited_color}")
        output = output.format(fore_color=fore_color,
                           back_color=back_color,
                           link_color=link_color,
                           visited_color=visited_color)
        print(output)
        return output



def colors_args_kwargs(*positional_arg, **keyword_arg):
    return positional_arg, keyword_arg

