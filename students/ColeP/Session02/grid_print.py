# horizontal = ('+ ' + ('- ' * 4)) * 2 + '+\n'
# vertical = ('|' + ' ' * 9) * 2 + '|\n'

# print((horizontal + vertical * 2) * 2 + horizontal)


def prnt_grid(n):
    horizontal = ('+ ' + ('- ' * (n//2))) * 2 + '+\n'
    vertical = ((('|' + ' ' * n) * 2) + '|\n') * (n//2)
    return (horizontal + vertical) * 2 + horizontal


# print(prnt_grid(int(input('what is "n"?'))))

def prnt_grid2(n, m):
    horizontal = (('- ' * m) + '+') * n + '\n'
    vertical = ((('|' + ' ' * m * 2) * n) + '|\n') * m
    return ('+' + horizontal + vertical) * n + '+' + horizontal


print(prnt_grid2(int(input('n')), int(input('m'))))

