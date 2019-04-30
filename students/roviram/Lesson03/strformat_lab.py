#------------------- Script Details-----------------#
# Week 3 Homework: String Formatting Lab
# Miguel Rovira-Gonzalez, 4/28/19, Created the script
#---------------------------------------------------#

# Task 1:
"""Desired Output
'file_002 :  123.46, 1.00e+04, 1.23e+04'
"""
# Data
four_tuple = (2, 123.4567, 10000, 12345.67)
def task_1(four_tuple):
    """String Formatting Lab Assignment Task 1 using Format Method"""
  #  four_tuple = (2, 123.4567, 10000, 12345.67)
    new_tuple = "'{} {}{} {:.2f}, {:.2e}, {:.3e}'".format("file_00" + str(four_tuple[0]), ":", " ", four_tuple[1], four_tuple[2], four_tuple[3])
    print(new_tuple)


# Task 2:
"""Desired Output using an alternative to the format method
'file_002 :  123.46, 1.00e+04, 1.23e+04'
"""
# Data

def task_2(four_tuple):
    """Same Desired Out as Task 1 function except using f strings"""
    new_tuple = f"""{"'file_00"}{four_tuple[0]} {': '}{four_tuple[1]: .2f}, {four_tuple[2]:.2e}, {four_tuple[3]:.3e}'"""
    print(new_tuple)

# Task 3
"""
Rewrite the statement below so it can take an arbitrary amount of numbers
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
"""
def formatter(*args):
    new_tuple = print("'The", len(args), "numbers are:", str(args) + "'")

# Task 4
"""
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
Print this with string formatting (use index to specify positions)
'02 27 2017 04 30'
"""
# Data
five_tuple = (4, 30, 2017, 2, 27)

def task_4(five_tuple):
    new_tuple = f"{five_tuple[3]:0>2d} {five_tuple[4]} {five_tuple[2]} {five_tuple[0]:0>2d} {five_tuple[1]}"
    print(new_tuple)

# Task 5
# Data
fruit_numbers = ['orange', 1.3, 'lemon', 1.1]
def task_5(fruit_numbers):
    new_fruit = f"""{"The weight of an"} {fruit_numbers[0]} is {fruit_numbers[1]} and the weight of a {fruit_numbers[2]} is {fruit_numbers[3]}"""
    upper_fruit = f"""{"The weight of an"} {fruit_numbers[0].upper()} is {fruit_numbers[1] * 1.2} and the weight of a {fruit_numbers[2].upper()} is {fruit_numbers[3] * 1.2}"""
    print(new_fruit)
    print(upper_fruit)

#Task 6
# Data
names = ["Miguel"]
ages = [28]
costs = ["$500"]
final_list = [names, ages, costs]

def task_6(final_list):
    print('{:20}{:20}{:20}'.format('Name:', 'Age:', 'Cost:'))
    print('{:20}{:20}{:20}'.format(str(final_list[0]), str(final_list[1]), str(final_list[2])))












