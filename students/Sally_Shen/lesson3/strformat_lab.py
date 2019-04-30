'''
Task One
Write a format string that will take the following four element tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'

Let’s look at each of the four tuple elements in turn:

The first element is used to generate a filename that can help with file sorting.
The idea behind the “file_002” is that if you have a bunch of files that you want to name with numbers that can be sorted,
 you need to “pad” the numbers with zeros to get the right sort order.
 The second element is a floating point number. You should display it with 2 decimal places shown.
 The third value is an integer, but could be any number.
You should display it in scientific notation, with 2 decimal places shown.
The fourth value is a float with a lot of digits – display it in scientific notation with 3 significant figures.

'''

example = ( 2, 123.4567, 10000, 12345.67)

'''the second value, we give right aligned (width 10)'''

print("file_{:0>3d} :".format(example[0]), "{:10.2f}, ".format(example[1]), "{:.2e}, ".format(example[2]), "{:.2e}".format(example[3]))

'''
Task Two
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string 
(hint: think about alternative ways to use .format() (keywords anyone?), 
and also consider f-strings if you’ve not used them already).
'''
example = ( 2, 123.4567, 10000, 12345.67)

print(f"file_{example[0]:0>3d} : {example[1]:10.2f},  {example[2]:.2e},  {example[3]:.2e}")


'''
Task Three
Dynamically Building up format strings
Rewrite:
"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

to take an arbitrary number of values.
'''

def formatter(in_tuple):
    length = len(in_tuple)
    output = "the {:d} numbers are:"
    output += " {:d}," * length
    output = output[:-1]
    output = output.format(len(in_tuple), *in_tuple)
    print(output)
    return output

formatter((1,2,3,4,5))

'''Task Four
Given a 5 element tuple:

( 4, 30, 2017, 2, 27)

use string formating to print:

'02 27 2017 04 30'

Hint: use index numbers to specify positions.
'''


myTuple = (4, 30, 2017, 2, 27)
print("{:0>2d}".format(myTuple[3]), myTuple[4], myTuple[2], "{:0>2d}".format(myTuple[0]), myTuple[1])


'''Task 5
Here’s a task for you: Given the following four element list:

['oranges', 1.3, 'lemons', 1.1]

Write an f-string that will display:

The weight of an orange is 1.3 and the weight of a lemon is 1.1

Now see if you can change the f-string so that it displays the names of the fruit in upper case, 
and the weight 20% higher (that is 1.2 times higher).
'''


myList = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {myList[0][0:-1]} is {myList[1]} and the weight of a {myList[2][0:-1]} is {myList[3]}")


'''
Write some Python code to print a table of several rows, each with a name, an age and a cost. 
Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.

'''
print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))

name = ["Nancy", "Sally", "Sam", "Lisa"]
age = [24, 30, 25, 36]
cost = [1209, 2089, 5790, 5686]

#print("{:<10} ".format("Name"), "{:<10} ".format("Age"), "{:<10} ".format("Cost"))
print("{:<10} ".format("Name:"), "{:<10} ".format(name[0]), "{:<10} ".format(name[1]), "{:<10} ".format(name[2]), "{:<10} ".format(name[3]))
print("{:<10} ".format("Age:"),"{:<10} ".format(age[0]), "{:<10} ".format(age[1]), "{:<10} ".format(age[2]), "{:<10} ".format(age[3]))
print("{:<10} ".format("Cost:"), "{:<10} ".format(cost[0]), "{:<10} ".format(cost[1]), "{:<10} ".format(cost[2]), "{:<10} ".format(cost[3]))





'''And for an extra task, given a tuple with 10 consecutive numbers, 
can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!'''

myTuple = (1,2,3,4,5,6,7,8,9,10)

print(("{:<5d}"*len(myTuple)).format(*myTuple))

