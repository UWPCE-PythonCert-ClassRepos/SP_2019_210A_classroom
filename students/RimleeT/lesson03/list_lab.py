"""
Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
"""
print('PRINTING SERIES 1 STARTS HERE')
list1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Origin list ", list1)
new_fruit = input("Enter a fruit name: ")
list1.append(new_fruit)
print("Fruit added ", list1)
item_number = int(input("Enter the item number: "))
if item_number<1:
	print ("List starts from 1")
elif item_number > len(list1):
	print ("No item exists at ",item_number)
else:
	print (item_number, list1[item_number-1])
begin_fruit = input("Enter another fruit in the beginning using + : ")
list1 = [begin_fruit] + list1
print('List after adding + : ',list1)
begin_fruit = input("Enter another fruit in the beginning using insert : ")
list1.insert(0, begin_fruit)
print ("Final list: ", list1)
for item in list1:
    if item[0] =='P':
        print ("Fruits starts with 'P' ", item)
print('PRINTING SERIES 1 ENDS HERE')		
		
"""
Series 2
Using the list created in series 1 above:
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
?????(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""

print('PRINTING SERIES 2 STARTS HERE')
print(list1)
print("Deleting the last item...")
del list1[-1]
print(list1)
del_fruit = input ("Enter the fruit to delete from list: ")
for item in list1:
	if item == del_fruit:
		list1.remove(del_fruit)
print(list1)
print('PRINTING SERIES 2 ENDS HERE')	

"""
Series 3
Again, using the list from series 1:
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
"""
print('PRINTING SERIES 3 STARTS HERE')
list1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('list: ',list1)
count = 0
while (count < len(list1)):
    like_dislike = input("Do you like " + list1[count].lower() + ': ')
    if like_dislike.lower() == "yes":
        count = count + 1
    elif like_dislike.lower() == "no":
        del list1[count]
        print("list after delete : ",list1)
    elif like_dislike.lower() != "yes" or like_dislike.lower() != "no":
        print("Enter either 'yes' or 'no'")
print('PRINTING SERIES 3 ENDS HERE')       

"""
Series 4
Once more, using the list from series 1:
Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
"""
print('PRINTING SERIES 4 STARTS HERE')
list1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('list: ',list1)
list2 = []
for item in list1:
    list2.append(item[::-1])
print("New list is: ", list2)
del list2[-1]
print("List after delete: ", list2)
print('PRINTING SERIES 4 ENDS HERE')




