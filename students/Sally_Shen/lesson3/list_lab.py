'''
Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
'''

mylist = ["Apples", "Pears", "Oranges", "Peaches"]
series1 = [fruit for fruit in mylist]
print(mylist)
response = input("What's your new fruit? > ")
mylist.append(response)
print(mylist)
response = input("What number will you choose? > ")
print(mylist[int(response)-1])
mylist = ["Coconuts"] + mylist
print(mylist)
mylist.insert(0, "Kiwis")
print(mylist)

new_list = []
for fruit in mylist:
    if fruit[0] == "P":
        new_list.append(fruit)

print(new_list)

'''Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
'''
print(mylist)
mylist.pop()
print(mylist)
response = input("Choose one fruit to delete: > ")
mylist.remove(response)
print(mylist)

'''Series 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
'''

mylist = [fruit.lower() for fruit in mylist]

print(mylist)

newList = []
for fruit in mylist:
    response = input("Do you like " + fruit + "?")
    while response not in ("yes", "no"):
        response = input("Please choose yes or no!")

    if response == "yes":
        newList.append(fruit)


mylist = newList
print(mylist)


'''Series 4
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
'''
newList = []

for fruit in series1:
    newList.append(fruit[::-1])

series1.pop()
print(series1)
print(newList)