#!/usr/bin/env python3.6

'''Module 3 - List Lab Excercise'''

'''
Series 1
- Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
- Display the list (plain old print() is fine…)
- Ask the user for another fruit and add it to the end of the list
- Display the list
- Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).\
	Remember that Python uses zero-based indexing, so you will need to correct
- Add another fruit to the beginning of the list using “+” and display the list
- Add another fruit to the beginning of the list using insert() and display the list
- Display all the fruits that begin with “P”, using a for loop'''

def series1():
	series1.fruits=['Apple','Pear', 'Orange','Peach']
	print(series1.fruits)
	series1.fruits.append(input('Enter a new fruit -->'))
	print(series1.fruits)
	item_no = int(input('Enter a number from 1 - 5 -->'))
	print("The fruit corresponding to the number",str(item_no),"you have entered is",series1.fruits[item_no -1])
	new_fruit=input('Enter a new fruit -->')
	series1.fruits = [new_fruit] + series1.fruits
	print (series1.fruits)
	series1.fruits.insert(0,(input('Enter a new fruit -->')))
	print(series1.fruits)
	for f in series1.fruits:
		if f.lower().startswith('p'):
			print(f)
	return series1.fruits 

series1()

'''
Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
'''

def series2():
	fruits = series1.fruits
	print(fruits)
	fruits.pop()
	print(fruits)
	fruits.remove((input('Enter fruit you want to delete from the above list -->')))
	print (fruits)
	return fruits

series2()


'''
Series 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
'''

def series3():
	fruits = series1.fruits 
	for i in fruits:
		print ("Do you like "+i.lower()+" ?")
		response =input('Enter y or n-->')
		if response.lower() == 'y':
			fruits.remove(i)
		elif response.lower() =='n':
			continue
		else:
			print('Enter either y or n as you response')
	print("These are the fruits left in the list",fruits)

series3()


'''
Series 4
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
'''

def series4():
	fruits = series1.fruits
	fruits.pop()
	updated_original = fruits
	print("The original list is: ", updated_original)
	updated_fruits = [f[::-1] for f in fruits][::-1]
	print("The new list is: ", updated_fruits)

series4()
