#!/usr/bin/env python3
#strformat
#FredBallyns
#Session03


def file_data_formater(seq):
    return ("file_" + '{:03}' +" :   " + '{:0.2f}' +(", "+ '{:.2E}')*2).format(*seq)


def file_data_formater_diff(seq):
    return ("file_" + '{:05}' +" :   " + '{:0.1f}' +(", "+ '{:.4E}')*2).format(*seq)


def formater(seq):
    l=len(seq)
    return ("The {} numbers are: "+", ".join(["{}"]*l)).format(l,*seq)


def date_formater(seq):
    return ('{:02}'+" " + '{:02}' + " " + '{:04}' +" " + '{:02}' + " " + '{:02}').format(seq[3], seq[4], seq[2], seq[0], seq[1])


def fruit_formater(input, multiplier=1):
    fruit1=input[0]
    if fruit1[-1:]=="s": fruit1=fruit1[:-1]
    weight1=input[1]
    fruit2=input[2]
    if fruit2[-1:]=="s": fruit2=fruit2[:-1]
    weight2=input[3]
    return f"The weight of an {fruit1} is {weight1*multiplier} and the weight of a {fruit2} is {weight2*multiplier}"


def column_formater(input):
    print('{:15}{:4}{:17}'.format('Name','| Age','|     Cost'))
    print('-'*(15+4+17))
    for row in input:
        print('{:15}|{:4}|{:15.2f}'.format(*row))


if __name__ == "__main__":
    # run a test
    a_tuple=( 2, 123.4567, 10000, 12345.67)
    print(file_data_formater(a_tuple))
    print(file_data_formater_diff(a_tuple))

    test1= (1,2,3)
    test2= (1,2,3,4)
    assert formater(test1) == 'The 3 numbers are: 1, 2, 3'
    assert formater(test2) == 'The 4 numbers are: 1, 2, 3, 4'
    print("assertions for formater passed")

    seq = ( 4, 30, 2017, 2, 27)
    assert date_formater(seq) == '02 27 2017 04 30'
    print('assert passed for date_fortmater')

    fruit_test=['oranges', 1.3, 'lemons', 1.1]
    assert fruit_formater(fruit_test) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    print(fruit_formater(fruit_test))
    print(fruit_formater(fruit_test,1.2))
    print('assert passed for fruit_fortmater')

    print('\n')
    input=[('Bob', 32, 3232.32), ('Mike', 25, 225522), ('Jones', 21, 999), ("Rocky", 76, 123456.78)]
    column_formater(input)
    
