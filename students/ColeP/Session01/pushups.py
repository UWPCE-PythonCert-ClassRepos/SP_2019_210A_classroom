# Sleep In
def sleep_in(weekday, vacation):
    if vacation == 'y':
        return True

    if weekday == 'y':
        return False
    elif weekday == 'n':
        return True


print(sleep_in(input('weekday '), input('vacation ')))


# Monkey Trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False


print(monkey_trouble(input('is a smiling?'), input('is b smiling?')))

# sum_double
def sum_double(a, b):
    if a == b:
        return a * 4
    else:
        return a + b


print(sum_double(int(input('a')), int(input('b'))))
