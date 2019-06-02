# String format lab

from decimal import Decimal

four_elements = (2, 123.4567, 10000, 12345.67)


def format_string(e4):
    # Task 1
    formatted_string = "file_{:03d} :   {:.2f}, {:.2e}, {:.3g}".format(e4[0], Decimal(e4[1]), e4[2], e4[3])
    return formatted_string


def format_string_kw(e4):
    # Task 2
    formatted_string = "file_{pad:03d} :   {dec2:.2f}, {sn2:.2e}, {sf3:.3g}".format(pad=e4[0], dec2=Decimal(e4[1]), sn2=e4[2], sf3=e4[3])
    return formatted_string


def variable_input(elements):
    # Task 3.  Understanding what the assignment was asking for took longer than writing the code
    constructed_string = 'the {} numbers are: '.format(len(elements)) + r'{:d}'
    for i in range(len(elements) - 1):
        constructed_string += r', {:d}'
    csf = constructed_string.format(*elements)
    return csf


def task_four(elements):
    # Task 4
    formatted_string = '{:02d} {} {} {:02d} {}'.format(elements[3], elements[4], elements[2], elements[0], elements[1])
    return formatted_string


def f_strings(input):
    # Task 5
    new_string = f"The weight of an {input[0][:-1]} is {input[1]} and the weight of a {input[2][:-1]} is {input[3]}"
    return new_string


def column_alignment(input):
    # Task 6
    table = ''
    for item in input:
        table += '{name}{cost}{age}\n'.format(
            name=' ' * (10 - len(item[0])) + item[0],
            cost=' ' * (6 - len(str(item[1]))) + str(item[1]),
            age=' ' * (6 - len(str(item[2]))) + str(item[2])
        )
    print(table)


assert format_string(four_elements) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert format_string_kw(four_elements) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert variable_input((1, 2, 3, 4, 5, 6, 7)) == "the 7 numbers are: 1, 2, 3, 4, 5, 6, 7"
assert task_four((4, 30, 2017, 2, 27)) == '02 27 2017 04 30'
assert f_strings(['oranges', 1.3, 'lemons', 1.1]) == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
column_alignment([['a', 1000, 1], ['bb', 10, 50], ['ccc', 421, 106]])