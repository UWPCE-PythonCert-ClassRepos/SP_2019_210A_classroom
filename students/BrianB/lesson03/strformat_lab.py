#!/usr/bin/env python3

# -----------------
# Task 1
#
# -----------------

t1 = (2, 123.4567, 10000, 12345.67)
print("file_00%d:  %.2f, %.2e, %.3e" % t1)


# -----------------
# Task 2
#
# -----------------

print("file_00{:d}:  {:.2f}, {:.2e}, {:.3e}"\
      .format(2, 123.4567, 10000, 12345.67))

# -----------------
# Task 3
# -----------------


def formatter(*seq):
    """ Returns a string calling out the number of inputs along
        with printing a string formatting of the tuple values"""
    length = len(seq)
    task_three = "the {} numbers are: " + ", ".join(["{}"]*length)
    return task_three.format(length, *seq)


print(formatter(3, 2, 5, 8, 9))


# -----------------
# Task 4
# -----------------

task_four = (4, 30, 2017, 2, 27)
print("{3:0>2d} {4:d} {2:d} {0:0>2d} {1:d}".format(*task_four))


# -----------------
# Task 5
# -----------------

name = ("orange", "lemon")
weight = (1.3, 1.1)
print(f"The weight of an {name[0].upper()} is {weight[0]*1.2} and the\
 weight of a {name[1].upper()} is {weight[1]*1.2}.")


# -----------------
# Task 6
# -----------------

name_age_cost = [("Ghost", 15, 35000), ("Lady", 6, 410),
                 ("Nymeria", 15, 15100), ("Shaggydog", 12, 5469)]

for item in name_age_cost:
    print("{:17}{:0>2d}{:9,}".format(*item))

