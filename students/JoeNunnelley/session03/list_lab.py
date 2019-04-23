#! /usr/bin/env python3

"""
When the script is run, it should accomplish the following four series of actions:
Series 1

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding
    to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""
def series1():
    fruit = ['Apples', 'Pears', 'Orange', 'Peaches']
    print(fruit)
    response = input('Add fruit > ')
    fruit.append(response)
    print(fruit)
    response = input('Get fruit number >')
    print('{} => {}'.format(response, fruit[int(response)-1]))
    fruit = ["Lychee"] + fruit
    print(fruit)
    fruit.insert(0, "Guava")
    print(fruit)

    for _ in fruit:
        if "P" in str.upper(_):
            print(_)

    return fruit


fruits = series1()

"""
Series 2

Using the list created in series 1 above:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found.
    Once found, delete all occurrences.)
"""
def series2(fruits):
    print(fruits)
    fruits.pop()
    print(fruits)
    response = input('Which fruit to delete >')
    fruits.remove(response)
    print(fruits)
    fruits = fruits * 2
    print(fruits)
    match = False

    while not match:
        print(fruits)
        response = input('What fruit to eat? >')
        if response in fruits:
            while response in fruits:
                fruits.remove(response)
                print("Chomp! {} ate {}".format(fruits, response))
            match = True


series2(fruits)

"""
Series 3

Again, using the list from series 1:

    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
"""

"""
Series 4

Once more, using the list from series 1:

    Make a new list with the contents of the original, but with all the letters in each item reversed.
    Delete the last item of the original list. Display the original list and the copy.

"""


