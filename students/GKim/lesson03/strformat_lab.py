"""
Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'

TASK 2

Using your results from Task One, repeat the exercise, but this time using an alternate type of format 
string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider
 f-strings if you’ve not used them already).

TASK 3

Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)


"""
tup = ( 2, 123.4567, 10000, 12345.67)
tup2 = ( 4, 30, 2017, 2, 27)
four_elements = ['oranges', 1.3, 'lemons', 1.1]

def task1(tup):
    task_1 ="Output:  file_{:0>3d}:   {:.2f}, {:.2e}, {:.3g}".format(tup[0],tup[1],tup[2],tup[3])
    print(task_1)

def task2(tup):
    task_2 =f"Output:  file_{tup[0]:0>3d}:   {tup[1]:.2f}, {tup[2]:.2e}, {tup[3]:.3g}"
    print(task_2)

def formatter(in_tuple):
    form_string = "formatter - file_{:0>3d}:   {:.2f}, {:.2e}, {:.3g}"

    print(form_string.format(*in_tuple))

def task_4(tup2):
    task_4 = f"{tup2[3]:0>2d}, {tup2[4]}, {tup2[2]}, {tup2[0]:0>2d}, {tup2[1]}"
    print(task_4)

def task_5(four_elements):
    fourElem = f"the weight of and {four_elements[0]} is {four_elements[1]} and the weight of a {four_elements[2]} is {four_elements[3]}"
    print(fourElem)

def task_6():
    t_six = print("{:<20}|{:^15}|{:^15}|{:>15}".format('First', '$99.01', 'Second', '$88.09'))
    return t_six


def main():
    task1(tup)
    task2(tup)
    formatter(tup)
    task_4(tup2)
    task_5(four_elements)
    task_6()

if __name__ == "__main__": main()
    