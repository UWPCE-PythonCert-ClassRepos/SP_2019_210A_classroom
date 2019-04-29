#!/usr/bin/env python3

# SERIES 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
# Ask the user for another fruit and add it to the end of the list.
# Display the list.
# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
# Add another fruit to the beginning of the list using “+” and display the list.
# Add another fruit to the beginning of the list using insert() and display the list.
# Display all the fruits that begin with “P”, using a for loop.

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the actual list
def list_fruits():

    print("The actual Fruit List is: ")
    for fruit in fruits:
        print(fruit)

    return fruits

# Ask and add a new fruit to Fruit list
def new_fruit():
    new_fruit = input("Which fruit would you like to add to this list?")
    fruits.append(new_fruit)


# Return fruit by index list_name.index(element, start, end)
def find_fruit():
    position = int(input("What position in the list are you looking for? Example: 1"))

    #verify if position exist on the list
    # if position is larger than size of the list, return error message
    if position >= len(fruits):
        print("position not valid in list")

    return position, fruits[position-1]


# Add another fruit to the beginning of the list using “+” and display the list.
def add_with_plus(fruits, added_fruit):

    fruits = [added_fruit] + fruits

    return fruits

# Add another fruit to the beginning of the list using insert()
def add_with_insert():

    fruits.insert(0, "Papaya")
    #list_fruits()

# Display all the fruits that begin with “P”, using a for loop.
def start_with_p():
    print("The fruits in the list that start with 'P' are:")
    for fruit in fruits:
        if fruit[0] == "P":
            print(fruit)


# Display the list
list_fruits()

# Ask the user for another fruit, add it to the end of the list and display list
new_fruit()

pos,returned_fruit = find_fruit()
print(pos, returned_fruit)
# Add another fruit to the beginning of the list using “+” and display the list.
#list_fruits()
fruits = add_with_plus(fruits, 'Grape')
list_fruits()

# Add another fruit to the beginning of the list using insert()
add_with_insert()

# Display all the fruits that begin with “P”, using a for loop.
start_with_p()


# _____________________________________________________________

# SERIES 2

# Using the list created in series 1 above:
# Display the list.
# Remove the last fruit from the list.
# Display the list.
# Ask the user for a fruit to delete, find it and delete it.
# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

