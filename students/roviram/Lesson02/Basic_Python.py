def not_string(str):
    if str[0:4] == 'not':
        return str

    else:
        return 'not' + ' ' + str
