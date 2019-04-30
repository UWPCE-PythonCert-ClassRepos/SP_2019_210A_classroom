#!/usr/bin/env python3

def task_one(input_tuple):
    a, b, c, d = input_tuple
    print('file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}'.format(a, b, c, d))

def task_two(input_tuple):
    a, b, c, d = input_tuple
    print(f'file_{a:0>3d} : {b:.2f}, {c:.2e}, {d:.2e}')

def task_three(input_tuple):
    my_str = "the {} numbers are: ".format(len(input_tuple))
    for i in range(len(input_tuple)):
        my_str = my_str + '{:d}, '
    print(my_str.format(*input_tuple)[:-2])

def task_four(input_tuple):
    print ('{3:0>2d} {4:d} {2:} {0:0>2d} {1:d}'.format(*input_tuple))

def task_five(inlist):
    a, b, c, d = inlist
    buff = 1.2
    str = f'The weight of an {a[:-1].upper()} is {buff * b} and the weight of a {c[:-1].upper()} is {buff * d}'
    print(str)

def task_six():
    data = [("First", 1, 20),("Second", 100, 20000),("Third", 10000, 200000000)]
    for dat in data:
        print("Name:{0:20} Age:{1:^20} cost:{2:5}".format(*dat))
    #extra
    tup = (1,2,3,4,5,6,7,8,9,10)
    for elem in tup: print("{:5}".format(elem), end = '')



if __name__ == '__main__':
    task_one(( 2, 123.4567, 10000, 12345.67))
    task_two(( 2, 123.4567, 10000, 12345.67))
    task_three((2,3,5))
    task_three((2,3,5,7,9,11))
    task_four((4,30,2017,2,27))
    task_five(['oranges', 1.3, 'lemons', 1.1])
    task_six()
