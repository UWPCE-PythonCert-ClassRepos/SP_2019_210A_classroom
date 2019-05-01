#!usr/bin/env pyhton3.6

'''Module 3 - String Format Lab Excercise'''

'''
************************ TASK 1 ***************************** 
Write a format string that will take the following four element tuple:
(2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
''' 

tup1 =(2, 123.4567, 10000, 12345.67)
print("file_{:0>3d}:   {:.2f}, {:.2e}, {:.2e}".format(tup1[0],tup1[1],tup1[2],tup1[3]))


'''
************************ TASK 2 ***************************** 
Using your results from Task One, repeat the exercise, 
but this time using an alternate type of format string 
(hint: think about alternative ways to use .format() (keywords anyone?), 
and also consider f-strings if you’ve not used them already).
'''

tup1 =(2, 123.4567, 10000, 12345.67)
print(f"file_{tup1[0]:0>3d}:	{tup1[1]:.2f}, {tup1[2]:.2e}, {tup1[3]:.2e}, ")


'''
************************ TASK 3 ***************************** 
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values.
'''

def formatter(in_tuple):
	form_string="the {:d} numbers are: " + ", ".join(["{:d}"]*(len(in_tuple)))
	return form_string.format((len(in_tuple)),*in_tuple)

formatter((2,3,4,5,5))


'''
************************ TASK 4 ***************************** 
Given a 5 element tuple:
(4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
'''

tup2 = (4, 30, 2017, 2, 27)
print("{:0>2d} {:d} {:d} {:0>2d} {:d}".format(tup2[3],tup2[4],tup2[2],tup2[0],tup2[1]))


'''
************************ TASK 5 ***************************** 
 Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher)
'''

lst1 = ['oranges', 1.3, 'lemon', 1.1]
print(f"The weight of an {lst1[0]:s} is {lst1[1]:.1f} and the weight of a {lst1[2]:s} is {lst1[3]:.1f}")

#uppercase and 1.2 times the weight
print(f"The weight of an {lst1[0].upper():s} is {lst1[1]*1.2:.1f} and the weight of a {lst1[2].upper():s} is {lst1[3]*1.2:.1f}")


'''
************************ TASK 6 ***************************** 
Part 1: Write some Python code to print a table of several rows, each with a name, an age and a cost. 
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

Part 2: And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the 
tuple in columns that are 5 charaters wide? It can be done on one short line!
'''

#Part 1
items = [("Phone", 5, 2500.00),("Charger", 7, 10.00),
         ("Sim", 15, 9.00),("Accessories", 9, 750.00)]

for i in items:
    print("Product Name: {:15s} | Product Age: {:5d} | Product Price: {:.2f}".format(*i))

#Part 2
tup3 = range(0,10)
print("{:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5}".format(*tup3))

