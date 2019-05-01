"""
Task One
Write a format string that will take the following four element tuple:
( 2, 123.4567, 10000, 12345.67)
and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""
print('PRINTING TASK 1 STARTS HERE')
my_tuple = ( 2, 123.4567, 10000, 12345.67)
print(my_tuple)
#first item
first_item = my_tuple[0]
first_item = f"{first_item:03d}"
first_item = 'file_' + str(first_item)
#second item
second_item = my_tuple[1]
second_item = round(second_item,2)
#third item
third_item = my_tuple[2]
third_item = "{:.2e}".format(third_item)
#fourth item
fourth_item = my_tuple[3]
fourth_item = "{:.2e}".format(fourth_item)
print (first_item + ': ',second_item,third_item,fourth_item)
print('PRINTING TASK 1 ENDS HERE')

"""
Task Two
Using your results from Task One, repeat the exercise, but this time using an alternate type of format string (hint: think about alternative ways to use .format() (keywords anyone?), and also consider f-strings if you’ve not used them already).
"""
print('PRINTING TASK 2 STARTS HERE')
my_tuple = ( 2, 123.4567, 10000, 12345.67)
print(my_tuple)
#first item
first_item = my_tuple[0]
first_item = f"{first_item:03d}"
first_item = 'file_' + str(first_item)
#second item
second_item = my_tuple[1]
second_item = f"{second_item:.2f}"
#third item
third_item = my_tuple[2]
third_item = f"{third_item:.2e}"
#fourth item
fourth_item = my_tuple[3]
fourth_item = f"{fourth_item:.2e}"
print (first_item + ': ',second_item,third_item,fourth_item)
print('PRINTING TASK 2 ENDS HERE')

"""
Task Three
Dynamically Building up format strings
"""
print('PRINTING TASK 3 STARTS HERE')
my_tuple = ( 2, 123.4567, 10000, 12345.67)
fstring = "{:f} " * len(my_tuple)
print(fstring.format(*my_tuple))
print('PRINTING TASK 3 ENDS HERE')

"""
Task Four
Given a 5 element tuple:
( 4, 30, 2017, 2, 27)
use string formating to print:
'02 27 2017 04 30'
Hint: use index numbers to specify positions.
"""
print('PRINTING TASK 4 STARTS HERE')
my_tuple = ( 4, 30, 2017, 2, 27)
print(f'{my_tuple[3]:02d} {my_tuple[4]} {my_tuple[2]} {my_tuple[0]:02d} {my_tuple[1]}')
print('PRINTING TASK 4 ENDS HERE')

"""
Task Five
Here’s a task for you: Given the following four element list:
['oranges', 1.3, 'lemons', 1.1]
Write an f-string that will display:
The weight of an orange is 1.3 and the weight of a lemon is 1.1
Now see if you can change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
"""
print('PRINTING TASK 5 STARTS HERE')
fruits = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {fruits[0].upper()} is {fruits[1]*1.2} and the weight of a {fruits[2].upper()} is {fruits[3]*1.2}')
print('PRINTING TASK 5 ENDS HERE')

"""
Task Six
Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print the tuple in columns that are 5 charaters wide? It can be done on one short line!
"""
print('PRINTING TASK 6 STARTS HERE')
print("{0:20}{1:<5}{2:>10}".format('Name','Age','Cost'))
my_tuple = [('Sam',30,10000),('Ritu',31,20000),('Pal',25,400000)]
for item in my_tuple:
    print("{0:20}{1:<5}${2:>10}".format(*item))
    
my_tuple2 = (1,2,3,4,5,6,7,8)
print(('{:5}\n'*len(my_tuple2)).format(*my_tuple2))
print('PRINTING TASK 6 ENDS HERE')














