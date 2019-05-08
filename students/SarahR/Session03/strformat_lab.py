#!/usr/bin/env python
"
# TASK 1

t = (2, 123.4567, 10000, 12345.67)

# produce -> 'file_002 :   123.46, 1.00e+04, 1.23e+04'

z = "file_{0:03}: {1:.2f}, {2:.2E}, {3:3.2E}"

print("file_{0:03}: {1:.2f}, {2:.2E}, {3:3.2E}".format(2, 123.4567, 10000, 12345.67))

print("file_{0:03}: {1:.2f}, {2:.2E}, {3:3.2E}".format(*t))

# TASK 2

print(f"file_{t[0]:03}: {t[1]:.2f}, {t[2]:.2E}, {t[3]:3.2E}")

# TASK 3

def formatter(in_tuple):

    text_string = 'the {} numbers are: '
    bracket_string = ["{}"]*len(in_tuple)

    form_string = text_string + ','.join(bracket_string)

    return form_string.format(len(in_tuple), *in_tuple)

t= (2,3,5)
t2=(2,3,5,7,9)

print(formatter(t2))

# TASK 4

print("{3:02} {4} {2} {0:02} {1}".format(4, 30, 2017, 2, 27))

# TASK 5

l = ['orange', 1.3, 'lemon', 1.1]

print(f"The weight of an {l[0]} is {l[1]} and the weight of a {l[2]} is {l[3]}.")

print(f"The weight of an {l[0].upper()} is {l[1]*1.2} and the weight of a {l[2].upper()} is {l[3]*1.2}.")

# TASK 6

test = []
test.append(("joao", 30, 1500))
test.append(("maria", 20, 500))
test.append(("carlos", 40, 100000))
test.append(("sarah", 30, 2000000))

print('{:^10}{:^10}{:^10}'.format("name", "age", "cost"))
for tuple in test:
    print('{:10}{:10}{:10}'.format(tuple[0], tuple[1], tuple[2]))

