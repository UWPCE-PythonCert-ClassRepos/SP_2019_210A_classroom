#!/usr/bin/env python3

# task one
# tuple_1 = (2, 123.4567, 10000, 12345.67)
#
# new_str = 'file_{:0>3d}: {:.2f} {:.2e} {:.2e}'.format(tuple_1[0], tuple_1[1], tuple_1[2], tuple_1[3])
#
#
# print(new_str)
#
# # task two
# new_str2 = 'file_%03d: %.2f %.2e %.2e' % (tuple_1[0], tuple_1[1], tuple_1[2], tuple_1[3])
# print(new_str2)
#
#
# # task three
#
# strang = "the 3 numbers are: {:d}, {:d}, {:d}".format(1, 2, 3)
#
# tup_1 = (1, 2, 3)
#
# tup_2 = (3, 5, 5, 7, 8)
#
#
# def formatter(tup):
#     new_str3 = 'the {} numbers are:'.format(len(tup))
#     form = str(' {}, '.format('{:d}'))*(len(tup)-1) + '{:d}'
#     new_str3 = new_str3 + form
#     return new_str3.format(*tup)
#
#
# print(formatter(tup_1))
#
# print(formatter(tup_2))
#
# # task four
#
# tuppie = (4, 30, 2017, 2, 27)
# stringie = '{:d},'*(len(tuppie)-1) + '{:d}'
#
# print(stringie.format(*tuppie[::-1]))
#
# # task five
#
# l1 = ['oranges', 1.3, 'lemons', 1.1]
#
# print(f'The weight of an {l1[0].strip("s").upper()} is {l1[1] * 1.2} and the weight of a {l1[2].strip("s").upper()} is '
#       f'{l1[3] * 1.2}')
#
# task six

omega_tuple = ('name', 'age', 'cost',
               'yogurt', '12 days', '$12.12',
               'crazy cheese', '5 years', '$130.99',
               'cream', '3 days', '$4.75',
               'super cheese', '10 years', '$12000.00000')

omega_new = omega_tuple[5::3]


omega_new_string = ''

for i in omega_new:
    striped_val = i.replace('$', ' ')
    a = '{:.2f}'.format(float(striped_val))
    omega_new_string += a + ','

ugh = omega_new_string.split(',')[0:-1]
print(ugh)

omega_list = list(omega_tuple)

print(omega_list[5::3])

for i in range(len(omega_list[5::3])):
    omega_list[5::3][i] = ugh[i]

print(omega_list)

print(('{:20}{:10}{:20}\n'*5).format(*omega_tuple))

