#!/usr/bin/env python3

#
#Week 3 Assignment 3
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
#

def strformat():
    t = (2,123.4567,10000,12345.67)
    # task1,2
    fname = "file_{:0>3}".format(t[0])
    fnames = []
    fnames.append(fname)
    print(fnames)
    
    fnumber_1 = format(t[1],".2f")
    print(fnumber_1)

    fnumber_2 = format(t[2],"E")
    print(fnumber_2)

    fnumber_3 = format(t[3],".3g")
    print(fnumber_3)

# task 3
def formatter_1(t):
    n = len(t)
    form_string = "The {} numbers are: ".format(n)
    for i in range(n):
        form_string = form_string + " {}".format(t[i])
    #print(form_string)
    return form_string

# task 4
def formatter_2():
    t = (4,30,2017,2,27)
    #print("{3:0>2d} {4} {2} {0:0>2d} {1}".format(*t))
    return "{3:0>2d} {4} {2} {0:0>2d} {1}".format(*t)

# task 5
def formatter_3():
    t = ['oranges', 1.3, 'lemons', 1.1]
    str = f"The weight of {t[0].upper()} is {float(t[1])*1.2} and the weight of {t[2].upper()} is {float(t[3])*1.2}."
    # print(str)
    return str

def formatter_print():
    header = ("Name","Age","Cost")
    row_1 = ("hoho","3","300")
    row_2 = ("koko","10","1000")
    row_3 = ("momo","200","20000")
    print("{:^10} |  {:<10} | {:<10}".format(*header))
    print("{:^10} |  {:<10} | {:<10}".format(*row_1))
    print("{:^10} |  {:<10} | {:<10}".format(*row_2))
    print("{:^10} |  {:<10} | {:<10}".format(*row_3))

if __name__ == "__main__":
    strformat()
    assert formatter_1((2,3,4,9,8,7)) == "The 6 numbers are:  2 3 4 9 8 7"
    assert formatter_2() == "02 27 2017 04 30"
    assert formatter_3() == "The weight of ORANGES is 1.56 and the weight of LEMONS is 1.32."
    formatter_print()
