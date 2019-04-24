#! /usr/bin/env python3

"""
List Lab Excercises
Author : Joe Nunnelley
"""
def series1():
    """
    When the script is run, it should accomplish the following four series of actions:
    Series 1

        Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
        Display the list (plain old print() is fine…).
        Ask the user for another fruit and add it to the end of the list.
        Display the list.
        Ask the user for a number and display the number back to the user and the
        fruit corresponding
        to that number (on a 1-is-first basis). Remember that Python uses zero-based
        indexing, so you will need to correct.
        Add another fruit to the beginning of the list using “+” and display the list.
        Add another fruit to the beginning of the list using insert() and display the list.
        Display all the fruits that begin with “P”, using a for loop.
    """
    print()
    print('>> Series 1 <<')
    print()
    fruit = ['Apples', 'Pears', 'Orange', 'Peaches']
    print(fruit)
    response = input('Add fruit > ')
    fruit.append(response)
    print(fruit)
    response = input('Get fruit number >')
    try:
        print('{} => {}'.format(response, fruit[int(response)-1]))
    except IndexError as identifier:
        print("Index not found in list: {}\n{}".format(int(response) - 1, identifier))

    fruit = ["Lychee"] + fruit
    print(fruit)
    fruit.insert(0, "Guava")
    print(fruit)

    for _ in fruit:
        if "P" in str.upper(_):
            print(_)

    return fruit


def series2(fruits_in):
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
    print()
    print('>> Series 2 <<')
    print()
    print(fruits_in)
    fruits_in.pop()
    print(fruits_in)
    response = input('Which fruit to delete >')

    try:
        fruits_in.remove(response)
    except ValueError as identifier:
        print("Did not find this item: {}\n{}".format(response, identifier))

    print(fruits_in)
    fruits_in = fruits_in * 2
    print(fruits_in)
    match = False

    while not match:
        print(fruits_in)
        response = input('What fruit to eat? >')
        if response in fruits_in:
            while response in fruits_in:
                try:
                    fruits_in.remove(response)
                    print("Chomp! {} ate {}".format(fruits_in, response))
                except ValueError as identifier:
                    print("Did not find this item: {}\n{}".format(response, identifier))

            match = True


def series3(fruits_in):
    """
    Series 3

    Again, using the list from series 1:

        Ask the user for input displaying a line like “Do you like apples?” for
        each fruit in the list (making the fruit all lowercase).
        For each “no”, delete that fruit from the list.
        For any answer that is not “yes” or “no”, prompt the user to answer with
        one of those two values (a while loop is good here)
        Display the list.
    """
    print()
    print('>> Series 3 <<')
    print()
    fruits_local = fruits_in[:]
    for fruit in fruits_in:
        response = None
        while response not in ['yes', 'no']:
            print(fruits_local)
            response = input("Do you like {}? (yes|no)".format(str.lower(fruit)))

            if response == "no":
                print('Throwout {}'.format(fruit))
                while fruit in fruits_local:
                    try:
                        fruits_local.remove(fruit)
                    except ValueError as identifier:
                        print("Did not find this item: {}\n{}".format(response, identifier))

    print(fruits_local)


def series4(fruits_in):
    """
    Series 4

    Once more, using the list from series 1:

        Make a new list with the contents of the original, but with all the letters
        in each item reversed.
        Delete the last item of the original list. Display the original list and the copy.

    """
    print()
    print('>> Series 4 <<')
    print()
    print("OLD LIST: {}".format(fruits_in))
    fruits_local = []
    for _ in fruits_in:
        fruits_local.append(_[::-1])

    fruits_in.pop()
    print("SHORTEND LIST: {}".format(fruits_in))
    print("NEW LIST: {}".format(fruits_local))


if __name__ == "__main__":
    fruits = series1()
    series2(fruits)
    series3(fruits)
    series4(fruits)
